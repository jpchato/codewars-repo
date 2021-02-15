'''
Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.
'''

def maskify(cc):
    cc = '4556364607935616'
    new_str = ''
    if len(cc) > 4:
        for i in range(len(cc)-4):
            new_str += '#'
        new_str += cc[-4] + cc[-3] + cc[-2] + cc[-1]
        print(new_str)
        return new_str
    if len(cc) == 4:
        new_str += cc[-4] + cc[-3] + cc[-2] + cc[-1]
        print(new_str)
        return new_str
    if len(cc) == 3:
        new_str += cc[-3] + cc[-2] + cc[-1]
        print(new_str)
        return new_str
    if len(cc) == 2:
        new_str += cc[-2] + cc[-1]
        print(new_str)
        return new_str
    if len(cc) == 1:
        new_str += cc[-1]
        print(new_str)
        return new_str
    if len(cc) == 0:
        print(new_str)
        return new_str


if __name__ == "__main__":
    maskify('4556364607935616')