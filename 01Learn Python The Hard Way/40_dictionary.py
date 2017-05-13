# create a mapping of state to abbreviation
states={
				'Oregeon':'OR',
				'Florida':'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY']='New York'
cities['OR']='Portland'

print '-'*10
print "NY state has: ", cities['NY']
print "MI state has: ", cities['MI']

# print some states
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

print '-'*10
for state,abbrev in states.items():
 print "%s is abbreviated %s" %(state,abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

print '-' * 10
state=states.get('Texas',None)
print 'state=',state

if not state:
 print "sorry ,no Texas"

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print "city=",city
print "The city for the state 'TX' is: %s" % city

print '-^-' * 10
aList=[1,2,3,4,5,6,7,8,9]
print aList
low=3
high=7

print filter(lambda x,l=low,h=high: h>x>l,aList)

#another way
def within_bounds(value,l=low,h=high):
 return h>value>l 
print filter(within_bounds,aList)

# since dictionary can't be sorted ,we use following:
def sortedDictValue(adict):
 items=adict.items()
 items.sort()
 return [ value for key,value in items]

print states
print sortedDictValue(states)

def sortedDictKeys(adict):
 items=adict.keys()
 items.sort()
 return items

print sortedDictKeys(states)
print states
print sorted(states)
print 'new=',states
print sorted(states, key=lambda student: states[student])  



