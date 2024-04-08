import collections
def main():
    P1=int(input())
    P2=int(input())
    N=input()
    r=[]
    loss=0
    for i in range(int(N)):
        r.append(input())
    r=collections.Counter(r)
    for j in r.values():
        if j>1:
            loss+=(P1*(j-1))+(P2*(j-1))
    print(loss)#損失

if __name__ == '__main__':
    main()