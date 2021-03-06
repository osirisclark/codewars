# 8 Drink about

def people_with_age_drink(age):

	return 'drink whisky' if age > 21 else 'drink beer' if age>= 18 else "drink coke" if age>=14 else "drink toddy"



# Test.describe('people_with_age_drink')
# Test.it("should return 'drink toddy' when age is less than 14")
print(people_with_age_drink(13), 'drink toddy', "Wrong result for 13")
print(people_with_age_drink(0), 'drink toddy', "Wrong result for 0")

# Test.it("should return 'drink coke' when age is between 14(inclusive) and 18(exclusive)")
print(people_with_age_drink(17), 'drink coke')
print(people_with_age_drink(15), 'drink coke')
print(people_with_age_drink(14), 'drink coke')

# Test.it("should return 'drink beer' when age is between 18(inclusive) and 21(exclusive)")
print(people_with_age_drink(20), 'drink beer')
print(people_with_age_drink(18), 'drink beer')

# Test.it("should return 'drink whisky' when age is greater than or equal to 21")
print(people_with_age_drink(22), 'drink whisky')
print(people_with_age_drink(21), 'drink whisky')
