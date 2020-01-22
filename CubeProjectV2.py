import random
import math
import time

class Cube:
    def __init__(self, clist):
        self.state = clist
    def __eq__(self, other):
        return self.state == other.state
    def copy(self):
        return Cube(self.state.copy())
    def R(self):
        temp = self.state[1]
        self.state[1] = self.state[7]
        self.state[7] = self.state[17]
        self.state[17] = self.state[21]
        self.state[21] = temp
        temp = self.state[3]
        self.state[3] = self.state[13]
        self.state[13] = self.state[19]
        self.state[19] = self.state[23]
        self.state[23] = temp
        temp = self.state[8]
        self.state[8] = self.state[14]
        self.state[14] = self.state[15]
        self.state[15] = self.state[9]
        self.state[9] = temp

    def Ri(self):
        temp = self.state[21]
        self.state[21] = self.state[17]
        self.state[17] = self.state[7]
        self.state[7] = self.state[1]
        self.state[1] = temp
        temp = self.state[23]
        self.state[23] = self.state[19]
        self.state[19] = self.state[13]
        self.state[13] = self.state[3]
        self.state[3] = temp
        temp = self.state[9]
        self.state[9] = self.state[15]
        self.state[15] = self.state[14]
        self.state[14] = self.state[8]
        self.state[8] = temp
        
    def F(self):
        temp = self.state[2]
        self.state[2] = self.state[11]
        self.state[11] = self.state[17]
        self.state[17] = self.state[8]
        self.state[8] = temp
        temp = self.state[3]
        self.state[3] = self.state[5]
        self.state[5] = self.state[16]
        self.state[16] = self.state[14]
        self.state[14] = temp
        temp = self.state[6]
        self.state[6] = self.state[12]
        self.state[12] = self.state[13]
        self.state[13] = self.state[7]
        self.state[7] = temp

    def Fi(self):
        temp = self.state[8]
        self.state[8] = self.state[17]
        self.state[17] = self.state[11]
        self.state[11] = self.state[2]
        self.state[2] = temp
        temp = self.state[14]
        self.state[14] = self.state[16]
        self.state[16] = self.state[5]
        self.state[5] = self.state[3]
        self.state[3] = temp
        temp = self.state[7]
        self.state[7] = self.state[13]
        self.state[13] = self.state[12]
        self.state[12] = self.state[6]
        self.state[6] = temp
        
    def U(self):
        temp = self.state[0]
        self.state[0] = self.state[2]
        self.state[2] = self.state[3]
        self.state[3] = self.state[1]
        self.state[1] = temp
        temp = self.state[4]
        self.state[4] = self.state[6]
        self.state[6] = self.state[8]
        self.state[8] = self.state[23]
        self.state[23] = temp
        temp = self.state[5]
        self.state[5] = self.state[7]
        self.state[7] = self.state[9]
        self.state[9] = self.state[22]
        self.state[22] = temp

    def Ui(self):
        temp = self.state[1]
        self.state[1] = self.state[3]
        self.state[3] = self.state[2]
        self.state[2] = self.state[0]
        self.state[0] = temp
        temp = self.state[23]
        self.state[23] = self.state[8]
        self.state[8] = self.state[6]
        self.state[6] = self.state[4]
        self.state[4] = temp
        temp = self.state[22]
        self.state[22] = self.state[9]
        self.state[9] = self.state[7]
        self.state[7] = self.state[5]
        self.state[5] = temp
    def solved(self):
        return self.state[0] == self.state[1] == self.state[2] == self.state[3]\
        and self.state[4] == self.state[5] == self.state[10] == self.state[11]\
        and self.state[6] == self.state[7] == self.state[12] == self.state[13]

movelist = [Cube.R, Cube.Ri, Cube.F, Cube.Fi, Cube.U, Cube.Ui]
moveliststr = ["R", "Ri", "F", "Fi", "U", "Ui"]

def brutesolve(cube, alg):
    PQ = [[evaluate(getinputs(cube), alg), cube, []]]
    visited = [cube]
    n = 0
    t1 = time.time()
    while time.time() < t1 + 1:
        n = n + 1
        curPair = PQ.pop(0)
        curCube = curPair[1]
        curSeq = curPair[2]
        for i in range(6):
            newSeq = curSeq.copy()
            newSeq.append(i)
            newCube = curCube.copy()
            movelist[i](newCube)
            if newCube.solved():
                print("Solved In Brute")
                
                return [newSeq[0], 1]
            if newCube in visited:
                pass
            else:
                visited.append(newCube.copy())
                info = [evaluate(getinputs(newCube), alg)[0],newCube.copy(), newSeq]
                PQ.append(info)
                #while j <= len(PQ):
                #    if j == len(PQ):
                #        PQ.append(info)
                #        j = len(PQ) + 1
                #    elif info[0] > PQ[j][0]:
                #        PQ.insert(0, info)
                #        j = len(PQ) + 1
                #    else:
                #        j = j + 1
                    
                    
    #print(n)
    PQ.sort()
    PQ.reverse()
    return [PQ[0][2][0], 0]

