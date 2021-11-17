def make_divison_by(n):
    return lambda x: x//n


def run():
    make_divison_by_3 = make_divison_by(3)
    print(make_divison_by_3(18)) # Expected output: 6

    make_divison_by_5 = make_divison_by(5)
    print(make_divison_by_5(100)) # Expected output: 20

    make_divison_by_18 = make_divison_by(18)
    print(make_divison_by_18(54)) # Expected output: 3


if __name__ == '__main__':
    run()