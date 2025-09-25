# zimpy/datewizard/convert.py
import pandas as pd

# ---- shared formatter: make pure date strings like 9/16/2025 ----
def _format_date_strings(parsed: pd.Series, *, style="mdy", zero_pad=False, sep="/") -> pd.Series:
    # normalize to midnight UTC so times vanish
    if getattr(parsed.dt, "tz", None) is not None:
        parsed = parsed.dt.tz_convert("UTC")
    parsed = parsed.dt.normalize()

    M = parsed.dt.month.astype("Int64")
    D = parsed.dt.day.astype("Int64")
    Y = parsed.dt.year.astype("Int64")

    def fmt(col):
        s = col.astype("string")
        return s.str.zfill(2) if zero_pad else s

    m, d, y = fmt(M), fmt(D), Y.astype("string")
    if style.lower() == "mdy":
        out = m + sep + d + sep + y
    elif style.lower() == "dmy":
        out = d + sep + m + sep + y
    elif style.lower() == "ymd":
        out = y + sep + m + sep + d
    else:
        raise ValueError("style must be 'mdy' | 'dmy' | 'ymd'")
    return out  # pandas StringDtype; <NA> for missing

# ---- explicit converters (dates only, output = strings) ----

def to_date_unix_s(s, **fmt):
    parsed = pd.to_datetime(s, unit="s", errors="coerce", utc=True)
    return _format_date_strings(parsed, **fmt)

def to_date_unix_ms(s, **fmt):
    parsed = pd.to_datetime(s, unit="ms", errors="coerce", utc=True)
    return _format_date_strings(parsed, **fmt)

def to_date_unix_us(s, **fmt):
    parsed = pd.to_datetime(s, unit="us", errors="coerce", utc=True)
    return _format_date_strings(parsed, **fmt)

def to_date_unix_ns(s, **fmt):
    parsed = pd.to_datetime(s, unit="ns", errors="coerce", utc=True)
    return _format_date_strings(parsed, **fmt)

def to_date_days_1970(s, **fmt):
    parsed = pd.to_datetime(s, unit="D", origin="1970-01-01", errors="coerce", utc=True)
    return _format_date_strings(parsed, **fmt)

def to_date_excel_1900(s, **fmt):
    parsed = pd.to_datetime(s, unit="D", origin="1899-12-30", errors="coerce", utc=True)  # handles Excel's 1900 bug
    return _format_date_strings(parsed, **fmt)

def to_date_excel_1904(s, **fmt):
    parsed = pd.to_datetime(s, unit="D", origin="1904-01-01", errors="coerce", utc=True)
    return _format_date_strings(parsed, **fmt)

def to_date_sas_date(s, **fmt):
    parsed = pd.to_datetime(s, unit="D", origin="1960-01-01", errors="coerce", utc=True)
    return _format_date_strings(parsed, **fmt)

def to_date_sas_datetime(s, **fmt):
    parsed = pd.to_datetime(s, unit="s", origin="1960-01-01", errors="coerce", utc=True)
    return _format_date_strings(parsed, **fmt)

def to_date_string(s, *, dayfirst=None, **fmt):
    """Generic string parser (ISO, m/d/Y, etc.)."""
    parsed = pd.to_datetime(s, errors="coerce", dayfirst=dayfirst, utc=True)
    return _format_date_strings(parsed, **fmt)

# ---- classroom preview helper ----
def see_dates(s, n=8, **fmt):
    parsed = to_date_string(s, **fmt) if s.dtype == "object" else None
    return pd.DataFrame({
        "raw": s.head(n),
        "date": (parsed if parsed is not None else to_date_string(s, **fmt)).head(n)
    })
