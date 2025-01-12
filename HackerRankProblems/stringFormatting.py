# a = int(input())
# binaryA = "{0:b}".format(a)
# print(binaryA)
# octalA = "{0:o}".format(a)
# print(octalA)
# hexadecimalA = "{0:X}".format(a)
# print(hexadecimalA)

def print_formatted(number):
    # your code goes here
    width = len("{0:b}".format(number))
    for d in range(1,number+1):
        o = "{0:o}".format(d)
        hexA = "{0:X}".format(d)
        b = "{0:b}".format(d)
        d_padded = "{:>{w}}".format(d,w=width)
        o_padded = "{:>{w}}".format(o,w = width)
        hexA_padded = "{:>{w}}".format(hexA,w=width)
        b_padded = "{:>{w}}".format(b,w=width)
        print(f"{d_padded} {o_padded} {hexA_padded} {b_padded}")
        # print(d)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


