### Important Notes!

###1.
#Only immutable types can be a dictionary key
#Only immutable types can be in a set

###2.
#Standard Format and common functions of Graphics
#(1)put it at the beginning of programming
from graphics import graphics
#(2)Create new gui and shapes
gui = graphics(500,700,'GUI')
gui.rectangle(50,50,100,100,'blue')
gui.ellipse(50,50,100,100,'red')
gui.line(50,50,200,200,'green',5)
gui.triangle(50,50,25,75,75,75,'yellow')
#(3)Move the shape
def move():
    gui = graphics(500, 300, 'Example')
    x_coord = 0
    while True:
        gui.clear()
        gui.rectangle(x_coord, 125, 50, 50, 'blue')
        gui.update_frame(30)
        x_coord += 2

#(4)Use mouse
def mouse():
    GUI = graphics(500, 300, 'Example')
    while True:
        GUI.clear()
        GUI.rectangle(GUI.mouse_x - 50, GUI.mouse_y - 50, \
                      100, 100, 'blue')
        GUI.update_frame(60)


###3.
#Implement the pythagorean function
a = 3
b = 4
print((a**2 + b**2)**0.5)

###4.
#Random
import random
# random.random() will return a float between 0 and 1
print(random.random())
# random.randint() will return a int between range the parameters expressing
print(random.randint(0,5))
# the random int group should include 5

###5.
#exit the program
from os import _exit as exit
print('I love you.')
My_answer = input('Do you love me, Yes or No?')
if My_answer == 'Yes!' or My_answer == 'Yes':
    print('We will be together forever!')
elif My_answer == 'No':
    exit(0)
    print('No!I am heartbroken!')

###6.
#Math!
#（1）**
#（2）* / % //
#(3)+ -
#(4)<= < > >=
#(5)<> == !=
#(6)= %= /= //= -= += *= **=
#(7)is is not
#(8)in not in
#(9)not and or

###7.
#teminology!
'''(1)CPU:Central Processing Unit
(2)RAM:Random-Access Memory
(3)ESD:external storage(memory) devices
(4)ASCII:The American Standard Code for Information Interchange
(5)DVD:digital versatile disc
(6)CD:Compact Disc Digital Audio
(7)WNIC: wireless network interface controller
(8)SSD:solid-state drive
(9)HDD:hard disk drive
(10)MOBO:mother board'''

def main():
    move()
    mouse()

main()
