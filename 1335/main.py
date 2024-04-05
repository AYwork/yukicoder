def main():
    A = input()
    S = input()
    T = []
    for x in S:
        if x == "0":
            T.append(A[0])
        elif x == "1":
            T.append(A[1])
        elif x == "2":
            T.append(A[2]) 
        elif x == "3":
            T.append(A[3]) 
        elif x == "4":
            T.append(A[4]) 
        elif x == "5":
            T.append(A[5])  
        elif x == "6":
            T.append(A[6])  
        elif x == "7":
            T.append(A[7])      
        elif x == "8":
            T.append(A[8])      
        elif x == "9":
            T.append(A[9])
        else:
            T.append(x)
    T = "".join(T) 
    print(T)

if __name__ == "__main__":
    main()