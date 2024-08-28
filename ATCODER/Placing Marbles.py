def main():
    input_value = int(input())
    A = list(map(int, input().split()))
    count = 0
    for a in A:
        if a == 1:
            count += 1
    print(count)


if __name__ == "__main__":
    main()