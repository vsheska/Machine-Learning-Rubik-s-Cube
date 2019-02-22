import random

class Cube:
    '''
    
    '''
    def __init__(self, clist):
        assert type(clist) == type([])
        assert len(clist) == 24
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

#def brutesolve(cube):
#    PQ = [[cube, []]]
#    visited = [cube]
#    while True:
#        curPair = PQ.pop(0)
#        curCube = curPair[0]
#        curSeq = curPair[1]
#        for i in range(6):
#            newSeq = curSeq.copy()
#            newSeq.append(moveliststr[i])
#            newCube = curCube.copy()
#            movelist[i](newCube)
#            if newCube.solved():
#                return newSeq
#            if newCube in visited:
#                pass
#            else:
#                 PQ.append([newCube.copy(), newSeq])
                
def randomcube(n):
    A = solvedcube()
    while A.solved():
        scramble = []
        for i in range(random.randint(1, n)):     
            r = random.randrange(6)
            scramble.append(moveliststr[r])
            movelist[r](A)
    return (scramble, A)

def solvedcube():
    SolvedCube = Cube([0, 0, 0, 0, 1, 1, 2, 2, 3, 3, 1, 1, 2, 2, 3, 3, 4, 4, 4, 4,
                   5, 5, 5, 5])
    return SolvedCube
