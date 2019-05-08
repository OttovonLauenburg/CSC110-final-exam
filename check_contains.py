def check_contains(my_list,check_one):
    for element in my_list:
        element = element.strip('\'')
        if element == check_one:
            return True
    return False


check = input('Please enter the string you want to check:\n')
user_list = input('PLease enter your list:\n').split(',')
result = check_contains(user_list,check)
print(result)