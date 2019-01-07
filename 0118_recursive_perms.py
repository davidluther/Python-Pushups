# recursive function to return all the permutations of a string, does not
# initially account for duplicates


def perms_with_dupes(collection):
    """Returns a list of permutations for an input string"""

    # base cases
    if len(collection) == 1:
        return [collection]
    if len(collection) == 2:
        return [collection, collection[::-1]]
    # recursion
    else:
        perms = []
        for ix, item in enumerate(collection):
            if ix == len(collection)-1:
                excl_items = collection[:-1]
            else:
                excl_items = collection[:ix] + collection[ix+1:]
            print("Item", item)
            print("Excl_items", excl_items)
            for perm in perms_with_dupes(excl_items):
                if isinstance(collection, list) and not isinstance(item, list):
                    item = [item]
                # print("Item:", item)
                # print("Perm:", perm)
                perms.append(item + perm)
        return perms


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
        perms = []
        chars = set()
        for ix, char in enumerate(str_in):
            if char in chars:
                continue
            elif ix == len(str_in)-1:
                not_char = str_in[:-1]
            else:
                not_char = str_in[:ix] + str_in[ix+1:]
            for perm in perms_no_dupes(not_char):
                perms.append(char + perm)
            chars.add(char)
        return perms


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
        perms = []
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
                perms.append(char + perm)
        return perms


def permutations_plus(collection, k=None):
    """
    Returns list of all k-length permutations from collection.
    """
    if not isinstance(collection, list):
        collection = list(collection)
    if k is None:
        k = len(collection)

    if k == 1:
        return [[item] for item in collection]
    else:
        perms = []
        for ix, item in enumerate(collection):
            if ix == len(collection)-1:
                excl_items = collection[:-1]
            else:
                excl_items = collection[:ix] + collection[ix+1:]
            for perm in permutations_plus(excl_items, k-1):
                perms.append([item] + perm)
        return perms


if __name__ == "__main__":
    while True:
        choice = input("\nString (s) or list (l): ")
        user_in = input("Enter pattern: ")
        if choice.lower() == 'l':
            user_in = user_in.split()

        user_k = input("Value of k (int): ")
        if user_k == '':
            user_k = None
        else:
            user_k = int(user_k)

        # if input("Remove duplicates? (y/n): ").lower() == 'y':
        #     rm_dupes = True
        # else:
        #     rm_dupes = False
        # perm_results = permutations(user_in, remove_dupes=rm_dupes)
        perm_results = permutations_plus(user_in, user_k)
        print(sorted(perm_results))
        print("Number of permutations:", len(perm_results))
