alphabets = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numerics = '123456789'
puncs = '_,.-*/;:"|'


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if (len(s) >= 2 and len(s) <= 6):
        for ele in s:
            if (s[0] in alphabets and s[1] in alphabets):
                if (s[-1] in numerics):
                    if (ele in puncs):
                        return False
                    else:
                        return True
                else:
                    return False
            else:
                return False


main()
