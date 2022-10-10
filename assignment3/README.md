# Renamable Horn Checker

Takes a CNF formula file F in DIMACS format as input.

- When n=1, outputs `already horn` if the formula is a Horn formula and `not horn` otherwise.
- When n=2, outputs a 2-CNF formula G (in DIMACS format) such that G is satisfiable if and only if F is renamable Horn.
- When n=3, outputs `already horn` if the formula is a Horn formula, otherwise `renamable` if it is renamable Horn and `not renamable` otherwise.
- When n=4, outputs `already horn` if the formula is a Horn formula, `not renamable` if it is not renamable. Otherwise, outputs a (space-separated) list of variables to be negated for F to become Horn.

Usage : `python assign3.py <FormulaFilePath> <n>`
