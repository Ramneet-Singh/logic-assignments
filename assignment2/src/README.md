# Proof Filler

Usage: `python prover.py <FormulaFilePath> <IncompleteProofFilePath> <OutputProofFilePath>`

Where
    - `<FormulaFilePath>` is the path to a CNF Formula File in `DIMACS` format.
    - `<IncompleteProofFilePath>` is the path to an incomplete proof file with lines of the form `n[f/p] m[f/p]` and sometimes `n[f/p] ??` or `?? m[f/p]`.
    - `<OutputProofFilePath>` is the path where the completed proof file will be output.

Assumption: Once the clauses have been identified, the resolvent is unique, i.e., two given clauses can only ever result in a unique resolvent in any proof.
