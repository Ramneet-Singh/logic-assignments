"""
Takes as input
(i) a formula file, containing a CNF formula in DIMACS format, and
(ii) a proof file that contains a resolution proof,
and prints “correct” if the resolution proof is correct, and “incorrect” otherwise.
Usage: python proof-checker.py <formulaFileName> <proofFileName>
Author: Ramneet Singh, IIT Delhi
"""
import sys

class CNFFormula(object):
    def __init__(self):
        super().__init__()
        self.numVariables = 0
        self.numClauses = 0
        self.addedClauses = 0
        self.clauses = dict()

    def addClause(self, literals, lineNum):
        if self.addedClauses==self.numClauses:
            raise Exception("Number of clauses in formula file is more than the number in header line!")
        for i in literals:
            if abs(i) > self.numVariables:
                raise Exception("Highest variable number in formula file is more than the number in header line!")
        self.addedClauses = self.addedClauses+1
        self.clauses[lineNum] = literals

    def __str__(self):
        output = ""
        for lineNum,clause in self.clauses.items():
            output += "Line " + str(lineNum) + ": "
            for literal in clause:
                output = output + str(literal) + " "
            output += "\n"
        return output


def parseClauses(formulaFileName):
    formulaFile = open(formulaFileName, 'r')
    formula = CNFFormula()
    literals = set()
    lineNum = 0
    for line in formulaFile:
        lineNum += 1
        if line[0]=='c':
            continue
        if line[0]=='p':
            tokens = line.strip().split()
            formula.numVariables = int(tokens[2])
            formula.numClauses = int(tokens[3])
            continue
        tokens = line.strip().split()
        for l in tokens:
            if l=="0":
                formula.addClause(literals.copy(), lineNum)
                literals = set()
            else:
                literals.add(int(l))
    formulaFile.close()
    return formula

def checkResolution(c1, c2, r):
    l0 = 0
    found = False
    for l in c1:
        if l not in r:
            found = True
            l0 = l
    if not found:
        return False
    if (-l0) not in c2:
        return False
    r0 = set()
    for l in c1:
        if l != l0:
            r0.add(l)
    for l in c2:
        if l != (-l0):
            r0.add(l)
    if r != r0:
        return False
    return True

def checkProof(formula, proofFileName):
    proofClauses = dict()
    proofFile = open(proofFileName, 'r')
    proofLineNum = 0
    for line in proofFile:
        proofLineNum += 1
        tokens = line.strip().split()
        lineNum = int(tokens[0][0])
        file = tokens[0][1]
        if file=='f':
            if lineNum not in formula.clauses:
                return False
            clause1 = formula.clauses[lineNum]
        elif file=='p':
            if lineNum not in proofClauses:
                return False
            clause1 = proofClauses[lineNum]
        else:
            raise Exception("Incorrect Proof File Format!")
        lineNum = int(tokens[1][0])
        file = tokens[1][1]
        if file=='f':
            if lineNum not in formula.clauses:
                return False
            clause2 = formula.clauses[lineNum]
        elif file=='p':
            if lineNum not in proofClauses:
                return False
            clause2 = proofClauses[lineNum]
        else:
            raise Exception("Incorrect Proof File Format!")
        resolvedClause = set()
        for i in range(2,len(tokens)):
            if tokens[i]=='0':
                if not checkResolution(clause1, clause2, resolvedClause):
                    return False
                proofClauses[proofLineNum] = resolvedClause.copy()
                break
            resolvedClause.add(int(tokens[i]))
    return True

if __name__=="__main__":
    formulaFileName = sys.argv[1]
    proofFileName = sys.argv[2]
    formula = parseClauses(formulaFileName)
    if checkProof(formula, proofFileName):
        print("correct")
    else:
        print("incorrect")
