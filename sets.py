def remove_duplicates(some_list):
#*   This is a set:
    return list(set(some_list))
#*   this is the same as that set but with for
    # without_duplicates = []
    # for element in some_list:
    #     if element not in without_duplicates:
    #         without_duplicates.append(element)
    # return without_duplicates

def run():
    random_list = [ 11, 55, 2, 2, 55]
    print(remove_duplicates(random_list))


if __name__ == '__main__':
    run()