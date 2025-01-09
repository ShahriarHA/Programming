# a = int(input())
# binaryA = "{0:b}".format(a)
# print(binaryA)
# octalA = "{0:o}".format(a)
# print(octalA)
# hexadecimalA = "{0:X}".format(a)
# print(hexadecimalA)

def print_formatted(number):
    # your code goes here
    for d in range(1,number+1):
        d_padded = "{:>5}".format(d)
        o = "{0:o}".format(d)
        o_padded = "{:>5}".format(o)
        hexA = "{0:X}".format(d)
        hexA_padded = "{:>5}".format(hexA)
        b = "{0:b}".format(d)
        b_padded = "{:>5}".format(b)

        print(f"{d_padded} {o_padded} {hexA_padded} {b_padded}")
        # print(d)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


