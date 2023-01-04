# Problem: https://www.hackerrank.com/challenges/text-wrap/problem

def wrap(string, max_width):
    s = ''
    for i in range(len(string)):
        if i>0 and i%max_width==0:
            s+="\n"
        s+=string[i]
    return s
