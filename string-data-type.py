myString= "This is a string"
print(type(myString))
print(myString + "is of the data type " + str(type(myString)))


firstString = "water"
secondString = "fall"
thirdString= firstString + secondString
print(thirdString)

name= input("Cual es tu nombre?")
print(name)

color= input("Cual es tu color favorito?")
animal= input("Cual es tu animal favorito?")

print("{}, te gusta un {} {}!".format(name,animal,color))
