
# If conditions

Weight = int(input("Weight:"))
unit= input("(K)g or (L)bs:")
if unit.upper() == "K":
    converted = Weight / 0.45
    # print("Weight in Lbs:" + str(converted))
    print(f"Weight in lbs:{converted}")
else:
    converted = Weight * 0.45
    print("Weight in Kg:" + str(converted))

