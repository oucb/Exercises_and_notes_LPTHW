__author__ = 'oucb'
class second(object):

    def second_pit(self):

        action = raw_input("> ")

        if action == 'third pit':
            print "Very good! NOW, you are at the third pit."
            print "Continuing to let the pinball to forth pit."
            return ['third_pit', 'third']
        elif action == 'fifth pit':
            print "You will use one more step than others."
            return ['second_pit', 'second']
        else:
            return ['death', 'death']

