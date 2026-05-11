import math
from itertools import product

allowed_triples = []
symmetric = True
number = 65

# non-symmetric
# 0 = a
# 1 = r
# 2 = -r
# symmetric
# 0 = a
# 1 = b
# 2 = c


'''
Initializes the program according to the parameter 'symmetric'
'''
def initialize():
    if symmetric:
        initialize_sym()
    else:
        initialize_asym()

'''
Initializes the array 'allowed_triple' in the case of symmetric relation algebras. 
'''
def initialize_sym():
    allowed_triples.append(((0,1,1),(0,2,2),(1,2,2)))                                                   #1
    allowed_triples.append(((0,0,0),(0,1,1),(0,2,2),(1,2,2)))
    allowed_triples.append(((1,1,1),(0,1,1),(0,2,2),(1,2,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(0,2,2),(1,2,2)))
    allowed_triples.append(((2,2,2),(0,1,1),(0,2,2),(1,2,2)))                                           #5
    allowed_triples.append(((0,0,0),(2,2,2),(0,1,1),(0,2,2),(1,2,2)))
    allowed_triples.append(((1,1,1),(2,2,2),(0,1,1),(0,2,2),(1,2,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(0,1,1),(0,2,2),(1,2,2)))
    allowed_triples.append(((0,1,1),(1,0,0),(0,2,2),(1,2,2)))
    allowed_triples.append(((0,0,0),(0,1,1),(1,0,0),(0,2,2),(1,2,2)))                                   #10
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,0),(0,2,2),(1,2,2)))
    allowed_triples.append(((2,2,2),(0,1,1),(1,0,0),(0,2,2),(1,2,2)))
    allowed_triples.append(((0,0,0),(2,2,2),(0,1,1),(1,0,0),(0,2,2),(1,2,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(0,1,1),(1,0,0),(0,2,2),(1,2,2)))
    allowed_triples.append(((1,0,0),(0,2,2),(2,0,0),(1,2,2)))                                           #15
    allowed_triples.append(((0,0,0),(1,0,0),(0,2,2),(2,0,0),(1,2,2)))
    allowed_triples.append(((1,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2)))
    allowed_triples.append(((0,0,0),(2,2,2),(1,0,0),(0,2,2),(2,0,0),(1,2,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(1,0,0),(0,2,2),(2,0,0),(1,2,2)))                   #20
    allowed_triples.append(((0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(2,1,1)))
    allowed_triples.append(((0,0,0),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(2,1,1)))
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(2,1,1)))
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(2,1,1)))
    allowed_triples.append(("fill", (0,1,2)))                                                           #25
    allowed_triples.append(((0,0,0),(0,1,1),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,0),(0,1,2)))
    allowed_triples.append(((0,0,0),(0,1,1),(0,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(1,0,0),(2,0,0),(0,1,2)))
    allowed_triples.append(((0,0,0),(2,2,2),(0,1,1),(1,0,0),(2,0,0),(0,1,2)))                           #30
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(0,1,1),(1,0,0),(2,0,0),(0,1,2)))
    allowed_triples.append(((0,0,0),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(0,2,2),(1,2,2),(0,1,2)))                           #35
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(0,1,1),(0,2,2),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,0),(0,2,2),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(0,1,1),(1,0,0),(0,2,2),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,1,1),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(0,1,1),(2,0,0),(1,2,2),(0,1,2)))                                   #40
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(0,1,1),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,1,1),(1,0,0),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(0,1,1),(1,0,0),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((1,1,1),(0,1,1),(1,0,0),(2,0,0),(1,2,2),(0,1,2)))                           #45
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,0),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((2,2,2),(0,1,1),(1,0,0),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(2,2,2),(0,1,1),(1,0,0),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((1,1,1),(2,2,2),(0,1,1),(1,0,0),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(0,1,1),(1,0,0),(2,0,0),(1,2,2),(0,1,2)))           #50
    allowed_triples.append(((1,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(0,1,2)))                   #55
    allowed_triples.append(((1,1,1),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((2,2,2),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,0,0),(2,2,2),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((1,1,1),(2,2,2),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(0,1,2)))           #60
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(0,1,2)))
    allowed_triples.append(((0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(2,1,1),(0,1,2)))
    allowed_triples.append(((0,0,0),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(2,1,1),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(2,1,1),(0,1,2)))
    allowed_triples.append(((0,0,0),(1,1,1),(2,2,2),(0,1,1),(1,0,0),(0,2,2),(2,0,0),(1,2,2),(2,1,1),(0,1,2))) #65

'''
Initializes the array 'allowed_triple' in the case of non-symmetric relation algebras. 
'''
def initialize_asym():
    allowed_triples.append(((1,1,1),(0,1,1),(1,0,1)))                           #1
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,1)))                   #2
    allowed_triples.append(((1,1,2),(0,1,1),(1,0,1)))                           #3
    allowed_triples.append(((0,0,0),(1,1,2),(0,1,1),(1,0,1)))                   #4
    allowed_triples.append(((1,1,1),(1,1,2),(0,1,1),(1,0,1)))                   #5
    allowed_triples.append(((0,0,0),(1,1,1),(1,1,2),(0,1,1),(1,0,1)))           #6
    allowed_triples.append(((1,1,1),(1,0,0)))                                   #7
    allowed_triples.append(((0,0,0),(1,1,1),(1,0,0)))                           #8
    allowed_triples.append(((1,1,2),(1,0,0)))                                   #9
    allowed_triples.append(((0,0,0),(1,1,2),(1,0,0)))                           #10 
    allowed_triples.append(((1,1,1),(1,1,2),(1,0,0)))                           #11
    allowed_triples.append(((0,0,0),(1,1,1),(1,1,2),(1,0,0)))                   #12
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,0)))                   #13
    allowed_triples.append(((1,1,1),(0,1,1),(1,0,1),(1,0,0)))                   #14
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,1),(1,0,0)))           #15
    allowed_triples.append(((1,1,1),(1,1,2),(0,1,1),(1,0,1),(1,0,0)))           #16
    allowed_triples.append(((0,0,0),(1,1,1),(1,1,2),(0,1,1),(1,0,1),(1,0,0)))   #17
    allowed_triples.append(("fill", (1,1,0)))                                   #18
    allowed_triples.append(((1,1,1),(1,1,2),(1,1,0)))                           #19
    allowed_triples.append(((0,0,0),(0,1,1),(1,0,1),(1,1,0)))                   #20
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,1),(1,1,0)))           #21
    allowed_triples.append(((0,0,0),(1,1,1),(1,1,2),(0,1,1),(1,0,1),(1,1,0)))   #22
    allowed_triples.append(((1,1,1),(1,0,0),(1,1,0)))                           #23
    allowed_triples.append(((0,0,0),(1,1,1),(1,0,0),(1,1,0)))                   #24
    allowed_triples.append(((1,1,1),(1,1,2),(1,0,0),(1,1,0)))                   #25
    allowed_triples.append(((0,0,0),(1,1,1),(1,1,2),(1,0,0),(1,1,0)))           #26
    allowed_triples.append(((1,1,1),(0,1,1),(1,0,0),(1,1,0)))                   #27
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,0),(1,1,0)))           #28
    allowed_triples.append(((1,1,1),(1,1,2),(0,1,1),(1,0,0),(1,1,0)))           #29
    allowed_triples.append(((0,0,0),(1,1,1),(1,1,2),(0,1,1),(1,0,0),(1,1,0)))   #30
    allowed_triples.append(((0,0,0),(0,1,1),(1,0,1),(1,0,0),(1,1,0)))           #31
    allowed_triples.append(((1,1,1),(0,1,1),(1,0,1),(1,0,0),(1,1,0)))           #32
    allowed_triples.append(((0,0,0),(1,1,1),(0,1,1),(1,0,1),(1,0,0),(1,1,0)))   #33
    allowed_triples.append(((1,1,2),(0,1,1),(1,0,1),(1,0,0),(1,1,0)))           #34
    allowed_triples.append(((0,0,0),(1,1,2),(0,1,1),(1,0,1),(1,0,0),(1,1,0)))   #35
    allowed_triples.append(((1,1,1),(1,1,2),(0,1,1),(1,0,1),(1,0,0),(1,1,0)))   #36
    allowed_triples.append(((0,0,0),(1,1,1),(1,1,2),(0,1,1),(1,0,1),(1,0,0),(1,1,0)))   #37

