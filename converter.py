weight = int(input ("Weight:"))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "k":
    converted = weight / 0.45
    print("weight is " + str(converted))
else:
    converted = weight * 0.45
    print("weight is " + str(converted))