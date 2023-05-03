# 4.7.3 The try-except branch

# try:
# 	# It's a place where
# 	# you can do something
#     # without asking for permission.
# except:
# 	# It's a spot dedicated to
#     # solemnly begging for forgiveness.

try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of', value, 'is', 1/value)
except:
    print('I do not know what to do.')
