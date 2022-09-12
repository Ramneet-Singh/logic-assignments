# Resolution Proof Checker

Usage: `python proof-checker.py <FormulaFilePath> <ProofFilePath>`

where
- `<FormulaFilePath>` is the path to a formula file in `DIMACS` format.
- `<ProofFilePath>` is the path to a proof file where each line is of the form `n[f/p] m[f/p] l1 l2 ... lk 0` denoting that clause at line `n` of `formula/proof` file has been resolved with clause at line `m` of `formula/proof` file to get clause `l1 l2 ... lk`.

# Test Cases

Formula File: `my-tests/formula.dat`
Formula: (!p1 or p3) and (p2 or !p3) and (p1 or p2 or p3) and (!p1 or !p2) and (!p2 or !p3) and (!p1 or !p3)

Correct Proof File 1: `my-tests/correct-proof1.dat`
Correct Proof File 2: `my-tests/correct-proof2.dat`
Incorrect Proof File: `my-tests/incorrect-proof.dat`
