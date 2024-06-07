def main():
    Ax,Ay,Az = map(int,input().split())
    Bx,By,Bz = map(int,input().split())

    Cx = (Ay * Bz) - (Az * By)
    Cy = (Az * Bx ) - (Ax * Bz)
    Cz = (Ax * By) - (Ay * Bx)

    print(Cx,Cy,Cz)

 
if __name__ == "__main__":
    main()