'''
Useful to generate LaTex-Code
'''
def t(triple):
    return "(" + translate(triple[0]) + "," + translate(triple[1]) + "," + translate(triple[2]) + ")"

'''
Useful to generate LaTex-Code
'''
def translate(atom): 
    if symmetric: 
        if atom == 0: 
            return "a"
        if atom == 1: 
            return "b"
        if atom == 2: 
            return "c"
    else:
        if atom == 0: 
            return "a"
        if atom == 1: 
            return "r"
        if atom == 2: 
            return "\\breve{{r}}"

'''
Calculates the converse of an atom.
param: atom
return: the converse of the atom
'''
def c(atom):
    if symmetric:
        return atom

    if atom==0:
        return 0
    if atom==1:
        return 2
    if atom==2: 
        return 1
    
'''
Calculates all the allowed triples according 
param: array of allowed triples in the standard form
return: array of all allowed triples, expanded by teh cycle law
'''
def get_cycle_structure(allowed):
    cycles = []
    for a in allowed:
        x = a[0]
        y = a[1]
        z = a[2]
        if x == y and y == z and symmetric:
            cycles.append((x,x,x))
        elif y == z and symmetric:
            cycles.append((x,y,y))
            cycles.append((y,x,y))
            cycles.append((y,y,x))
        elif not symmetric and a == (1,1,2):
            cycles.append((1,1,2))
            cycles.append((2,2,1))
        elif not symmetric and a == (1,0,1):
            cycles.append((1,0,1))
            cycles.append((2,1,0))
            cycles.append((0,2,2))
        else:
            # these triples are all equivalent according to the cycle law 
            cycles.append((x,y,z))
            cycles.append((c(x),z,y))
            cycles.append((y,c(z),c(x)))
            cycles.append((c(y),c(x),c(z)))
            cycles.append((c(z),x,c(y)))
            cycles.append((z,c(y),x))
    return cycles

