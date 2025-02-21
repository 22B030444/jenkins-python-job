import sys

if len(sys.argv) < 2:
    print("Usage: python print_names.py <name1> <name2> ...")
else:
    for name in sys.argv[1:]:
        print(name)
