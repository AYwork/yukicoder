import collections
def main():
    n=int(input())
    a=[input() for _ in range(n)]
    count=collections.Counter(a)
    if count.most_common()[0][1] > (n+1)/2:
        print("NO")
    else:
        print("YES")

if __name__ == "__main__":
    main()