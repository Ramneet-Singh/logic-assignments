Convert CNF Formula F to a 2-CNF Formula G such that G is satisfiable if and only if F is a renameable Horn formula.

{{ 1,2,-1,-2 }}
convertFormula(F) := 
case F is
    {} => {}    
    {C} =>

convertClause(C):
1. If C={} then {}
2. If C is a horn-formula then {}
3. C has more than 1 positive literals, say they are x1,...,xn
4. We need to negate at least (n-1) of x1,...,xn.
5. For i from 1 to n:
    5a. Negate x1,...,x(i-1),x(i+1),...,xn
    5b. Move to the next clause. If success, return success. Else continue.
6. 

Formula F with variables x1,...,xn

Make a 2-CNF Formula G with variables y1,...,yn. Any model corresponds to a negation of some of the variables in F.
yi = 1 => xi has to be negated in the formula F. We will derive conditions on the negation which will ensure that the transformed formula is a Horn formula. If there is a model which satisfies these conditions, then the formula is renamable Horn, through negating exactly those variables xi which have yi=1.

convertFormula(F):
    G = {}
    For each clause C in F:
        S = convertClause(C)
        G = G union S
    return G

convertClause(C):
    S = {}
    For each pair i,j in C:
        if i<0 and j<0:
            # don't negate i or don't negate j
            S.insert( {i,j} )
        elif i<0 and j>0:
            # don't negate i or negate j
            S.insert( {i,j} )
        elif i>0 and j<0:
            # negate i or don't negate j
            S.insert( {i,j} )
        elif i>0 and j>0:
            # negate i or negate j
            S.insert( {i,j} )
    return S
