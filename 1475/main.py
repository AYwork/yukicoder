def main():
    N = int(input())
    for i in range(N):
        L = list(map(int, input().split()))[1:]
        L = sorted(L, reverse=True)
        L = ' '.join(map(str,L))
        print(L)


if __name__ == "__main__":
    main()