def listsum(l):
    n = len(l)
    total = 0
    for i in range(n):
        total = total + l[i]
    return total

def normalize(l):
    n = listsum(l)
    for i in range(len(l)):
        l[i] = l[i] / n



def randomcube(n):
    A = SolvedCube.copy()
    scramble = []
    for i in range(n):     
        r = random.randrange(6)
        scramble.append(moveliststr[r])
        movelist[r](A)
    return (scramble, A)

def sigmoid(x):
    if x < 0:
        x = 0
    return x
    
def getinputs(cube):
    inputs = [0] * 144
    for i in range(24):
        inputs[6*i + cube.state[i]] = 1
    return inputs

def genevalalg():
    L1 = []
    outnode = []
    for i in range(144):
        node = []
        for j in range(144):
            node.append(random.uniform(0, 1))
        normalize(node)
        L1.append(node.copy())
        outnode.append(random.uniform(0, 1))
    normalize(outnode)
    return [L1, outnode]

def dot(v1, v2):
    total = 0
    for i in range(len(v1)):
        total = total + v1[i] * v2[i]

def evaluate(inputs, alg):
    
    result = 0
    L1 = alg[0]
    outnode = alg[1]
    outres = []
    
    for i in range(144):
        L1Ni = L1[i]
        total1 = 0

        
        for j in range(144):
            mult = (inputs[j] * L1Ni[j])
            total1 = total1 + mult
        
        total2 = total1 * outnode[i]
        outres.append(total1)
        result = result + total2

    return (result, outres)

def wdfssolve(cube, alg):
    PQ = [[evaluate(getinputs(cube), alg), cube, []]]
    visited = [cube]
    n = 0
    while n < 21:
        n = n + 1
        nxt = PQ.pop(0)
        for i in range(6):
            curCube = nxt[1].copy()
            curSeq = nxt[2].copy()
            movelist[i](curCube)
            if curCube not in visited:
                visited.append(curCube.copy())
                curSeq.append(movelist[i])
                if curCube.solved():
                    return curSeq
                PQ.append([evaluate(getinputs(curCube), alg), curCube, curSeq])
                PQ.sort()
    
    return PQ[1][2]
    
def backprop(alg, evallist, inputs, factor):
    L1 = alg[0]
    outnode = alg[1]
    outres = evallist[1]
    normalize(outres)
    grad = outnode.copy()
    grad2 = outres
    for i in range(144):
        step = grad[i] * factor
        for j in range(144):
            L1[i][j] = max(0.0000001, L1[i][j] + step/144)
        normalize(L1[i])
        outnode[i] = max(0.0000001, outnode[i] + factor * outres[i]/144)

    normalize(outnode)
        
          
        
    
    

def train(cube, alg):
    last13 = []
    moves = []
    while True:
        seq = wdfssolve(cube, alg)
        last13.append(cube.copy())
        i = movelist.index(seq[0])
        seq[0](cube)
        print (moveliststr[i])
        if len(last13)>13:
            inputs = getinputs(last13.pop(0))
            backprop(alg, evaluate(inputs, alg), inputs, -1)
        
        if cube.solved():
            print("Solved")
            break
    
    



def solve(cube, alg):
    n = 0
    seq = []
    last13 = []
    while n < 20:
        n = n + 1
        bmove = brutesolve(cube, alg)
        if bmove[1] == [1]:
            n = n - 1
        move = bmove[0]
        print(moveliststr[move])
        seq.append(moveliststr[move])
        if not(cube in last13):
            last13.insert(0, cube.copy())
        if len(last13) > 13:
            last13.__delitem__(-1)
        movelist[move](cube)
        if cube.solved():
            fact = 10
            for k in range(len(last13)):
                
                inputs = getinputs(cube)
                evals = evaluate(inputs, alg)
                outres = evals[1]
                sumo = listsum(outres)  # sum of x vector components squared
                suma1 = listsum(alg[1])
                for i in range(144):
                    for j in range(144):
                        alg[0][i][j] = alg[0][i][j] - (inputs[j]/ 24)* (pow(outres[i], 2)/ sumo)* fact   
                    alg[1][i] = alg[1][i] - (pow(outres[i], 2)/ sumo)* fact
            return seq

        inputs = getinputs(cube)
        evals = evaluate(inputs, alg)
        outres = evals[1]
        sumo = listsum(outres)  # sum of x vector components squared
        suma1 = listsum(alg[1])
        for i in range(144):


            for j in range(144):

                alg[0][i][j] = alg[0][i][j] - (inputs[j]/ 24)* (pow(outres[i], 2)/ sumo)* 0.1


            alg[1][i] = alg[1][i] - (pow(outres[i], 2)/ sumo)* 0.1
    print("next cube")


        

SolvedCube = Cube([0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4,
                   5, 5, 5, 5])
B = SolvedCube.copy()
B.R()
B.R()
B.U()
alg = genevalalg()
inputs = getinputs(B)
evallist = evaluate(inputs, alg)
#while True:
#    (s, A) = randomcube(random.randint(1, 20))
#    print(s)
#    solve(A, alg)
    
