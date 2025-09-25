import re, unicodedata as ud
import pandas as pd
_ALLOWED_SINGLE = re.compile(r'[A-Za-z0-9_]')

def see_wonky(df) -> pd.DataFrame:
    """
    Return a small table listing columns that violate the rules.

    The result includes:
      - column : the original column name
      - reason : a short tag like 'non-ASCII', 'space', 'zero-width', 'not-identifier'
      - codepoints : the hex codepoints of offending characters (e.g., '00A0 200B')

    Parameters
    ----------
    df : pandas.DataFrame

    Returns
    -------
    pandas.DataFrame
        Empty if nothing is wonky; otherwise one row per offending column.

    Examples
    --------
    >>> import zimpy.ventclean as vc
    >>> vc.see_wonky(vc.test_df).head(3)
          column       reason   codepoints
    0      col1 x       space        0020
    1      col6​x   zero-width         200B
    2     col21Ａx   non-ASCII        FF21
    """
    rows = []
    for col in df.columns:
        bads = [(ch, f"U+{ord(ch):04X}", ud.name(ch, "?"))
                for ch in col if not _ALLOWED_SINGLE.fullmatch(ch)]
        if bads:
            rows.append({"column": col, "bad_chars": bads})
    return pd.DataFrame(rows, columns=["column", "bad_chars"])
