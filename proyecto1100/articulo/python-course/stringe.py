myStr = "hello,world"

#print(dir(myStr))

#print (myStr.upper())
print (myStr.lower())
print (myStr.swapcase())
print (myStr.capitalize())

print (myStr.replace('hello','bye'))
print (myStr.count("o"))
print (myStr.startswith("wolrd"))
print (myStr.endswith("world"))

print (myStr.split())
print (myStr.split(","))

print (myStr.find('o'))
print(len(myStr))
print (myStr.index("e"))

print(myStr.isnumeric())
print(myStr.isalpha())

print(myStr[4])
print (myStr[1])

print("My name is" + myStr)
print (f"my name is {myStr}")
print( "my name is (0)".format(myStr))