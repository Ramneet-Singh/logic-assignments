"""
Takes as input
(i) a formula file, containing a CNF formula in DIMACS format, and
(ii) a proof file that contains a resolution proof,
and prints “correct” if the resolution proof is correct, and “incorrect” otherwise.
Usage: python proof-checker.py <FormulaFilePath> <ProofFilePath>
Author: Ramneet Singh, IIT Delhi
"""
import sys

"""
CNF Formula Class. A formula is represented by a dict mapping line number --> Clause (set of literals).
In addition, the class stores the number of variables and the number of clauses and throws an exception
if more clauses are added or more variables are used.
"""
class CNFFormula(object):
    def __init__(self):
        super().__init__()
        self.numVariables = 0
        self.numClauses = 0
        self.addedClauses = 0
        self.clauses = dict()

    # Add clause with literals at lineNum.
    def addClause(self, literals, lineNum):
        if self.addedClauses==self.numClauses:
            raise Exception("Number of clauses in formula file is more than the number in header line!")
        for i in literals:
            if abs(i) > self.numVariables:
                raise Exception("Highest variable number in formula file is more than the number in header line!")
        self.addedClauses = self.addedClauses+1
        self.clauses[lineNum] = literals

    # Dump string representation of formula.
    def __str__(self):
        output = ""
        for lineNum,clause in self.clauses.items():
            output += "Line " + str(lineNum) + ": "
            for literal in clause:
                output = output + str(literal) + " "
            output += "\n"
        return output

# Given a formula file, parse it line by line to extract clauses. Return the CNFFormula object constructed.
def parseClauses(formulaFileName):
    formulaFile = open(formulaFileName, 'r')
    formula = CNFFormula()
    literals = set()
    lineNum = 0
    for line in formulaFile:
        lineNum += 1
        if line[0]=='c':
            # Comments
            continue
        if line[0]=='p':
            # Header line
            tokens = line.strip().split()
            formula.numVariables = int(tokens[2])
            formula.numClauses = int(tokens[3])
            continue
        # Form new clause. Add literals one-by-one.
        tokens = line.strip().split()
        for l in tokens:
            if l=="0":
                # End Of Clause
                formula.addClause(literals.copy(), lineNum)
                literals = set()
            else:
                literals.add(int(l))
    formulaFile.close()
    return formula

# Check whether c1 and c2 can be resolved to r. c1,c2,r are sets of literals (represented by ints).
def checkResolution(c1, c2, r):
    for l in c1:
        if (-l) in c2:
            # l,-l is a possible pair of complementary literals. Check.
            candidate = (c1 - {l}) | (c2 - {-l})
            if r==candidate:
                return True
    # If no pair can be found and verified, the resolution is not possible or not correct.
    return False

# Given an input formula (object of CNFFormula Class) and a proof file, check whether each line of the proof
# is a valid application of the resolution rule. Further check that the proof derives an empty clause.
# Return True if both these conditions are met, False otherwise.
def checkProof(formula, proofFileName):
    proofClauses = dict() # Mapping line number to proven clause
    proofFile = open(proofFileName, 'r')
    proofLineNum = 0
    for line in proofFile:
        # Get clause1, clause2, resolvent. Then call checkResolution to verify.
        proofLineNum += 1
        tokens = line.strip().split()

        # Clause 1
        lineNum = int(tokens[0][0])
        file = tokens[0][1]
        if file=='f':
            if lineNum not in formula.clauses:
                proofFile.close()
                return False
            clause1 = formula.clauses[lineNum]
        elif file=='p':
            if lineNum not in proofClauses:
                proofFile.close()
                return False
            clause1 = proofClauses[lineNum]
        else:
            raise Exception("Incorrect Proof File Format!")

        # Clause 2
        lineNum = int(tokens[1][0])
        file = tokens[1][1]
        if file=='f':
            if lineNum not in formula.clauses:
                proofFile.close()
                return False
            clause2 = formula.clauses[lineNum]
        elif file=='p':
            if lineNum not in proofClauses:
                proofFile.close()
                return False
            clause2 = proofClauses[lineNum]
        else:
            raise Exception("Incorrect Proof File Format!")

        # Resolved clause
        resolvedClause = set()
        for i in range(2,len(tokens)):
            if tokens[i]=='0':
                # Clause complete. Check the resolution.
                if not checkResolution(clause1, clause2, resolvedClause):
                    return False
                # Save resolved clause for future reference.
                proofClauses[proofLineNum] = resolvedClause.copy()
                break
            resolvedClause.add(int(tokens[i]))

    # Verify that the last clause derived in the proof is the empty clause.
    if (proofLineNum in proofClauses) and len(proofClauses[proofLineNum])==0:
        return True
    return False

if __name__=="__main__":
    formulaFileName = sys.argv[1]
    proofFileName = sys.argv[2]

    # Construct formula
    formula = parseClauses(formulaFileName)

    # Check proof
    if checkProof(formula, proofFileName):
        print("correct")
    else:
        print("incorrect")
