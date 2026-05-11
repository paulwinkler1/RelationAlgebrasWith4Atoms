# implemented for 1_37 - 37_37
import numpy as np
from itertools import product

# Id            = 0
# a             = 1
# r             = 2
# converse r    = 3

allowed_triples = []
identity_triples = [(0,0,0),(0,1,1),(2,1,2),(0,1,1)]
symmetric = True

def initialize():
    if not symmetric:
        initialize_asm()
    else:
        initialize_sym()

def initialize_asm():
    allowed_triples.append([(2,2,2),(1,2,2),(2,1,2)])                           #1
    allowed_triples.append([(1,1,1),(2,2,2),(1,2,2),(2,1,2)])                   #2
    allowed_triples.append([(2,2,3),(1,2,2),(2,1,2)])                           #3
    allowed_triples.append([(1,1,1),(2,2,3),(1,2,2),(2,1,2)])                   #4
    allowed_triples.append([(2,2,2),(2,2,3),(1,2,2),(2,1,2)])                   #5
    allowed_triples.append([(1,1,1),(2,2,2),(2,2,3),(1,2,2),(2,1,2)])           #6
    allowed_triples.append([(2,2,2),(2,1,1)])                                   #7
    allowed_triples.append([(1,1,1),(2,2,2),(2,1,1)])                           #8
    allowed_triples.append([(2,2,3),(2,1,1)])                                   #9
    allowed_triples.append([(1,1,1),(2,2,3),(2,1,1)])                           #21 
    allowed_triples.append([(2,2,2),(2,2,3),(2,1,1)])                           #22
    allowed_triples.append([(1,1,1),(2,2,2),(2,2,3),(2,1,1)])                   #22
    allowed_triples.append([(1,1,1),(2,2,2),(1,2,2),(2,1,1)])                   #23
    allowed_triples.append([(2,2,2),(1,2,2),(2,1,2),(2,1,1)])                   #24
    allowed_triples.append([(1,1,1),(2,2,2),(1,2,2),(2,1,2),(2,1,1)])           #25
    allowed_triples.append([(2,2,2),(2,2,3),(1,2,2),(2,1,2),(2,1,1)])           #26
    allowed_triples.append([(1,1,1),(2,2,2),(2,2,3),(1,2,2),(2,1,2),(2,1,1)])   #27
    allowed_triples.append(["fill", (2,2,1)])                                   #28
    allowed_triples.append([(2,2,2),(2,2,3),(2,2,1)])                           #29
    allowed_triples.append([(1,1,1),(1,2,2),(2,1,2),(2,2,1)])                   #31
    allowed_triples.append([(1,1,1),(2,2,2),(1,2,2),(2,1,2),(2,2,1)])           #32
    allowed_triples.append([(1,1,1),(2,2,2),(2,2,3),(1,2,2),(2,1,2),(2,2,1)])   #33
    allowed_triples.append([(2,2,2),(2,1,1),(2,2,1)])                           #33
    allowed_triples.append([(1,1,1),(2,2,2),(2,1,1),(2,2,1)])                   #34
    allowed_triples.append([(2,2,2),(2,2,3),(2,1,1),(2,2,1)])                   #35
    allowed_triples.append([(1,1,1),(2,2,2),(2,2,3),(2,1,1),(2,2,1)])           #36
    allowed_triples.append([(2,2,2),(1,2,2),(2,1,1),(2,2,1)])                   #37
    allowed_triples.append([(1,1,1),(2,2,2),(1,2,2),(2,1,1),(2,2,1)])           #38
    allowed_triples.append([(2,2,2),(2,2,3),(1,2,2),(2,1,1),(2,2,1)])           #39
    allowed_triples.append([(1,1,1),(2,2,2),(2,2,3),(1,2,2),(2,1,1),(2,2,1)])   #31
    allowed_triples.append([(1,1,1),(1,2,2),(2,1,2),(2,1,1),(2,2,1)])           #32
    allowed_triples.append([(2,2,2),(1,2,2),(2,1,2),(2,1,1),(2,2,1)])           #33
    allowed_triples.append([(1,1,1),(2,2,2),(1,2,2),(2,1,2),(2,1,1),(2,2,1)])   #33
    allowed_triples.append([(2,2,3),(1,2,2),(2,1,2),(2,1,1),(2,2,1)])           #34
    allowed_triples.append([(1,1,1),(2,2,3),(1,2,2),(2,1,2),(2,1,1),(2,2,1)])   #35
    allowed_triples.append([(2,2,2),(2,2,3),(1,2,2),(2,1,2),(2,1,1),(2,2,1)])   #36
    allowed_triples.append([(1,1,1),(2,2,2),(2,2,3),(1,2,2),(2,1,2),(2,1,1),(2,2,1)])   #37 

