def main():
    num=input()
    dig=len(num)
    ans=[]
    for i in range(dig-1,-1,-1):
        ans.append(num[i])
        if (dig-i)%3==0 and i!=0:
            ans.append(",")
    print("".join(ans)[::-1])

if __name__ == "__main__":
    main()