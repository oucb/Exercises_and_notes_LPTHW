__author__ = 'oucb'
ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there's not 10 things in that list, let's fix that."

# the syntax for split() method:string.split(str=' ', num=string.count(str))
# split the string and return a list of the words in the string
# using str as the delimiter string and num is the times to split
stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Friasbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    # delete a element of the list (the last as the default) and return the value of it's
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's go some things with stuff."

print stuff[1]
print stuff[-1] # whoa! fancy
print stuff.pop()
# join the string elements of sequence by str seprator
# the syntax for join() method:str.join(sequence)
print ' '.join(stuff) #what? cool!
print '#'.join(stuff[3:5]) #super stellar!