my_var_1 = 'hello'
my_var_2 = my_var_1
print(my_var_1)
print(my_var_2)

print(hex(id(my_var_1)))
print(hex(id(my_var_2)))

my_var_2 = my_var_2 + ' world!'

print(hex(id(my_var_1)))
print(hex(id(my_var_2)))

##############################################################################
print('##############################################################################')

my_list_1 = [1, 2, 3]
my_list_2 = my_list_1
print(my_list_1)
print(my_list_2)

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))

my_list_2.append(4)
print(my_list_2)
print(my_list_1)

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))

print('##############################################################################')

a = 10
b = 10

print(hex(id(a)))
print(hex(id(b)))

b = 15

print(hex(id(a)))
print(hex(id(b)))


my_list_1 = [1, 2, 3]
my_list_2 = [1, 2, 3]

print(hex(id(my_list_1)))
print(hex(id(my_list_2)))
