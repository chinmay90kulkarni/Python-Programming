#Local and Global variables 
# Edited by Soham


def func1():
    global a
    a=1
    b = 2

a="One"
b="Two"
func1()
print "a=",a    # a=1 if a is global else a= "One"
print "b=",b     #b="two"
print "----------------------------------------------------"
