import collections
def main():
    p1 = int(input())
    p2 = int(input())
    n = input()
    rooms = []
    loss = 0
    for i in range(int(n)):
        r.append(input())
    r = collections.Counter(r)
    for j in rooms.values():
        if j>1:
            loss += (p1*(j-1))+(p2*(j-1))
    print(loss)

if __name__ == '__main__':
    main()