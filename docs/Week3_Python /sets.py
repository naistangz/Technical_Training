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
normal_set = set(["a", "b", "c"])
print(normal_set)

# Frozen Set
frozen_set = frozenset(["e", "f", "g"])
print(frozen_set)

# This will throw an error. Frozenset objects cannot use the 'add' attribute
# frozen_set.add("h")

