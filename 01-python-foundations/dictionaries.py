print("------ Dictionaries ------")
my_dict = {'key1':'value1','key2':'value2'}
print(my_dict['key1'])

prices_lookup = {'apples':2.99,'oranges':1.99,'milk':5.80}
print("Oranges Price: {}".format(prices_lookup['oranges']))

d = {'k1':123,'k2':['a','b','c'],'k3':{'insideKey':100}}
print(d['k2'])
print(d['k3']['insideKey'])

letter = d['k2'][2].upper()
print(letter)

d = {'k1':100,'k2':200}
d['k3'] = 300
print(d)
d['k1'] ='NEW VALUE' # type:ignore
print(d)

d = {'k1':100,'k2':200,'k3':300}
print(d.keys())
print(d.values())
print(d.items())

print()
print("------ Coding Challenge: Dictionary ------")
# Create a dictionary with days name as strings and their corresponding number in the week as integers
days_of_week = {'Monday':1,'Tuesday':2,'Wednesday':3,'Thursday':4,'Friday':5,'Saturday':6,'Sunday':7}
print(days_of_week)