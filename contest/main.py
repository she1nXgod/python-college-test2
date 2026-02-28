def create_phone_number(lst: list) -> str:
    s = ""
    for i in lst:
        s += str(i)
    return "(" + s[0:3] + ") " + s[3:6] + "-" + s[6:]

def duplicate_encode(text: str) -> str:
    text = text.lower()
    res = ""
    for i in text:
        if text.count(i) > 1:
            res += ")"
        else:
            res += "("
    return res

def is_valid_walk(walk: list) -> bool:
    if len(walk) != 10: return False
    if walk.count('n') == walk.count('s') and walk.count('w') == walk.count('e'):
        return True
    return False

def move_zeros(lst: list) -> list:
    res = []
    zeros = []
    for i in lst:
        if i == 0 and type(i) == int:
            zeros.append(i)
        else:
            res.append(i)
    return res + zeros

def find_uniq(lst: list):
    for i in lst:
        if lst.count(i) == 1:
            return i
