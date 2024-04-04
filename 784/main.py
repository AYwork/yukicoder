def main():
    num=input()
    dig=len(num)
    if dig>=4:
        num = num[:-3] + ',' + num[-3:]
    if dig>=7:
        num = num[:-7] + ',' + num[-7:]
    if dig>=10:
        num = num[:-11] + ',' + num[-11:]
    print (num)

if __name__ == "__main__":
    main()