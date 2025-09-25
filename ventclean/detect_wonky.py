import re
_ALLOWED_FULL = re.compile(r'^[A-Za-z0-9_]+$')

def detect_wonky(df) -> bool:
    """True if ANY column name contains a char outside [A-Za-z0-9_]."""
    return any(not _ALLOWED_FULL.fullmatch(c) for c in df.columns)