def c(atom):
    if not symmetric:
        if atom==0:
            return 0
        if atom==1:
            return 2
        if atom==2: 
            return 1

def get_cycle_structure(allowed):
    cycles = []
    for a in allowed:
        x = a[0]
        y = a[1]
        z = a[2]
        
        cycles.append((x,y,z))
        cycles.append((c(x),z,y))
        cycles.append((y,c(z),c(x)))
        cycles.append((c(y),c(x),c(z)))
        cycles.append((c(z),x,c(y)))
        cycles.append((z,c(y),x))
    return cycles

def polys31_65():
    # 0 = id, 1 = a, 2 = b
    allowed = [(0,0,0),(0,1,1),(0,2,2),(1,1,1),(2,2,2),(3,3,3),(1,2,2),(2,1,1),(3,1,1),(1,2,3)]
    cycles = get_cycle_structure(allowed)
    f = -1*np.ones((4,4,4), dtype=int)
    
    for i in range(4):
        f[i][i][i] = i

    for i in range(4):
        if i == 2:
            continue
        f[i][i][2] = i
        f[i][2][i] = i
        f[2][i][i] = i
        f[2][2][i] = 2
        f[2][i][2] = 2
        f[i][2][2] = 2
    
    for p in product(range(4), repeat=3):
        if f[p[0]][p[1]][p[2]] == -1:
            f[p[0]][p[1]][p[2]] = 1

    for (t1,t2,t3) in product(allowed, repeat=3):
        t = (f[t1[0]][t2[0]][t3[0]], f[t1[1]][t2[1]][t3[1]], f[t1[2]][t2[2]][t3[2]])
        if t not in cycles:
            print(t)
            print("Failed at binary relation with", t1, t2, t3)
            break


def polys4_7():
    # 0 = id, 1 = a, 2 = b
    allowed = [(0,0,0),(0,1,1),(0,2,2),(1,1,1),(2,2,2),(1,2,2)]
    cycles = get_cycle_structure(allowed)
    f = np.zeros((3,3), dtype=int)
    for i in range(2):
        f[i+1][0] = i+1
        f[0][i+1] = i+1
    for i in range(3):
        f[i][i] = i

    f[1][2] = 2
    f[2][1] = 2

    failed = False

    for (t1,t2) in product(allowed, repeat=2):
        t = (f[t1[0]][t2[0]], f[t1[1]][t2[1]], f[t1[2]][t2[2]])
        if t not in cycles:
            print("Failed at binary relation with", t1, t2)
            failed = True
            break
    
    if failed:
        return False


def polys(n):
    allowed = allowed_triples[n].append(identity_triples)
    print(allowed)
    cycles = get_cycle_structure(allowed)
    polys = []
    for p in product('12', '12', '13', '13', '23', '23'):
        f = np.zeros((4,4), dtype=int)
        for i in range(3):
            f[i+1][0] = i+1
            f[0][i+1] = i+1
        for i in range(4):
            f[i][i] = i

        f[2][1] = p[0]
        f[1][2] = p[1]
        f[3][1] = p[2]
        f[1][3] = p[3]
        f[3][2] = p[4]
        f[2][3] = p[5]

        failed = False

        # print(f)

        for (i,j) in product(range(4), repeat=2):
            if f[i][j] != c(f[c(i)][c(j)]):
                # print("Failed at binary relation with", i, j)
                failed = True
                break
        
        if failed:
            continue

        for (t1,t2) in product(allowed, repeat=2):
            if t1 == "fill" or t2 == "fill":
                continue
            t = (f[t1[0]][t2[0]], f[t1[1]][t2[1]], f[t1[2]][t2[2]])
            if t not in cycles:
                # print("Failed at binary relation with", t1, t2)
                failed = True
                break
        
        if failed:
            continue

        polys.append(f)
    return polys

if __name__ == "__main__":
    symmetric = True
    initialize()
    # print(len(allowed_triples))
    for i in range(65):
        f = polys(i)
        if len(f) > 0:
            print(i, f[0])
        
