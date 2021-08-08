def is_numeric(s):
    if not s:
        return False

    numeric, pos = scan_integer(s)

    if pos < len(s) and s[pos] == '.':
        numeric_dec, pos = scan_unsigned_integer(s[pos + 1:])
        numeric = numeric or numeric_dec

    if pos < len(s) and (s[pos] == 'e' or s[pos] == 'E'):
        if pos + 1 >= len(s):
            return False
        numeric_exp, _ = scan_integer(s[pos + 1:])
        numeric = numeric_exp and numeric

    return numeric


def scan_integer(s):
    if not s:
        return False

    i = 0
    if s[i] == '+' or s[i] == '-':
        i += 1

    numeric, pos = scan_unsigned_integer(s[i:])
    return numeric, i + pos


def scan_unsigned_integer(s):
    if not s:
        return False
    i = 0
    while i < len(s):
        if '0' <= s[i] <= '9':
            i += 1
        else:
            return False, i
    return i > 0, i


if __name__ == '__main__':
    print(is_numeric('5e2'))