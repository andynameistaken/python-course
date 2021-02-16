def something(*args):
    for arg in args:
        print(arg)

lst = ['very', 'simple', 'list']

print(lst)
print(*lst)

i_lst = [1, 2, 3]
print(i_lst)
print(*i_lst)

s = "letters"
print(s)
print(*s)

something(lst)
something(*lst)

print(list(range(3, 6)))            # normal call with separate arguments

args = [3, 6]
print(list(range(*args)))            # call with arguments unpacked from a list

