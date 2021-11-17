def remove_duplicates(some_list):
    return list(set(some_list))
    # without_duplicates = []
    # for element in some_list:
    #     if element not in without_duplicates:
    #         without_duplicates.append(element)
    # return without_duplicates

def run():
    some_list = [ 11, 55, 2, 2, 55]
    print(remove_duplicates(some_list))


if __name__ == '__main__':
    run()