import math
def main():
    A = str(input())
    E = A.count('E')
    W = A.count('W')
    N = A.count('N')
    S = A.count('S')

    print(math.sqrt(pow((abs(E - W)),2)+pow((abs(N - S)),2)))


if __name__ == "__main__":
    main()