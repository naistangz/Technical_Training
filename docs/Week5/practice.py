import math

def get_drink_by_profession(p):
    if p.capitalize() == "Jabroni":
        print("Patron Tequila")
    elif p.capitalize() == "School Counselor":
        print("Anything with Alcohol")
    elif p.capitalize() =="Programmer":
        print("Hipster Craft Beer")
    elif p.capitalize() == "Bike Gang member":
        print("Moonshine")
    elif p.capitalize() == "Politician":
        print("Your tax dollars")
    elif p.capitalize() == "Rapper":
        print("Cristal")
    else:
        print("Beer")

get_drink_by_profession("scHOOl counselor")
get_drink_by_profession("pundit")
get_drink_by_profession("jabrOni")
get_drink_by_profession("poLiTiCian")




def duty_free(price, discount, holiday_cost):
    saving = (holiday_cost/(price*discount)*100)
    return math.floor(saving)

print(duty_free(12, 50, 1000)) # 166


def first_non_consecutive(arr):
    prev = arr[0]
    count = None
    # for every number in array
    for num in arr[1::]:
        # if previous integer is not equal to the num
        if prev + 1 != num:
            count = num
            break
        prev += 1
        return count

print(first_non_consecutive([1,2,3,4,6,6,7,8]))
print(first_non_consecutive([31,32]))

def name_to_initials(name):
    first_initial = name[0].upper()
    second_initial = name[1].upper()
    abbreviated = f"{first_initial}.{second_initial}"
    return abbreviated

def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

def is_index_even(arr, i):
    is_even = arr[i]
    if is_even % 2 == 0:
        return True
    else:
        return False

print(is_index_even([1, 2, 3, 5, 5, 6],3)) # 5 False
print(is_index_even([1, 2, 3, 5, 5, 6],5)) # 6 True