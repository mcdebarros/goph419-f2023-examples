from goph419.binary import (
    binary_int,
    binary_float,
)


def main():
    # test the Mauricio number
    a = 728226
    a_str = binary_int(a)
    a_exp = "0 0000000000010110001110010100010"
    print(f"test binary_int({a})")
    print(f"expected: {a_exp}\nactual  : {a_str}\n")

    # test an exact power of 2
    a = -16
    a_str = binary_int(a)
    a_exp = "1 0000000000000000000000000010000"
    print(f"test binary_int({a})")
    print(f"expected: {a_exp}\nactual  : {a_str}\n")

    # test a value entered as a binary literal
    a = 0b01110011001100011000
    a_str = binary_int(a)
    a_exp = "0 0000000000001110011001100011000"
    print(f"test binary_int({a})")
    print(f"expected: {a_exp}\nactual  : {a_str}\n")

    # test an int providing the (optional) number of bits
    a = 18
    b = 11
    a_str = binary_int(a, b)
    a_exp = "0 0000010010"
    print(f"test binary_int({a}, {b})")
    print(f"expected: {a_exp}\nactual  : {a_str}\n")

    # test an unsigned int, also providing the number of bits
    a = 18
    b = 11
    s = False
    a_str = binary_int(a, b, s)
    a_exp = "00000010010"
    print(f"test binary_int({a}, {b}, {s})")
    print(f"expected: {a_exp}\nactual  : {a_str}\n")

    # test the Mauricio number as a float
    a = 728226
    a_str = binary_float(a)
    a_exp = ("0 0 0000010100 "
             + "10110001110010100010000000000000000000000000000000000")
    print(f"test binary_float({a})")
    print(f"expected: {a_exp}\nactual  : {a_str}\n")

    # test a negative float that is below 0.5 (i.e. negative exponent)
    a = -0.01567
    a_str = binary_float(a)
    a_exp = ("1 1 0000000101 "
             + "10000000010111100101111100110000111001111111111101011")
    print(f"test binary_float({a})")
    print(f"expected: {a_exp}\nactual  : {a_str}\n")


if __name__ == "__main__":
    main()
