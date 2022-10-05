"""
Given a formula and a modified proof file but with holes (denoted by “??”), this outputs a complete proof file.
Author: Ramneet Singh, IIT Delhi
"""
from typing import List, Dict, Set, Tuple
import sys
sys.setrecursionlimit(100000)

"""
Parse the input clauses given in formula file and store in inputClauses dict.
Handles commented lines. Also checks that header line matches with the rest of the file, and raises an error otherwise.
Returns an inputClauses Dict mapping line number --> clause (set of literals).
"""
def parseInput(formulaFileName : str) -> Dict[int,Set[int]]:
    """Input Clauses in Formula File. Dict mapping line number --> clause (set of literals)"""
    inputClauses : Dict[int,Set[int]] = dict()

    with open(formulaFileName, 'r') as formulaFile:
        literals : Set[int] = set()
        lineNum : int = 0
        addedClauses : int = 0
        for line in formulaFile:
            lineNum += 1
            if line[0]=='c':
                # Comments
                continue
            if line[0]=='p':
                # Header line
                tokens = line.strip().split()
                numVariables = int(tokens[2])
                numClauses = int(tokens[3])
                continue
            # Form new clause. Add literals one-by-one.
            tokens = line.strip().split()
            for l in tokens:
                if l=="0":
                    # End Of Clause
                    if addedClauses >= numClauses:
                        raise Exception("Number of clauses in formula file is more than the number in header line!")
                    inputClauses[lineNum] = literals.copy()
                    addedClauses += 1
                    literals = set()
                else:
                    if abs(int(l))>numVariables:
                        raise Exception("Highest variable number in formula file is more than the number in header line!")
                    literals.add(int(l))
    return inputClauses

"""
Parses the given proof file and fills in proofClauses list. Doesn't fill resolved clause, that will be done by
fillProof. Returns proof clauses - a list of tuples ("nf/p","mf/p", resolved clause).
"""
def parseProof(proofFileName : str) -> List[Tuple[str,str,Set[int]]]:
    """
    Proof Clauses. List with Tuple of ("nf/p", "mf/p", resolved clause) at index lineNum-1.
    where resolved clause is the result of resolving line n of f/p file with line m of f/p file.
    If "nf/p" or "mf/p"=="??" this is a hole.
    """
    proofClauses : List[Tuple[str,str,Set[int]]] = list()

    with open(proofFileName, 'r') as proofFile:
        for line in proofFile:
            tokens = line.strip().split()
            proofClauses.append((tokens[0], tokens[1], set())) # Keep resolvent empty for now
    return proofClauses

"""Check if two clauses can be resolved."""
def canResolve(c1 : Set[int], c2 : Set[int]) -> bool:
    for l in c1:
        if (-l) in c2:
            return True
    return False

"""Assuming they can be resolved, resolve two clauses. If multiple resolvents possible, choose least literal."""
def resolve(c1 : Set[int], c2 : Set[int]) -> Set[int]:
    for l in sorted(c1, key=lambda x : abs(x)):
        if (-l) in c2:
            r : Set[int] = (c1 - {l}) | (c2 - {-l})
            return r
    raise Exception("resolve called on two unresolvable clauses!")

