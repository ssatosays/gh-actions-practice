"""System module."""
def main():
    """main dayo"""
    a_dayo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b_dayo = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in a_dayo:
        print(str([i * j for j in b_dayo]))


if __name__ == "__main__":
    main()
