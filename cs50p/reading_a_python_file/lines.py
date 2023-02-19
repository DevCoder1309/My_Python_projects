import sys
d = 0
b = []
if len(sys.argv) == 2:
    if sys.argv[1][-2:] == "py":
        try:
            a = sys.argv[1]
            with open(a, "r") as file:
                for i in file:
                    if not i.isspace():
                        b.append(i)
                for j in b:
                    v = ''.join(j)
                    if '#' in v:
                        c = v.find('#')
                        z = v.replace(v[c:], '')
                        print(z)
                    else:
                        d = d + 1
            print(d)
        except (FileNotFoundError):
            sys.exit("File does not exist")
    elif sys.argv[1][-2:] != "py":
        sys.exit("Not a python file")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
else:
    sys.exit("Too few command-line arguments")
