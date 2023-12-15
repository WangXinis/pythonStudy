from turtle import *
color('red')
fillcolor('yellow')
begin_fill()
a='y'
for steps in range(100):
    while a=='y':
        forward(200)
        left(170)
        print(abs(pos()))
        if abs(pos())<1:
            print("这里小于1")
            a='n'
            break
end_fill()
mainloop()