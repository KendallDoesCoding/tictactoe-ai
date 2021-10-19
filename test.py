a = [1, 2, 3, 4]


def test():
    if True:
        a[2] = 333
        print(a[2])

test()

print(a[2])