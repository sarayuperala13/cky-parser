import nltk
from nltk import CFG
from parser import CKYParser

grammar_cnf = CFG.fromstring("""
    S -> NP VP
    VP -> V NP | VP PP
    PP -> P NP
    NP -> Det N | NP PP | 'Barbie' | 'Tom'
    Det -> 'a' | 'the'
    N -> 'model' | 'pattern' | 'joke'
    V -> 'built' | 'spotted'
    P -> 'with'
""")

def run_demo():
    tokens = "Tom built a model with a pattern".split()
    print(f"Parsing Tokens: {tokens}\n" + "-"*40)

    parser = CKYParser(grammar_cnf)
    trees = parser.parse(tokens)

    if not trees:
        print("No valid parse tree found for the given input.")
        return

    print(f"Found {len(trees)} valid parse tree(s):\n")
    for idx, tree in enumerate(trees, 1):
        print(f"--- Parse Tree {idx} ---")
        tree.pretty_print()

if __name__ == "__main__":
    run_demo()
