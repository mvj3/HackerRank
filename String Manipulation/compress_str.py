"""
Problem: Compress a string such that 'AAABCCDDDD' becomes 'A3BC2D4'.
Only compress the string if it saves space.
"""

def compress1st(s):
    """
    unfinished:
    1. None -> None
    2. 'AABBCC' -> 'AABBCC' # use A2 if only save space
    """
    if len(s) <= 1:
        return s

    result = s[0]
    cnt = 1
    for c in s[1:]:
        if c == result[-1:]:
            cnt += 1
        else:
            if cnt > 1:
                result += str(cnt)
            result += c
            cnt = 1
    if cnt > 1:
        result += str(cnt)
    return result

def compress(s):
    if s is None or len(s) <= 1:
        return s

    result = s[0]
    cnt = 1
    for c in s[1:]:
        if c == result[-1:]:
            cnt += 1
        else:
            if cnt > 1:
                result += str(cnt)
            result += c
            cnt = 1
    if cnt > 1:
        result += str(cnt)
    return result if len(result) < len(s) else s


print("compress 'AAABCCDDDD' should become 'A3BC2D4', and the result is",
      compress('AAABCCDDDD'))
print("compress '' should become '', and the result is",
      compress(''))
print("compress 'A' should become 'A', and the result is",
      compress('A'))
print("compress 'AA' should become 'AA', and the result is",
      compress('AA'))
print("compress 'AB' should become 'AB', and the result is",
      compress('AB'))
