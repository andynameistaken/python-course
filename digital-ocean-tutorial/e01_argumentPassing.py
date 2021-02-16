import sys

args_len = len(sys.argv)
print("Number of arguments: ",  args_len)

for i in range(args_len):
    if i == 0:
        print('first arg is file name')
        print()
    print(sys.argv[i])
