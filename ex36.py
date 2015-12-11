__author__ = 'oucb'
def work_time():
    print "the time what you get at the workplace determin whether you lot or not."
    w_time = raw_input("> ")
    if w_time < 510:
        good_time()
    else:
        bad_time()
def work_bus():
    print "the time bus get at the station."
    b_time = raw_input("> ")
    while True:
        if b_time < 470:
            good_time()
        elif b_time in range(470,490):
            work_time()
        else:
            bad_time()
def good_time():
    print "Good luck! you are so great!"
    exit(0)

def bad_time():
    print "So bad! Sorry!"
    exit(0)

def eat_select():
    print "You can select what to eat."
    e_select = raw_input("> ")
    if "caofen" in e_select:
        print "You can select hundun or banmian"
        work_bus()
    else:
        print "Buy something else to eat"
        work_bus()
def go_work():
    print "Select the time to awake"
    bed_time = raw_input("> ")
    if bed_time < 450:
        print "You can eat"
        eat_select()
    else:
        print "Oh, my god!you can not eat"
        work_bus()
go_work()

