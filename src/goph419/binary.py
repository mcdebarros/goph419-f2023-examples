def binary_converter(value):
    """Convert an integer into a binary string.

    Inputs
    ------
    value : int
        The integer to convert

    Returns
    -------
    str
        A string with a binary representation of the input
    """
    value = int(value)
    sign = "0 "
    if value < 0:
        sign = "1 "
    rem = abs(value)
    for b in range(30, -1, -1):
        if (dig_val := 2 ** b) <= rem:
            sign += "1"
            rem -= dig_val
        else:
            sign += "0"
    return sign
