def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    s1_len = len(s1)
    s2_len = len(s2)
    min_str = ''
    if s1_len == 0 and s2_len == 0:
        return min_str
        
    other_str = ''
    if s1_len > s2_len:
        min_str = s2
        other_str = s1
    else:
        min_str = s1
        other_str = s2
        
    laced = ''
    for i in range(len(min_str)):
        laced = laced + s1[i] + s2[i]
        
    for i in range(len(min_str), len(other_str)):
        laced += other_str[i]
        
    return laced