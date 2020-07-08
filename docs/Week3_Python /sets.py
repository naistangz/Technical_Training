# An unordered collection data type that is iterable, mutable and has no duplicate elements
# They are very similar to lists but it has a highly optimised method for checking whether a specific element is contained in the set.
# This is based on a data structure known as a has table

car_parts = {"wheels", "windows", "doors"}
print(car_parts)

# Adding an item to a set
car_parts.add("breaks")
print(car_parts)

# Deleting an item in a set
car_parts.discard("windows")
print(car_parts)

# Frozen Set
# Frozen sets are immutable objects that only support methods and operators that produce a result without affecting the frozen set or sets to which they are applied.
# Elements of a set can be modified at any time, elements of the frozen set remain the same after creation

# Normal Set
# Prints b, c, a or c, a, b
normal_set = set(["a", "b", "c"])
normal_set.add("d")
print(normal_set)

# Frozen Set
# Prints f, e, g
frozen_set = frozenset(["e", "f", "g"])
print(frozen_set)

# This will throw an error. Frozenset objects cannot use the 'add' attribute
# frozen_set.add("h")


# Example 2
# initialize my_set
my_set = {1, 3}
print(my_set)

# if you uncomment line 9,
# you will get an error
# TypeError: 'set' object does not support indexing

# my_set[0]

# add an element
# Output: {1, 2, 3}
my_set.add(2)
print(my_set)

# add multiple elements
# Output: {1, 2, 3, 4}
my_set.update([2, 3, 4])
print(my_set)

# add list and set
# Output: {1, 2, 3, 4, 5, 6, 8}
my_set.update([4, 5], {1, 6, 8})
print(my_set)

# Removing vs discard
# Discard function leaves a set unchanged if element not present in set
# Remove function raises error if element not present in the set

# Difference between discard() and remove()

# initialize my_set
my_set = {1, 3, 4, 5, 6}
print(my_set)

# discard an element
# Output: {1, 3, 5, 6}
my_set.discard(4)
print(my_set)

# remove an element
# Output: {1, 3, 5}
my_set.remove(6)
print(my_set)

# discard an element
# not present in my_set
# Output: {1, 3, 5}
my_set.discard(2)
print(my_set)

# remove an element
# not present in my_set
# you will get an error.
# Output: KeyError

my_set.remove(2)