class Circle:

    __pi = 3.14

    def __init__(self, diameter):
        self.diameter = diameter
        self.radius = diameter / 2

    def calculate_circumference(self):
        result = 2 * Circle.__pi * self.radius
        return result

    def calculate_area(self):
        result = Circle.__pi * self.radius ** 2
        return result

    def calculate_area_of_sector(self, angle):
        result = (Circle.__pi * self.radius ** 2) * (angle / 360)
        return result


circle = Circle(10)
current_angle = 5

print(f"{circle.calculate_circumference():.2f}")
print(f"{circle.calculate_area():.2f}")
print(f"{circle.calculate_area_of_sector(current_angle):.2f}")
