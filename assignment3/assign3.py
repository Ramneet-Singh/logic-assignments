"""
Takes a CNF formula file F in DIMACS format as input.
- When n=1, outputs already horn if the formula is a Horn formula and not horn otherwise.
- When n=2, outputs a 2-CNF formula G (in DIMACS format) such that G is satisfiable if and only if F is renamable Horn.
- When n=3, outputs already horn if the formula is a Horn formula, otherwise renamable if it is renamable Horn and not renamable otherwise.
- When n=4, outputs already horn if the formula is a Horn formula, not renamable if it is not renamable. Otherwise,
  outputs a (space-separated) list of variables to be negated for F to become Horn.
"""
from collections import defaultdict
from typing import List, Set, Tuple, FrozenSet, Dict
import sys

"""
Convert the CNF formula F to string in DIMACS format.
"""
def formulaToString(F : Set[FrozenSet[int]], numVariables : int, numClauses : int, comment : str) -> str:
    output : str = ""
    output += f"c {comment}\n"
    output += f"p cnf {numVariables} {numClauses}\n"
    C : FrozenSet[int]
    for C in F:
        l : int
        for l in sorted(C, key = lambda x : (abs(x),x)):
            output += f"{l} "
        output += "0\n"
    return output

"""
Parse the input formula from the formula file content and store it as a set of sets of integers.
Handles commented lines. Also checks that header line matches with the rest of the file, and raises an error otherwise.
Returns a formula which is a set of clauses (sets of literals).
"""
def parseFormula(formulaFileContent : str) -> Tuple[Set[FrozenSet[int]], int, int]:
    """Formula : Set of sets of literals"""
    formula : Set[FrozenSet[int]] = set()
    numClauses : int = 0
    numVariables : int = 0

    literals : Set[int] = set()
    addedClauses : int = 0
    for line in formulaFileContent.split("\n"):
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
                formula.add(frozenset(literals))
                addedClauses += 1
                literals = set()
            else:
                if abs(int(l))>numVariables:
                    raise Exception("Highest variable number in formula file is more than the number in header line!")
                literals.add(int(l))
    return (formula, numVariables, numClauses)

"""
Check whether a formula is a Horn formula or not.
"""
def checkHorn(formula : Set[FrozenSet[int]]) -> bool:
    # Check each clause
    clause : FrozenSet[int]
    for clause in formula:
        # Check if there are two or more positive literals
        foundPositiveLiteral : bool = False
        l : int
        for l in clause:
            if (l>0) and foundPositiveLiteral:
                return False
            if (l>0):
                foundPositiveLiteral = True
    return True

"""
Convert formula F to a 2-CNF formula G such that G is satisfiable if and only if F is renamable Horn.
Idea: Formula F with variables x1,...,xn. Make a 2-CNF Formula G with variables y1,...,yn.
Any model corresponds to a negation of some of the variables in F. yi = 1 => xi has to be negated in the formula F.
We will derive conditions on the negation which will ensure that the transformed formula is a Horn formula.
If there is a model which satisfies these conditions, then the formula is renamable Horn,
through negating exactly those variables xi which have yi=1.
"""
def convertFormula(F : Set[FrozenSet[int]]) -> Set[FrozenSet[int]]:
    G : Set[FrozenSet[int]] = set()
    # Each clause should be a Horn clause after renaming. So, iterate over clauses.
    clause : FrozenSet[int]
    for clause in F:
        # Get the 2-CNF clauses which must hold for clause to be Horn after renaming.
        S : Set[FrozenSet[int]] = convertClause(clause)
        G = G.union(S)
    return G

"""
Convert a clause to a 2-CNF Formula which is satisfiable if and only if the renaming leads to clause becoming a Horn clause.
Note: If corresponding variable is 1 the original variable should be negated, otherwise not.
"""
def convertClause(C : Set[int]) -> Set[FrozenSet[int]]:
    S : Set[FrozenSet[int]] = set()
    literals : List[int] = list(C)
    i : int
    for i in range(len(literals)):
        j : int
        for j in range(i+1,len(literals)):
            """
            Case analysis for reference:
                literals[i]<0 and literals[j]<0 : don't negate var[literals[i]] or don't negate var[literals[j]]
                literals[i]<0 and literals[j]>0 : don't negate var[literals[i]] or negate var[literals[j]]
                literals[i]>0 and literals[j]<0 : negate var[literals[i]] or don't negate var[literals[j]]
                literals[i]>0 and literals[j]>0 : negate var[literals[i]] or negate var[literals[j]]
            """
            S.add( frozenset({ literals[i], literals[j] }) )
    return S

"""
Graph class. Meant to be used to represent a 2-CNF Formula.
"""
class Graph:
    vertices : Set[int] = set()
    adjDict : Dict[int, Set[int]] = defaultdict(set)

