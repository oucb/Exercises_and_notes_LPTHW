__author__ = 'oucb'
def while_number(number,cal):
    i = 0
    numbers = []

    while i < number:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + cal
        print "Numbers now: ", numbers
        print "At the bottom i is %d" % i

    print "The numbers: "

    for num in numbers:
        print num

while_number(4,2)