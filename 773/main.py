def main():
    a, b = map(int, input().split())
    ans=3
    for c in range(23,26):
        if a>=c>=b:
            ans-=1
    print(str(ans)+"日")


if __name__ == "__main__":
    main()