"""
Fills in the proof in proofClauses list, starting from line number l.
Returns True on success, False on failure.
"""
def fillProof(l : int, inputClauses : Dict[int,Set[int]], proofClauses : List[Tuple[str,str,Set[int]]]) -> bool:
    for i in range(l-1, len(proofClauses)):
        line1:str = proofClauses[i][0]
        line2:str = proofClauses[i][1]

        """Check if this line has a hole."""
        if line1!="??" and line2!="??":
            """No holes. Get both the clauses."""
            file = line1[-1]
            lineNum = int(line1[:-1])
            if file=="f":
                if lineNum not in inputClauses:
                    return False
                clause1 = inputClauses[lineNum]
            else:
                assert file=="p"
                if lineNum>i:
                    return False
                clause1 = proofClauses[lineNum-1][2]
            file = line2[-1]
            lineNum = int(line2[:-1])
            if file=="f":
                if lineNum not in inputClauses:
                    return False
                clause2 = inputClauses[lineNum]
            else:
                assert file=="p"
                if lineNum>i:
                    return False
                clause2 = proofClauses[lineNum-1][2]

            """Resolve the clauses and fill in the proof."""
            if not canResolve(clause1, clause2):
                return False
            proofClauses[i] = (proofClauses[i][0], proofClauses[i][1], resolve(clause1, clause2))

            """If this is the last line, ensure we've reached an empty clause."""
            if i==len(proofClauses)-1 and len(proofClauses[i][2])!=0:
                return False
            continue

        if line1=="??":
            fillIdx=0
        else:
            fillIdx=1

        """Search for a clause to fill the hole."""
        for inLine in inputClauses:
            """Fill this clause here. Then recursively try to fill ahead."""
            if fillIdx==0:
                proofClauses[i] = (str(inLine)+"f", proofClauses[i][1], proofClauses[i][2])
            else:
                proofClauses[i] = (proofClauses[i][0], str(inLine)+"f", proofClauses[i][2])
            if fillProof(i+1, inputClauses, proofClauses):
                return True
            if fillIdx==0:
                proofClauses[i] = ("??", proofClauses[i][1], proofClauses[i][2])
            else:
                proofClauses[i] = (proofClauses[i][0], "??", proofClauses[i][2])

        for j in range(i):
            """Fill this clause here. Then recursively try to fill ahead."""
            if fillIdx==0:
                proofClauses[i] = (str(j+1)+"p", proofClauses[i][1], proofClauses[i][2])
            else:
                proofClauses[i] = (proofClauses[i][0], str(j+1)+"p", proofClauses[i][2])
            if fillProof(i+1, inputClauses, proofClauses):
                return True
            if fillIdx==0:
                proofClauses[i] = ("??", proofClauses[i][1], proofClauses[i][2])
            else:
                proofClauses[i] = (proofClauses[i][0], "??", proofClauses[i][2])

        """We weren't able to find a suitable clause."""
        return False

    """We've reached the end of the file."""
    return True

"""Print the proof to proofFileName. If success, print the resolved clauses. Otherwise, print np in place of ??."""
def printProof(success:bool, proofFileName:str, proofClauses : List[Tuple[str,str,Set[int]]]) -> None:
    with open(proofFileName, 'w') as outFile:
        for i in range(len(proofClauses)):
            string = ""
            if proofClauses[i][0]=="??":
                string += "np "
            else:
                string += proofClauses[i][0]
                string += " "
            if proofClauses[i][1]=="??":
                string += "np"
            else:
                string += proofClauses[i][1]
            if success:
                string += " "
                for l in sorted(proofClauses[i][2], key=lambda x : (abs(x),x)):
                    string += str(l)
                    string += " "
                string += "0"
            string += "\n"
            outFile.write(string)

def solve(formulaFileName : str, proofFileName : str, outFileName : str) -> None:

    """Input Clauses in Formula File. Dict mapping line number --> clause (set of literals)"""
    inputClauses : Dict[int,Set[int]] = dict()

    """
    Proof Clauses. List with Tuple of ("nf/p", "mf/p", resolved clause) at index lineNum-1.
    where resolved clause is the result of resolving line n of f/p file with line m of f/p file.
    If "nf/p" or "mf/p"=="??" this is a hole.
    """
    proofClauses : List[Tuple[str,str,Set[int]]] = list()

    """Parse the input clauses given in formula file and store them in inputClauses dict."""
    inputClauses = parseInput(formulaFileName)

    """Parse the given proof and store it in proofClauses list."""
    proofClauses = parseProof(proofFileName)

    """Fill in the proof in proofClauses list, starting from line number 1."""
    if fillProof(1, inputClauses, proofClauses):
        """Success! Print out the proof."""
        printProof(True, outFileName, proofClauses)
    else:
        """Failure!(?) Print out the proof with np in place of holes."""
        printProof(False, outFileName, proofClauses)
