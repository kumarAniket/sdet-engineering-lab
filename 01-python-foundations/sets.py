print("--------- Sets -------------")
myset = set()
myset.add(1)
myset.add(2)
print(myset)


my_list = [1,1,1,1,1,1,2,2,2,2,2,3,4,3,3,3,3,3]
my_set = set(my_list)
print("Set before list conversion: {}".format(my_set))
new_list = list(set(my_list))
print("Set converted to list: {}".format(new_list))

print()
print("Coding Challenge: Turn 'Mississippi' into a set of unique characters")
print(set('Mississippi'))