import nltk
from nltk import Tree, CFG

class CKYParser:
    def __init__(self, grammar: CFG):
        self.grammar = grammar
        self._verify_cnf()

    def _verify_cnf(self):
        """Verifies if the loaded grammar adheres to Chomsky Normal Form."""
        for prod in self.grammar.productions():
            rhs = prod.rhs()
            if len(rhs) == 1 and not isinstance(rhs[0], str):
                raise ValueError(f"Grammar contains unit production: {prod}")
            elif len(rhs) > 2:
                raise ValueError(f"Grammar contains non-binary production: {prod}")

    def parse(self, tokens: list[str]) -> list[Tree]:
        """
        Executes the CKY dynamic programming parsing algorithm.
        Returns a list of valid NLTK Parse Trees.
        """
        n = len(tokens)
        if n == 0:
            return []

        # DP Table: table[row][col] stores sets of (NonTerminal, LeftChild, RightChild) or (NonTerminal, Word)
        table = [[[] for _ in range(n + 1)] for _ in range(n + 1)]

        # Phase 1: Terminal Rules (Base Diagonal)
        for i, word in enumerate(tokens):
            for prod in self.grammar.productions():
                if prod.rhs() == (word,):
                    # Store (LHS, word)
                    table[i][i + 1].append((prod.lhs(), word))

        # Phase 2: Non-Terminal Rules (Upper Triangle)
        for length in range(2, n + 1):  # Span length
            for i in range(0, n - length + 1):
                j = i + length
                for k in range(i + 1, j):  # Split point
                    for left in table[i][k]:
                        for right in table[k][j]:
                            left_sym = left[0]
                            right_sym = right[0]

                            for prod in self.grammar.productions():
                                if prod.rhs() == (left_sym, right_sym):
                                    table[i][j].append((prod.lhs(), left, right))

        # Phase 3: Construct NLTK Parse Trees from the Start Symbol (S)
        start_symbol = self.grammar.start()
        valid_parses = [node for node in table[0][n] if node[0] == start_symbol]

        return [self._build_nltk_tree(node) for node in valid_parses]

    def _build_nltk_tree(self, node) -> Tree:
        """Recursively transforms internal DP table nodes into NLTK Tree objects."""
        lhs = str(node[0])
        
        # Base case: Terminal node
        if len(node) == 2:
            return Tree(lhs, [node[1]])

        # Recursive case: Binary rule
        _, left_child, right_child = node
        return Tree(lhs, [self._build_nltk_tree(left_child), self._build_nltk_tree(right_child)])
