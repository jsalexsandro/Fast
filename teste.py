import sys

a =  "\\".join([i for i in sys.argv[0].split("\\")[0:-1]])+"\\run"

print(a)