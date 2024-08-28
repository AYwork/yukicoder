def main():
    N = int(input())
    x_list = list(map(int, input().split()))

    count = 0
    while True:
        all_even_number = True
        for i in range(N):
            if x_list[i] % 2 != 0:
                all_even_number = False
                break

        if not all_even_number:
            break

        for i in range(N):
            x_list[i] //= 2
        count += 1

    print(count)



if __name__ == "__main__":
    main()