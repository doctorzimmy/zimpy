import re, unicodedata as ud
try:
    from unidecode import unidecode
except Exception:
    def unidecode(s): return s  # fallback

def _sanitize(name: str, replacement: str = "_") -> str:
    s = ud.normalize("NFKC", name)
    s = "".join(ch for ch in s if ud.category(ch) not in {"Cc","Cf"})       # drop zero-width/BOM/etc.
    s = "".join(replacement if ch.isspace() else ch for ch in s)            # any Unicode space -> _
    s = unidecode(s)
    s = re.sub(r'[^A-Za-z0-9_]', replacement, s)
    s = re.sub(rf'{re.escape(replacement)}+', replacement, s).strip(replacement)
    if s[:1].isdigit(): s = replacement + s
    return s or "col"

def kill_wonky(df, replacement: str = "_"):
    out = df.copy()
    new = [_sanitize(c, replacement) for c in out.columns]
    seen, final = {}, []
    for n in new:
        if n in seen:
            seen[n] += 1; final.append(f"{n}_{seen[n]}")
        else:
            seen[n] = 0;  final.append(n)
    out.columns = final
    return out
