# Lists

my_list = [1,2,3]

my_list = ['STRING',100,2.3]
print(len(my_list))

# Indexing and Slicing
my_list = ['one','two','three',4,5]
print(my_list[0])
print(my_list[1:])

# List Concatenation
my_list = ['one','two','three']
another_list = ['four','five','six']
new_list=my_list + another_list
print(new_list)

# List operations

# Append - Add element to end of list
new_list.append('seven')
print(new_list)

new_list.append('eight')
print(new_list)

# Pop - Remove last element of list and return it
popped_item = new_list.pop()
print("Popped Item:", popped_item)
print(new_list)

# Pop specific index
popped_index_item = new_list.pop(2) 
print("Popped Index Item:", popped_index_item)
print(new_list)

# Sort & Reverse
new_list = ['a','e','x','b','c']
num_list = [4,1,8,3]

new_list.sort()
my_sorted_list = new_list
print(my_sorted_list)
new_list.sort(reverse=True)
rev_list = new_list
print("Rev List: ", rev_list)

num_list.reverse()
print("Reversed List: ", num_list)

print()
print("----- Coding Challenge: Lists -----")
print("['apple',100,35.46]")