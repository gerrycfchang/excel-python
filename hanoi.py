def hanoi(n,fromPole, withPole, toPole):
    if n > 0:
        hanoi(n-1, fromPole, toPole, withPole)
        print "Move a Disc %s from %s to %s" % (str(n), fromPole, toPole)
        hanoi(n-1, withPole, fromPole, toPole)

if __name__ == '__main__': 
    hanoi(3,"A","B","C")