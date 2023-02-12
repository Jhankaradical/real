demo_list = [1, 'hello',1.34, True, [1,2,3]]
colors = ['red,green,blue']

#numbers_list = list((1,2,3,4,5))
#print(type(numbers_list))

#r = list(range(1,112))
#print(r)

#print(dir(colors))
#print(len(demo_list))
#print(colors[-2])

#print (colors)
#colors [1]= 'yellow'
#print(colors)

#colors.append ('violet')
#colors.extend (['yellow','violet'])
#colors.extend (['pink','yellow,''orange'])

colors.insert(1,'violet')
colors.insert(len(colors),'violet')

print(colors)

colors.pop()
colors.remove('green')
colors.clear()
print(colors)




