def get_gender(sex='Unknown'):
    if sex is 'M':
        sex = 'Male'
    elif sex is 'F':
        sex = 'Female'
    return sex

print(get_gender('M'))
print(get_gender('F'))
print(get_gender())
