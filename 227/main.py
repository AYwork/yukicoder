import collections
def main():
    count=collections.Counter(map(int,input().split()))
    num=list(count.values())
    if 3 in num and 2 in num:
        print("FULL HOUSE")
    elif 3 in num:
        print("THREE CARD")
    elif num.count(2) == 2:
        print("TWO PAIR")
    elif 2 in num:
        print("ONE PAIR")
    else:
        print("NO HAND")

if __name__ == "__main__":
    main()