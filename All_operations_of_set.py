### Create a new set
# Empty
my_set = set()
print(my_set)
# Non empty
my_set = {1,2,3}
print(my_set)

### Add and remove elements
# Add single item
my_set.add(5)
print(my_set)
# Add mutiple items
my_set.update([7,8,9])
print(my_set)
# Remove item which does not exist with an error.
my_set.remove(9)
print(my_set)
# Remove item which does not exist without an error.
my_set.discard(9)
print(my_set)
# Remove a random element in the set
x = my_set.pop()
print(x)
print(my_set)

### Access the set
# Get the length
length = len(my_set)
print(length)
# Check whether something in the set or not
print(7 in my_set)
# Get all the elements in the set
for element in my_set:
    print(element)

### Make other data structures into set
my_list = [1,2,3,4,5]
print(set(my_list))

### The operations between two sets
# combine two sets
total_set = my_set.union(my_list)
print(total_set)
# Get the intersection of two sets
intersection_set = my_set.intersection(my_list)
print(intersection_set)
# Get the difference between two sets
difference_set = my_set.difference(my_list)
print(difference_set)
s_d_set = my_set.symmetric_difference(my_list)
print(s_d_set)
# Check whether another set contains this set or not
print(my_set.issubset(total_set))
# Check whether this set contains another set or not
print(total_set.issuperset(my_set))
# Check whether two sets have a intersection or not
print(my_set.isdisjoint(total_set))