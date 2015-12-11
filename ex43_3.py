__author__ = 'oucb'
class third(object):

    def __init__(self, step):
        self.step = 0

    def third_pit(self):
        print "Now, you are at the third pit."
        print "Your goal it to let the pinball to forth pit"

        action = raw_input("> ")

        if action == 'forth':
            print "Very good! you are at the forth pit."
            print "You should let the pinball to fifth pit at the next step."
            return 'forth_pit'
        elif action == 'fifth pit':
            print "You will use one more step than others."
            self.step += 1
            return 'forth_pit'
        else:
            return 'death'
