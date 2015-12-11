__author__ = 'oucb'
class line(object):


    def start_line(self):
        print "Now, you are at the start line."
        print "Your goal it to let the pinball to first pit"

        action = raw_input("> ")

        if action == 'first pit':
            print "Very good! Now,you are at the first pit"
            print "Continue to let the pinball to second pit"
            return ['first_pit', 'first']
        elif action == 'fifth pit':
            print "You will use one more step than others."
            return ['start_line', 'start']
        else:
            return ['death', 'death']

