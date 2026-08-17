# CKY Computational Linguistics Parser

An implementation of the **Cocke-Kasami-Younger (CKY)** dynamic programming algorithm from scratch in Python to parse Context-Free Grammars (CFG) in Chomsky Normal Form (CNF).

## Features
- **Algorithmic Mechanics**: Bottom-up chart parsing utilizing dynamic programming ($O(n^3 \cdot |G|)$ complexity).
- **Visualization**: Converts DP matrix paths directly into NLTK tree objects for terminal rendering.
- **Strict Verification**: Automatic grammar checks to ensure input adherence to Chomsky Normal Form rules.

## Setup & Running

```bash
# Clone Repository
git clone [https://github.com/sarayuperala13/cky-parser.git](https://github.com/sarayuperala13/cky-parser.git)
cd cky-parser

# Install Dependencies
pip install nltk

# Run Demo
python main.py
