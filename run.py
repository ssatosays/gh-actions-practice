""" run.py
"""
def main():
    """ main
    """
    a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in a_list:
        print(str([i * j for j in b_list]))


if __name__ == "__main__":
    main()
