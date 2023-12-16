"""      turtle-example-suite:

          tdemo_wikipedia3.py

This example is
inspired by the Wikipedia article on turtle
graphics. (See example wikipedia1 for URLs)

First we create (ne-1) (i.e. 35 in this
example) copies of our first turtle p.
Then we let them perform their steps in
parallel.

Followed by a complete undo().
"""
from turtle import Screen, Turtle, mainloop
from time import perf_counter as clock, sleep

#这是画图的主要函数mn_eck()
def mn_eck(p, ne,sz):
    #p is not defined,it is defined below
    turtlelist = [p]
    #create ne-1 additional turtles  mn_eck(p, 36, 19)
    for i in range(1,ne):
        q = p.clone()
        #the below parameters is 36
        q.rt(360.0/ne)
        turtlelist.append(q)
        p = q
    for i in range(ne):
        c = abs(ne/2.0-i)/(ne*.7)
        print(c)
        # let those ne turtles make a step
        # in parallel:
        for t in turtlelist:
            t.rt(360./ne)
            t.pencolor(1-c,0,c)
            t.fd(sz)

def main():
    s = Screen()
    s.bgcolor("black")
    p=Turtle()
    p.speed(1)
    p.hideturtle()
    p.pencolor("red")
    p.pensize(3)

    s.tracer(45,10)

    at = clock()
    mn_eck(p, 36, 19)
    et = clock()
    z1 = et-at

    sleep(10)

    at = clock()
    while any(t.undobufferentries() for t in s.turtles()):
        for t in s.turtles():
            t.undo()
    et = clock()
    return "runtime: %.3f sec" % (z1+et-at)


if __name__ == '__main__':
    msg = main()
    print(msg)
    mainloop()      