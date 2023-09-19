from goph419.binary import binary_converter


def main():
    a = 728226
    a_str = binary_converter(a)
    a_exp = "0 0000000000010110001110010100010"
    print("test binary_converter()")
    print(f"value: {a}\nexpected: {a_exp}\nactual  : {a_str}")


if __name__ == "__main__":
    main()
