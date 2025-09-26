# Re-export your core functions (keep the "wonky" names)
from .detect_wonky import detect_wonky
from .see_wonky    import see_wonky
from .kill_wonky   import kill_wonky

# --- Demo data: auto-create a test DataFrame with “wonky” headers ---
import pandas as pd

# Representative troublemakers
WONKY = [
    "\u00A0",      # NBSP
    "\u202F",      # narrow NBSP
    "\u2009",      # thin space
    "\u2007",      # figure space
    "\u200A",      # hair space
    "\u200B",      # zero-width space
    "\u200C",      # ZWNJ
    "\u200D",      # ZWJ
    "\uFEFF",      # BOM / ZWNBSP
    "\u200E",      # LRM
    "\u200F",      # RLM
    "\u202A",      # LRE
    "\u202C",      # PDF
    "\u2066",      # LRI
    "\u2067",      # RLI
    "\u2069",      # PDI
    "\u0301",      # combining acute
    "\u0651",      # Arabic shadda (combining)
    "\u03B1",      # Greek alpha
    "\u0410",      # Cyrillic A
    "\uFF21",      # Fullwidth A
    "\u3000",      # Ideographic space
    "\U0001F600",  # 😀
    "\uFE0F",      # variation selector-16
    "\uE000",      # private-use
    "\uFDD0",      # noncharacter
]

def suspicious_columns():
    """Return column names containing representative 'wonky' characters."""
    return [f"col{i}{ch}x" for i, ch in enumerate(WONKY, 1)] + ["e\u0301_name", "price\u00A0usd"]

def suspicious_df(rows: int = 1) -> pd.DataFrame:
    """Construct a tiny demo DataFrame with 'wonky' headers."""
    cols = suspicious_columns()
    return pd.DataFrame([[1] * len(cols) for _ in range(rows)], columns=cols)

# Create a small demo DF at import time (handy for live demos)
_test_df = suspicious_df()

def demo_df(copy: bool = True) -> pd.DataFrame:
    """Get the built-in demo DataFrame (copy by default so students can mutate safely)."""
    return _test_df.copy(deep=True) if copy else _test_df

__all__ = [
    "detect_wonky", "see_wonky", "kill_wonky",
    "WONKY", "suspicious_columns", "suspicious_df", "demo_df", "test_df"
]

# Keep 'test_df' available for quick access, but prefer demo_df() in notebooks.
test_df = _test_df
