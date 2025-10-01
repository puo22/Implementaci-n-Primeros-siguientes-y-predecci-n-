from collections import defaultdict

def compute_first(grammar):
    first = defaultdict(set)
    changed = True
    while changed:
        changed = False
        for A, prods in grammar.items():
            for prod in prods:
                add_epsilon = True
                for symbol in prod:
                    if symbol not in grammar:  # terminal
                        if symbol not in first[A]:
                            first[A].add(symbol)
                            changed = True
                        add_epsilon = False
                        break
                    else:  # nonterminal
                        before = len(first[A])
                        first[A] |= (first[symbol] - {"ε"})
                        if "ε" not in first[symbol]:
                            add_epsilon = False
                            break
                        if len(first[A]) > before:
                            changed = True
                if add_epsilon:
                    if "ε" not in first[A]:
                        first[A].add("ε")
                        changed = True
    return first
