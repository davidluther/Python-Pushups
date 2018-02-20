# Write function to determine whether one string is a permutation of another


def edges_and_checks(target, test):

    # edge cases and basic tests with no operations
    if len(target) == 0 or len(test) == 0:
        return False
    if target == test:
        return True
    if len(target) != len(test):
        return False
    

def perm_check(target, test):

    # edges cases and basic tests
    edges_and_checks(target, test)

    # sort and test equivalency
    if sorted(test) == sorted(target):
        return True
    else:
        return False


from itertools import permutations 

def perm_check_mult(target, test_list):
    
    # make sure target is not 0 length
    assert len(target) > 0, "target is of zero length"

    # make sure test_list is a list and not empty
    if not isinstance(test_list, list):
        test_list = list(test_list)
    assert len(test_list) > 0, "test_list is empty"

    # make set of target permutations
    target_perms = set()
    for perm_tup in permutations(target):
        target_perms.add(''.join(perm_tup)) 

    results = {}
    for test_str in test_list:
        if test_str in target_perms:
            results[test_str] = True
        else:
            results[test_str] = False

    return results


if __name__ == "__main__":
    while True:
        trg = input("\nTarget string: ")
        # tst = input("Test string: ")
        test_list = input("Test list: ").strip().split()
        print(perm_check_mult(trg, test_list))
