def binary_int(value, bits=32, signed=True):
    """Convert an integer into a binary string.

    Inputs
    ------
    value : int
        The integer to convert
    bits : int, optional, default=32
        The number of bits (including the sign bit)
    signed : bool, optional, default=True
        Flag for signed or unsigned integer

    Returns
    -------
    str
        A string with a binary representation of the input
    """
    # check that both value and bits are convertible to int
    value = int(value)
    bits = int(bits)
    # make sure that bits has a sensible value
    if bits < 1:
        raise ValueError(f"{bits} is an invalid number of bits, "
                         + "should be a positive integer")
    # get the sign bit if it is a signed integer
    if signed:
        int_str = "0 "
        if value < 0:
            int_str = "1 "
        bits -= 1
    else:
        int_str = ""
    # build the binary integer string
    rem = abs(value)
    for b in range(bits-1, -1, -1):
        if (dig_val := 2 ** b) <= rem:
            int_str += "1"
            rem -= dig_val
        else:
            int_str += "0"
    return int_str


def binary_float(value):
    """Convert a float into a binary string.

    Inputs
    ------
    value : float_like
        The number to convert

    Returns
    -------
    str
        A string with a binary representation of the input

    Notes
    -----
    Follows the IEEE-754 standard for a 64-bit float.
    """
    # test that the provided value is convertible to float
    value = float(value)
    # get the sign information
    sgn_str = "0"
    if value < 0:
        sgn_str = "1"
    sig = abs(value)
    # normalize the signficand, determine the exponent
    exp = 0
    while sig < 0.5:
        sig *= 2
        exp -= 1
    while sig >= 1.0:
        sig /= 2
        exp += 1
    # get the exponent string, float64 has 11 exponent bits (incl sign bit)
    exp_str = binary_int(exp, 11)
    # compute the significand bits, float64 has 53 significand bits
    # Note: the first bit for 2 **- 1 is not actually stored, it is always 1
    sig_str = ""
    rem = sig
    for b in range(-1, -54, -1):
        if (dig_val := 2 ** b) <= rem:
            sig_str += "1"
            rem -= dig_val
        else:
            sig_str += "0"
    # build the full binary string and return it
    # Note: the join method of the string class concatenates
    #       multiple strings together with the character at the beginning
    #       (in this case a space " ") placed between the strings
    return " ".join([sgn_str, exp_str, sig_str])
