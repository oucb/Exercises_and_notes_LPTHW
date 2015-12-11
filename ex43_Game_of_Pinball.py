__author__ = 'oucb'

from sys import exit

from ex43_death import death
from ex43_line import line
from ex43_first import first
from ex43_second import second
from ex43_third import third
from ex43_fourth import fourth


class Game_Of_Pinball(object):

    def __init__(self, start, room ):
        self.step = 0
        self.start = start
        self.room = room

    def play(self):
        next = self.start
        action = self.room
#       GOALS = {'start line': 'start_line', 'first pit': 'first_pit', 'second pit': 'second_pit',
#                'third pit': 'third_pit', 'fourth pit': 'fourth_pit', 'death': 'death'}
        ROOMS = {'line': line, 'first': first, 'second': second, 'third': third,
                 'fourth': fourth, 'death': death}

        while True:
#           next = GOALS[next]
            action = ROOMS[action]
            result = getattr(action(), next)
            running = result()
            next = running[0]
            action = running[1]
            self.step += 1
            print "You have used %d steps up to now" % self.step


a_game = Game_Of_Pinball("start_line", "line")
a_game.play()