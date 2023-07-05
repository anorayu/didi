# print ("hello")
# print("Ali Malikov", "six of january" 1999, 123456, "Samarkand", "Uzbekistan", "street A", "app", 6)
class City:
     def __init__(self, city, district, state, citizens):
           self.city = city
           self.district = district
           self.state = state
           self.citizens = citizens



cityFirst = City("Fergana", "Fergana valley", "Uzbekistan", "25")

print(cityFirst.city, cityFirst.district, cityFirst.state, cityFirst.citizens)

