# TO DECIMAL
def dms2dec(d, m, s):
    """
    Degrees, minutes, seconds to decimal degrees.
    (e.g. DEC)
    """
    return d + (m/60) + (s/3600)

def hms2dec(h, m, s):
    """
    Hours, minutes, seconds to decimal degrees.
    (e.g. RA)
    """
    return (h*15) + (m/60)*15 + (s/3600)*15

# FROM DECIMAL
def dec2dms(dd):
    """
    (e.g. DEC)
    """
    d = int(dd)
    m = int((dd - d) * 60)
    s = (dd - d - m / 60) * 3600
    return (d, m, s)

def dec2hms(dd):
    """
    (e.g. RA)
    """
    h = int(dd / 15)
    m = int(((dd/15)-h)*60)
    s = ((((dd/15)-h)*60)-m)*60
    return (h, m, s)