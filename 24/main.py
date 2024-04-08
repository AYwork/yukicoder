def main():
    turn=int(input())
    ans=set(range(10))
    for i in range(turn):
        *taro,rw=input().split()
        taro=set(map(int,taro))
        if rw == "NO":
            ans -= taro
        else:
            ans &= taro
    print(ans.pop())

if __name__ == "__main__":
    main()