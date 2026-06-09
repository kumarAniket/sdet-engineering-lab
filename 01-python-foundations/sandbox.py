# =====================================================================
# DIAGNOSTIC 1: List/Dict Comprehensions & Data Filtering
# Task: Take the raw input list and use a single-line comprehension
# to create a dictionary where the key is the string and the value
# is its length, but ONLY for strings that contain the letter 'e'.
# =====================================================================
raw_input = ["apple", "banana", "cherry", "date", "elderberry", "fig"]

my_dict = {index: len(index) for index in raw_input if 'e' in index}
print(my_dict)

# =====================================================================
# DIAGNOSTIC 2: Object-Oriented Foundations & Inheritance
# Task: Create a base class 'Component' with an __init__ method that
# sets self.name. Create a subclass 'Service' that inherits from
# Component, accepts both 'name' and 'port', uses super() to initialize
# the name, and has a __str__ method returning "Service: <name> on port <port>".
# =====================================================================

# Your code here:
class Component:
    def __init__(self,name):
        self.name = name

class Service(Component):
    def __init__(self, name, port):
        super().__init__(name)
        self.port = port

    def __str__(self):
        return f"Service: {self.name} on port {self.port}"

service = Service("Jenkins Server",4403)
print(service)

# =====================================================================
# DIAGNOSTIC 3: Algorithmic Logic (Two-Pointer Mechanics)
# Task: Given a sorted list of integers, write a quick function to
# find if there are two numbers that log a sum equal to a target.
# Return the indices of those two numbers. Optimize for O(N) time.
# =====================================================================
nums = [2, 7, 11, 15]
target = 9

def find_two_sum_sorted(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        current_sum=nums[left]+nums[right]

        if current_sum==target:
            return [left,right]
        elif current_sum < target:
            left+=1
        else:
            right-=1
    return None

value_index = find_two_sum_sorted(nums,target)
print(value_index)