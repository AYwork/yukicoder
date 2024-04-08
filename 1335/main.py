def main():
    a = input()
    s = input()
    t = []
    for x in s:
        try:
            x=int(x)
            t.append(a[x])
        except:
            t.append(x)
    t = "".join(t) 
    print(t)

if __name__ == "__main__":
    main()