my_var = 10
print(hex(id(my_var)))

my_var = 16
print(hex(id(my_var)))

my_var = my_var + 1
print(hex(id(my_var)))

my_var = 9
print(hex(id(my_var)))
# degerler aynı olunca ref aynı oluyor adresler
my_var_2 = 9
print(hex(id(my_var_2)))
