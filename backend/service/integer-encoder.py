CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
BASE = 62

def encode_62(num: int) -> str:
    res = ''
    while num > 0:
        remainder = num % BASE
        res = CHARS[remainder] + res
        num //= BASE
    return res

def decode_62(s: str) -> int:
    res = 0
    for index, val in enumerate(s):
        power = len(s) - index - 1
        res += BASE ** power * CHARS.index(val)
    return res




if __name__ == '__main__':
    res_1 = encode_62(1234567890123)
    res_2 = encode_62(38474)

    print(decode_62(res_1))
    print(decode_62(res_2))


