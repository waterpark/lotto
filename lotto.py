from random import *

cnt = 0

while cnt < 5:

    ret = list(range(1,46))

    shuffle(ret)

    ret = sample(ret, 6)
    ret.sort()

    print("{0} {1} {2} {3} {4} {5}" .format(ret[0], ret[1], ret[2], ret[3], ret[4], ret[5]))

    cnt += 1