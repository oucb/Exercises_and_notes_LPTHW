__author__ = 'oucb'
class forth(object):

    def __init__(self, step):
        self.step = 0

    def forth_pit(self):
        print "Now, you are at the forth pit."
        print "Your goal it to let the pinball to fifth pit"

        action = raw_input("> ")

        if action == 'fifth pit':
            print "Congratulation! you succed to let the pinball to fifth pit at last"
            exit(0)
        else:
            return 'death'
