# compute Levenstein distance between two strings

def lev(str1, str2):
    
    # check edges here

    # base cases
    if str1 == str2:
        return 0
    elif str1 == "":
        return len(str2)
    elif str2 == "":
        return len(str1)

    # recursive, with four different cases to check & return min
    else:
        a = lev(str1[1:], str2[1:])
        if str1[0] != str2[0]:
            a += 1
        b = lev(str1[1:], str2[:-1]) + 2
        c = lev(str1[:-1], str2[1:]) + 2
        d = lev(str1[:-1], str2[:-1])
        if str1[-1] != str2[-1]:
            d += 1
        return min(a, b, c, d)


if __name__ == "__main__":

    while True:
        str1 = input("\nFirst string: ")
        str2 = input("Second string: ")
        print(lev(str1, str2))
