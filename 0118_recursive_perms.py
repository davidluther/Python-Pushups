# recursive function to return all the permutations of a string, does not
# initially account for duplicates


def perms_with_dupes(str_in):
    """Returns a list of permutations for an input string"""

    # base cases
    if len(str_in) == 1:
        return [str_in]
    if len(str_in) == 2:
        return [str_in, str_in[::-1]]
    # recursion
    else:
        plist = []
        for ix, char in enumerate(str_in):
            if ix == len(str_in)-1:
                not_char = str_in[:-1]
            else:
                not_char = str_in[:ix] + str_in[ix+1:]
            for perm in perms_with_dupes(not_char):
                plist.append(char + perm)
        return plist


def perms_no_dupes(str_in):
    """Returns a list of permutations for an input string, removes dupes"""

    # base cases
    if len(str_in) == 1:
        return [str_in]
    elif len(str_in) == 2:
        if str_in[0] == str_in[1]:
            return [str_in]
        else:
            return [str_in, str_in[::-1]]
    # recursion
    else:
        plist = []
        chars = set()
        for ix, char in enumerate(str_in):
            if char in chars:
                continue
            elif ix == len(str_in)-1:
                not_char = str_in[:-1]
            else:
                not_char = str_in[:ix] + str_in[ix+1:]
            for perm in perms_no_dupes(not_char):
                plist.append(char + perm)
            chars.add(char)
        return plist


def permutations(str_in, remove_dupes=True):
    """Returns a list of permutations for an input string, removes duplicates
    if indicated"""

    # base cases
    if len(str_in) == 1:
        return [str_in]
    elif len(str_in) == 2:
        if str_in[0] == str_in[1] and remove_dupes:
            return [str_in]
        else:
            return [str_in, str_in[::-1]]
    # recursion
    else:
        plist = []
        if remove_dupes:
            chars = set()
        for ix, char in enumerate(str_in):
            if remove_dupes:
                if char in chars:
                    continue
                else:
                    chars.add(char)
            if ix == len(str_in)-1:
                not_char = str_in[:-1]
            else:
                not_char = str_in[:ix] + str_in[ix+1:]
            for perm in permutations(not_char, remove_dupes=remove_dupes):
                plist.append(char + perm)
        return plist


if __name__ == "__main__":
    while True:
        str_in = input("\nA string: ")
        if input("Remove duplicates? (y/n): ").lower() == 'y':
            rm_dupes = True
        else:
            rm_dupes = False

        perms = permutations(str_in, remove_dupes=rm_dupes)
        print(perms)
        print("Number of permutations:", len(perms))
