# -*- coding: utf-8 -*-


def xrange(start_stop, stop=None, step=None):
    """
    Funkcja która działa jak funkcja range (wbudowana i z poprzednich zajęć)
    która działa dla liczb całkowitych.
    """
    if step == None:
        step = 1
    if stop == None:
        stop = start_stop
        start_stop = 0
   
    yield start_stop
    while (start_stop + step) < stop:
        yield start_stop + step
        start_stop += step
                        
            
for i in xrange(2):
    print(i)
