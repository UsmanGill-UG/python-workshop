first_name = 'Usman'
last_name = 'Gill'

# This will concatenate the two strings and store it in full_name
full_name = first_name + ' ' + last_name 
print(full_name) # Usman Gill

# We can't concatenate string with int
age = 23
usman_name_and_age = full_name + ' ' + age
# This will give us error as one is string and one is int
# In console we see following error
# TypeError: can only concatenate str (not "int") to str

# instead we can type-caste 23 to string
usman_name_and_age = full_name + ' ' + str(age) # This will work fine
print(usman_name_and_age) # Usman Gill 23

# We can also type caste a valid number string to int
age = '23'
age = int(age) # This will change '23' to 23

any_word = 'mango'
mango = int(any_word) # This will give us error as mango is not a valid number
# ValueError: invalid literal for int() with base 10: 'mango'

# but we can mutiply a string with a int
fruit = 'mango'
print(fruit*3) # mangomangomango