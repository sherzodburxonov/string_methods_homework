def main(s):
    """
    A variable of type str is given. Check that it consists only of numbers.
    Args:
        s: str
    Returns:
        bool: answer
    """
    if s.isdigit() and s.isalpha():
        a="false"
    else :
        a="true"
    return a
print(main("123"))