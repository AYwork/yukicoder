def main():
    m = int(input())
    n = m*m
    a = [[0 for i in range(m)] for j in range(m)]
    num = 1
    x = 0
    y = 0
    slide = m
    updown = m

    while True:
        for i in range(slide):
            a[x][y] = num
            y += 1
            num += 1
        updown -= 1
        y -= 1
        x += 1

        for i in range(updown):
            a[x][y] = num
            x += 1
            num += 1
        slide -= 1
        x -= 1
        y -= 1

        for i in range(slide):
            a[x][y] = num
            y -= 1
            num += 1
        updown -= 1
        y += 1
        x -= 1

        for i in range(updown):
            a[x][y] = num
            x -= 1
            num += 1
        slide -= 1
        x += 1
        y += 1
        if num == n+1:
            break
 
    for i in range(m):
        for j in range(m):
            if len(str(a[i][j])) == 1:
                a[i][j] = "00" + str(a[i][j]) 
            elif len(str(a[i][j])) == 2:
                a[i][j] = "0" + str(a[i][j])

    for i in range(m):
        for j in range(m):
            if j == m-1:
                print(a[i][j])
            else:
                print(a[i][j], end=' ')

if __name__ == "__main__":
    main()