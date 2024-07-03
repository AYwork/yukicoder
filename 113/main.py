import math
def main():
    input_string = input()

    ans = 101

    for i in range(len(input_string)-2):
        for j in range(i+2,len(input_string)):
            if input_string[i] == 'c' and S[j] == 'w' and input_string[i:j+1].count('w') == 2:
                ans = min(ans, j-i+1)
            else:
                continue

    print(ans if ans != 101 else -1)


if __name__ == "__main__":
    main()