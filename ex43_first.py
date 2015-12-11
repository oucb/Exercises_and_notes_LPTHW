__author__ = 'oucb'
class first(object):


    def first_pit(self):

        action = raw_input("> ")

        if action == 'second pit':
            print "Very good!Now,you are at the second pit."
            print "Continuing to let the pinball to third pit"
            return ['second_pit', 'second']
        elif action == 'fifth pit':
            print "Please trying to let the pinball to second pit again! "
            print "You will use one more step than others."
            return ['first_pit', 'first']
        else:
            return ['death', 'death']

