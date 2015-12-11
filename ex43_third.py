__author__ = 'oucb'
class third(object):

    def third_pit(self):

        action = raw_input("> ")

        if action == 'fourth pit':
            print "Very good! Now, you are at the fourth pit."
            print "Continuing to let the pinball to fifth pit at the next step last."
            return ['fourth_pit', 'fourth']
        elif action == 'fifth pit':
            print "You will use one more step than others."
            return ['third_pit', 'third']
        else:
            return ['death', 'death']
