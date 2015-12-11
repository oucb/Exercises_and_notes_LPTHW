__author__ = 'oucb'
class start(object):

    def __init__(self, step):
        self.step = 0

    def start_line(self):
        print "Now, you are at the start line."
        print "Your goal it to let the pinball to first pit"

        action = raw_input("> ")

        if action == 'first pit':
            print "Very good! continue to let the pinball to second pit"
            return 'first_pit'
        elif action == 'fifth pit':
            print "You will use one more step than others."
            self.step += 1
            return 'second_pit'
        else:
            return 'death'

