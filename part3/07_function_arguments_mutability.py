def process(s):
    print('initial s # = {0}'.format(hex(id(s))))
    s = s + ' world'
    print('s after change # = {0}'.format(hex(id(s))))


my_var = 'hello'
print('my_var # = {0}'.format(hex(id(my_var))))

process(my_var)
print('my_var # = {0}'.format(hex(id(my_var))))

print('##############################################################################')


def modify_list(items):
    print('initial items # = {0}'.format(hex(id(items))))
    if len(items) > 0:
        items[0] = items[0] ** 2
    items.pop()
    items.append(5)
    print('final items # = {0}'.format(hex(id(items))))


my_list = [2, 3, 4]
print('my_list # = {0}'.format(hex(id(my_list))))

modify_list(my_list)
print(my_list)
print('my_list # = {0}'.format(hex(id(my_list))))

print('##############################################################################')


def modify_tuple(t):
    print('initial t # = {0}'.format(hex(id(t))))
    t[0].append(100)
    print('final t # = {0}'.format(hex(id(t))))


my_tuple = ([1, 2], 'a')

print(hex(id(my_tuple)))

modify_tuple(my_tuple)

print(my_tuple)
