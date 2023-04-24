def main(s):
    """
    A variable of type str is given. Check that it consists of letters only.
    Args:
        s: str
    Returns:
        bool: answer
    """
    if s.isdigit() and s.isalpha():
        a="false"
    if s.isalpha() :
        a="true"
    return a
print(main("aabc"))