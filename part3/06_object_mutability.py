my_list = [1, 2, 3]
print(my_list)
print(hex(id(my_list)))

my_list.append(4)
print(my_list)
print(hex(id(my_list)))

#
my_list_1 = [1, 2, 3]
print(my_list_1)
print(hex(id(my_list_1)))

my_list_1 = my_list_1 + [4]
print(my_list_1)
print(hex(id(my_list_1)))
# burda farklı cunku iki listeyi birlestirip yeni bir liste olusturuyor

# dictionaryde de aynı
my_dict = dict(key1='value 1')
print(my_dict)
print(hex(id(my_dict)))

my_dict['key1'] = 'modified value 1'
print(my_dict)
print(hex(id(my_dict)))

my_dict['key2'] = 'value 2'
print(my_dict)
print(hex(id(my_dict)))

# tuple degismez

t = (1, 2, 3)
print(hex(id(t)))
a = [1, 2]
b = [3, 4]
t = (a, b)
print(t)
print(hex(id(t)))
a.append(3)
b.append(5)
print(t)
print(hex(id(t)))

print(id(t))
print(t[0])
print(t[1])
t[0].append(3)
print(t)
