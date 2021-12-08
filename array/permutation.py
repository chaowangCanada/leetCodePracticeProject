def toString(List):
    return ''.join(List)


#
# def swap(string, l, r):
#     temp = string[l]
#     string[l] = string[r]
#     string[r] = temp


def permute(string, l, r):
    if l == r:
        print(toString(string))
    else:
        for i in range(l, r + 1):
            string[l], string[i] = string[i], string[l]
            permute(string, l + 1, r)
            string[l], string[i] = string[i], string[l]


def permute_wapper(string):
    r = len(string)
    permute(list(string), 0, r - 1)


string = "ABC"
permute_wapper(string)
