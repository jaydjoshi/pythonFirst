def calculate_health(age, apples_ate , cig_smoked):
    print((100-age) + (apples_ate*3) - (cig_smoked*4))

jay_data = [27, 1, 0]
calculate_health(jay_data[0], jay_data[1], jay_data[2])
calculate_health(*jay_data)
