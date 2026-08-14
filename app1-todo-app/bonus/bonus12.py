feet_inches = input("Enter feet and inches: ")



def convert(feet_inches):
    parts = feet_inches.split(' ')
    feet = float(parts[0])
    inch = float(parts[1])

    meters = feet * 0.3048 + inch * 0.0254
    return meters

print(convert(feet_inches))


