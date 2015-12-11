__author__ = 'oucb'
class second(object):

    def __init__(self, step):
        self.step = 0

    def second_pit(self):
        print "Now, you are at the second pit."
        print "Your goal it to let the pinball to third pit"

        action = raw_input("> ")

        if action == 'third pit':
            print "Very good! you are at the third pit."
            print "You should let the pinball to forth pit at the next step."
            return 'third_pit'
        elif action == 'fifth pit':
            print "You will use one more step than others."
            self.step += 1
            return 'third_pit'
        else:
            return 'death'