"""
Perform DFS on graph from source node. Fill up reachable dict.
reachable: Dict mapping node to set of nodes reachable from it.
"""
def DFS(graph : Graph, source : int, reachable : Dict[int, Set[int]]) -> None:
    stack : List[int] = [source]
    visited : Set[int] = set()
    while not len(stack)==0:
        node : int = stack.pop()
        visited.add(node)
        v : int
        for v in graph.adjDict[node]:
            if v not in visited:
                stack.append(v)
    reachable[source] = visited

"""
Convert the 2-CNF Formula F with n variables to a graph G.
G has 2n vertices. For each clause (l1 or l2) in F, there is an edge from
(i) -l1 to l2 (ii) -l2 to l1
"""
def formulaToGraph(F : Set[FrozenSet[int]],n : int) -> Graph:
    G : Graph = Graph()
    i : int
    for i in range(1,n+1):
        G.vertices.add(-i)
        G.vertices.add(i)
    C : FrozenSet[int]
    for C in F:
        literals : List[int] = list(C)
        l1 : int = literals[0]
        l2 : int = literals[1]
        G.adjDict[-l1].add(l2)
        G.adjDict[-l2].add(l1)
    return G

"""
Precondition: The 2-CNF Formula F is satisfiable.
Find and return a satisfying assignment for 2-CNF formula F with numVariables variables.
Idea: Construct a graph G from F. Run DFS to find the set of vertices reachable from each vertex.
Then iteratively assign T to literals v with no path from v to -v and to all literals reachable from v.
Satisying assignment = Set of variables which are assigned True.
"""
def find2SAT(F : Set[FrozenSet[int]], numVariables : int) -> Set[int]:
    # Convert formula to graph.
    G : Graph = formulaToGraph(F, numVariables)
    reachable : Dict[int, Set[int]]= defaultdict(set)
    
    # Perform DFS from each vertex to determine the set of reachable vertices.
    source : int
    for source in G.vertices:
        DFS(G, source, reachable)

    # The formula is SAT. Iteratively assign variables. All unassigned literals reside in leftLiterals.
    # Already true assigned variables live in trueVars.
    leftLiterals : Set[int] = G.vertices.copy()
    trueVars : Set[int] = set()
    while (len(leftLiterals) != 0):
        # Find an x with no path from x to -x
        x : int = None
        v : int
        for v in leftLiterals:
            if (-v) not in reachable[v]:
                x = v
                break
        # Assign true to literal x and all vertices reachable from it.
        # Note that every node is reachable from itself in our DFS implementation.
        l : int
        for l in reachable[x]:
            leftLiterals.discard(l)
            leftLiterals.discard(-l)
            if l>0:
                trueVars.add(l)
    return trueVars

"""
Check satisfiability of given 2-CNF Formula. Return True if SAT and False if UNSAT.
"""
def check2SAT(F : Set[FrozenSet[int]], numVariables : int) -> bool:
    # Convert formula to graph.
    G : Graph = formulaToGraph(F, numVariables)
    reachable : Dict[int, Set[int]]= defaultdict(set)
    
    # Perform DFS from each vertex to determine the set of reachable vertices.
    source : int
    for source in G.vertices:
        DFS(G, source, reachable)
    
    # If for any variable x there is a path from x to -x and from -x to x then the formula is UNSAT.
    v : int
    for v in G.vertices:
        if ((-v) in reachable[v]) and (v in reachable[-v]):
            return False
    # If no such v exists, the formula is SAT.
    return True

# Do not change the name of the function.
# Do not use global variables as we will run your code on multiple test cases.
#
def solve(inputString, n):
    (formula, numVariables, numClauses) = parseFormula(inputString)
    if n==1:
        if checkHorn(formula):
            return "already horn"
        else:
            return "not horn"
    elif n==2:
        G : Set[FrozenSet[int]] = convertFormula(formula)
        return formulaToString(G, numVariables, len(G), "2-CNF formula which is sat iff input is renamable Horn")
    elif n==3:
        if checkHorn(formula):
            return "already horn"
        G : Set[FrozenSet[int]] = convertFormula(formula)
        if check2SAT(G, numVariables):
            return "renamable"
        else:
            return "not renamable"
    elif n==4:
        if checkHorn(formula):
            return "already horn"
        G : Set[FrozenSet[int]] = convertFormula(formula)
        if not check2SAT(G, numVariables):
            return "not renamable"
        # Assignment = set of true variables.
        assignment : Set[int] = find2SAT(G, numVariables)
        output : str = " ".join(list(map(lambda x : str(x), sorted(assignment))))
        return output
    
    return "nil"


# Main function: do NOT change this.
if __name__=="__main__":
    inputFile = sys.argv[1]
    n = int(sys.argv[2])
    with open(inputFile, 'r') as f:
        inputString = f.read()
        print(solve(inputString, n))
