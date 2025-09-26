import re, unicodedata as ud
import pandas as pd

_ALLOWED_SINGLE = re.compile(r"[A-Za-z0-9_]")

# Specific space code points you care about
_SPACE_TAGS = {
    "\u00A0": "nbsp",
    "\u202F": "nnbsp",
    "\u2009": "thin-space",
    "\u2007": "figure-space",
    "\u200A": "hair-space",
    "\u3000": "ideographic-space",
}

_ZERO_WIDTH = {"\u200B", "\u200C", "\u200D", "\uFEFF"}  # ZWSP, ZWNJ, ZWJ, BOM/ZWNBSP
_BIDI_MARKS = {"\u200E", "\u200F", "\u202A", "\u202C", "\u2066", "\u2067", "\u2069"}

def _is_variation_selector(cp: int) -> bool:
    return (0xFE00 <= cp <= 0xFE0F) or (0xE0100 <= cp <= 0xE01EF)

def _is_noncharacter(cp: int) -> bool:
    # U+FDD0..FDEF and every U+..FFFE/U+..FFFF across planes
    return (0xFDD0 <= cp <= 0xFDEF) or ((cp & 0xFFFE) == 0xFFFE and cp <= 0x10FFFF)

def _reason_for(ch: str) -> str | None:
    cp = ord(ch)
    cat = ud.category(ch)  # e.g., 'Lu','Mn','Co','So'
    if ch in _SPACE_TAGS:
        return _SPACE_TAGS[ch]
    if ch in _ZERO_WIDTH:
        return "zero-width"
    if ch in _BIDI_MARKS:
        return "bidi-mark"
    if ch.isspace():
        return "space"
    if _is_variation_selector(cp):
        return "variation-selector"
    if ud.combining(ch):                # combining accents, etc. (Mn)
        return "combining"
    if 0xFF00 <= cp <= 0xFFEF:          # Halfwidth/Fullwidth forms block
        return "fullwidth"
    if cat == "Co":                     # private-use
        return "private-use"
    if _is_noncharacter(cp):
        return "noncharacter"
    if cat == "So" and cp >= 0x1F000:   # symbols/emoji-ish (heuristic)
        return "emoji/symbol"
    if cp > 127:
        return "non-ASCII"
    if not _ALLOWED_SINGLE.fullmatch(ch):
        return "not-identifier"         # ASCII punctuation like '-' etc.
    return None

def see_wonky(df: pd.DataFrame) -> pd.DataFrame:
    """
    List columns that violate our header rules and why.

    Flags include (not exhaustive): 'nbsp','nnbsp','thin-space','figure-space',
    'hair-space','ideographic-space','zero-width','bidi-mark','combining',
    'variation-selector','fullwidth','private-use','noncharacter',
    'emoji/symbol','non-ASCII','not-identifier','space'.

    Returns a DataFrame with:
      - column: original header
      - reason: comma-joined tags found in that name
      - codepoints: unique offending code points as HEX (e.g. "00A0 200B FF21")
    """
    rows = []
    for col in df.columns:
        reasons, codes = set(), set()
        for ch in col:
            r = _reason_for(ch)
            if r:
                reasons.add(r)
                codes.add(f"{ord(ch):04X}")
        if reasons:
            rows.append({
                "column": col,
                "reason": ",".join(sorted(reasons)),
                "codepoints": " ".join(sorted(codes)),
            })
    return pd.DataFrame(rows, columns=["column","reason","codepoints"])