'''
Checks whether the relation algebra n_number has a normal representation by 2-point-amalgamation of size 5. 
param: number of relation algebra
return: normal representation?
'''
def has_normal(n):
    # print(n+1)
    allowed = allowed_triples[n]
    cycles = get_cycle_structure(allowed)
    r = True 
    for a in allowed:
        # For a given allowed triple 'a', if we add some point, 'S' collects all possibilities to label the edges with atoms
        # In directed case: From the allowed triple to the new point
        S = []
        for x in product(range(3), repeat=3):
            if (a[0], x[1], x[0]) in cycles and (a[2], x[1], x[0]) in cycles and (a[1], x[2], x[1]) in cycles:
                S.append(x)

            # if (a[0], x[1], x[0]) in cycles and (a[1], x[2], x[1]) in cycles and (a[2], x[2], x[0]) in cycles:
            #     S.append(x)

        # For every network in S we add another point and collect all consistent networks in 'T'
        for x in S:
            T = []
            for y in product(range(3), repeat=4):
                if (a[0], y[1], y[0]) in cycles and (a[2], y[2], y[0]) in cycles and (x[0], y[3], y[0]) in cycles \
                    and (a[1], y[2], y[1]) in cycles and (x[1], y[3], y[1]) in cycles and (x[2], y[3], y[2]) in cycles:
                    T.append(y)
            # For every two triangles t1, t2 (left and right in diagram) from S there has to be a connection z.
            # If i = j we can always choose z = Id and wlog we assume j < i.
            for i in range(1, len(T)):
                t1 = T[i]
                for j in range(i+1): 
                    t2 = T[j]
                    possible = False
                    for z in range(3):
                        # In directed case: t1[.], t2[.] is from the allowed triple 'a' outwards and 'z' is from "t1 to t2". 
                        if (t1[0], z, t2[0]) in cycles and (t1[1], z, t2[1]) in cycles and (t1[2], z, t2[2]) in cycles and (t1[3], z, t2[3]) in cycles \
                            or t1 == t2:
                            possible = True
                            break

                    if not possible:
                        r = False

                        ## counts same atoms on left and right
                        # cnt = 0
                        # s = ""
                        # for k in range(3):
                        #     if t1[k] == t2[k]:
                        #         s += str(t1[k])
                        #         cnt += 1
                        # print(x,t1,t2,cnt,s)

                        # gives one counter example
                        print(str(n+1) + "_" + str(number) + " has no normal representation. Failed at", a, x, t1, t2)
                        # print(str(n+1) + "_{" + str(number) + "} & " + t(a) + ", " + t(t1) + ", " + t(t2) + "\\\\ \\hline") # LaTeX

                        return False # comment out for if you want to debug        
        
    return r

def has_normal_all():
    for n in range(number):
        if has_normal(n):
           print(str(n+1) + " HAS NORMAL")

if __name__ == "__main__":
    # switch this boolean for symmetric/non-symmetric case
    symmetric = False

    initialize()
    if symmetric:
        print("ALL RELATION ALGEBRAS ARE SYMMETRIC")
        number = 65
    else:
        print("ALL RELATION ALGEBRAS ARE NON-SYMMETRIC")
        number = 37

    has_normal_all()
    # has_normal(29) # attention: the counting starts with 0

    # x = 1
    # y = 1
    # z = 2
    # cycles = []
    # cycles.append((x,y,z))
    # cycles.append((c(x),z,y))
    # cycles.append((y,c(z),c(x)))
    # cycles.append((c(y),c(x),c(z)))
    # cycles.append((c(z),x,c(y)))
    # cycles.append((z,c(y),x))
    # print(cycl