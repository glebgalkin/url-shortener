class Base62Encoder:
    CHARS = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    BASE = 62

    @staticmethod
    def __encode_62(num: int) -> str:
        """Encodes a number into a Base62 string (private method)."""
        if num == 0:
            return Base62Encoder.CHARS[0]
        res = ''
        while num > 0:
            remainder = num % Base62Encoder.BASE
            res = Base62Encoder.CHARS[remainder] + res
            num //= Base62Encoder.BASE
        return res

    @staticmethod
    def __decode_62(s: str) -> int:
        """Decodes a Base62 string back into a number (private method)."""
        res = 0
        for index, val in enumerate(s):
            power = len(s) - index - 1
            res += Base62Encoder.BASE ** power * Base62Encoder.CHARS.index(val)
        return res

    '''
    Strings Are Not Numbers
    To encode a string into Base62, we first need to turn the string into a number.

    - Convert the string into its binary form (bytes).
    - Treat the binary data as a single large number.
    '''
    @staticmethod
    def encode(s: str) -> str:
        """Encodes a string into a Base62 string."""
        if not s:
            return ''
        big_int = int.from_bytes(s.encode('utf-8'), byteorder='big')
        return Base62Encoder.__encode_62(big_int)

    '''
    Why Does Adding 7 Work?
    Adding 7 ensures the remainder (extra bits) bumps the division up to the next integer. Here's why:

    Examples:

    Bit Length = 8 (Perfectly divisible by 8)
    (8 + 7) // 8 = 15 // 8 = 1 byte

    Bit Length = 39 (Not divisible by 8)
    (39 + 7) // 8 = 46 // 8 = 5 bytes

    Bit Length = 45 (Not divisible by 8)
    (45 + 7) // 8 = 52 // 8 = 6 bytes
    '''
    @staticmethod
    def decode(encoded_str: str) -> str:
        """Decodes a Base62 string back into the original string."""
        if not encoded_str:
            return ''
        big_int = Base62Encoder.__decode_62(encoded_str)
        bytes_needed = (big_int.bit_length() + 7) // 8
        byte_representation = big_int.to_bytes(bytes_needed, byteorder='big')
        return byte_representation.decode('utf-8')

if __name__ == '__main__':
    original_string = "hello"
    encoded = Base62Encoder.encode(original_string)
    print(f"Encoded: {encoded}")

    decoded = Base62Encoder.decode(encoded)
    print(f"Decoded: {decoded}")

    assert original_string == decoded
