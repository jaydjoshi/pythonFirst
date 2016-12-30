def calculate_age_i_can_date(age):
    age_i_can_date = age / 2 + 7
    return age_i_can_date

print(calculate_age_i_can_date(26))

print("Age", "\t", "Date age")
for i in range(18, 60):
    print(i, "\t", calculate_age_i_can_date(i))


