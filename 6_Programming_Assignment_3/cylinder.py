# Paul Wade
# PA 3

from math import pi   # need pi for the area & volume calcs below


cylinder_radius = float(input("Enter the radius of the right cylinder: "))
cylinder_height = float(input("Enter the height of the right cylinder: "))


# Calculate surface area
cylinder_surface_area = (2 * pi * cylinder_radius * cylinder_height) + (2 * pi * (cylinder_radius ** 2))

# Calculate volume
cylinder_volume = (pi * (cylinder_radius ** 2) * cylinder_height)


print("\nThe surface area of the right cylinder is: {area:,.4f}".format(area=cylinder_surface_area))
print("The volume of the right cylinder is: {vol:,.4f}".format(vol=cylinder_volume))
