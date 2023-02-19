import sys
from tabulate import tabulate
if len(sys.argv)==2:
    if sys.argv[1][-3:] == "csv":
            try:
                g = []
                h = []
                l = []
                a = sys.argv[1]
                with open(a) as file:
                    for i in file:
                        d = i.rstrip().split(",")
                        g.append(d[0])
                        h.append(d[1])
                        l.append(d[2])

                    table = [
                            [g[1],h[1],l[1]],
                            [g[2],h[2],l[2]],
                            [g[3],h[3],l[3]],
                            [g[4],h[4],l[4]],
                            [g[5],h[5],l[5]],
                            ]
                    headers = [g[0],h[0],l[0]]
                    print(tabulate(table,headers,tablefmt = 'grid'))
            except FileNotFoundError:
                sys.exit("File does not exist")
    elif(sys.argv[1][-3:] != "csv"):
        sys.exit("Not a CSV file")
elif len(sys.argv)>2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv)<2:
    sys.exit("Too few command-line arguments")