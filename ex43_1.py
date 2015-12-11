__author__ = 'oucb'
__author__ = 'oucb'
class first(object):

    def __init__(self, step):
        self.step = 0

    def first_pit(self):
        print "Now, you are at the first pit."
        print "Your goal it to let the pinball to second pit"

        action = raw_input("> ")

        if action == 'second pit':
            print "Very good! You are at the second pit."
            print "Continuing to let the pinball to third pit"
            return 'second_pit'
        elif action == 'fifth pit':
            print "You will use one more step than others."
            self.step += 1
            return 'second_pit'
        else:
            return 'death'

