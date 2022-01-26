
def main():
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in a:
        print(str([i * j for j in b]))


if __name__ == "__main__":
    main()

