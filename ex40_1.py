__author__ = 'oucb'
def dict_for_loop(list_x):
    # because the 'list_x.items()' return a list, so it can running without error
    # if the 'list_x.items()' become 'list_x', will return the error "'dict' object is not cabbable'
    for numbers in list_x.items():
        print numbers
c = dict([('one', 1),('two', 2),('three',3)])
dict_for_loop(c)