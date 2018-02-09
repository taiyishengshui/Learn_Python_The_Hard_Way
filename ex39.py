# part1
# things = ['a', 'b', 'c', 'd']
# print(things[1])
# things[1] = 'z'
# print(things[1])
# print(things)


# part2
# stuff = {'name':'Zed', 'age':39, 'height':6 * 12 + 2}
# print(stuff['name'])#要用[]，不要用()
# print(stuff['age'])#要用[]，不要用()
# print(stuff['height'])#要用[]，不要用()
# stuff['city'] = 'SF'  #要用[]，不要用()
# print(stuff['city'])
# stuff[1] = "Wow"
# stuff[2] = "Neato"
# print(stuff[1])
# print(stuff[2])
# print(stuff)
# del stuff['city']
# del stuff[1]
# del stuff[2]
# print(stuff)


#part3
#create a mapping of state to appreviation
states = {
    'Oregon':'OR',
    'Florida':'FL',
    'California': 'CA',
    'New Youk': 'NY',
    'Michigan': 'MI'
}

#create a basic set of states and some cities in them
cities = {
    "CA":"San Francisco",
    "MI":"Detroit",
    "FL":"Jacksonville"
}

#add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#print out some cities
print(cities)
print('-' * 10)
print("NY State has: ",cities['NY'])
print("OR stete has: ",cities['OR'])

#print out some states
print(states)
print('-' * 10)
print("Michigan's abbreviation is ",states['Michigan'])
print("Florida's abbreviation is ",states['Florida'])

#do it by using the state the cities dict
print('-' * 10)
print("Michigan has: ", cities[states['Michigan']])
print("Florida has:", cities[states['Florida']])


#print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} has the city {abbrev}")

#print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
#safely get a abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")
#get a city with a default value
city = cities.get('TX','Does Not Exist')
print(f"The city for the state 'TX' is : {city} ")