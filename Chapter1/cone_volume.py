def cone_volume(r, h):
    """
    Calculate the volume of a cone.
    -Parameters:
    r (int or float): Radius of the cone (1–100)
    h (int or float): Height of the cone (1–100)

    -Formula:
    volume = pi * r**2 * (h / 3), where pi = 3.14

    -Returns:
    float: Volume of the cone if inputs are valid.
    str: "INVALID INPUTS!" if radius or height is out of range.
    """
    pi = 3.14
    if not (1 <= r <= 100) or not (1 <= h <= 100):
        return "INVALID INPUTS!"
    else:
        result = pi * (r ** 2) * (h / 3)
        return result

r = int(input("Enter the radius: "))
h = int(input("Enter the height: "))
print(cone_volume(r, h))
