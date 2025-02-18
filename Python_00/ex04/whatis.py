import sys

args_len = len(sys.argv)

if args_len == 1:
    print("No arguments")
    sys.exit(1)
elif args_len > 2:
    print("Too many arguments")
    sys.exit(1)

try:
    sys.argv[1] = int(sys.argv[1])

except ValueError:
    print("Argument is not an integer")
    sys.exit(1)

if (int(sys.argv[1]) % 2) == 0:
    print("I'm Even")
else:
    print("I'm Odd")
sys.exit(0)
