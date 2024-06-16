# For loop runs till the condition is true

# When i will become 5, the loop will stop so 5 in not printed
for i in range(5):
    print(i)
    
# Output: 0, 1, 2, 3, 4
# By default i starting value is 0

for i in range(5, 10):
    print(i)

# Ouput: 5, 6, 7, 8, 9
# 5 is inclusive and 10 is exclusive so 10 is not printed

# Note: we can't use i outside the loop, it is only available in the loop
