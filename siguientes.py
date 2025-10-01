from collections import defaultdict

def compute_follow(grammar, first, start_symbol):
    follow = defaultdict(set)
    follow[start_symbol].add("$")
    changed = True
    while changed:
        changed = False
        for A, prods in grammar.items():
            for prod in prods:
                for i, B in enumerate(prod):
                    if B in grammar:
                        beta = prod[i+1:]
                        if beta:
                            beta_first = set()
                            add_follow_A = True
                            for symbol in beta:
                                if symbol in grammar:
                                    beta_first |= (first[symbol] - {"ε"})
                                    if "ε" in first[symbol]:
                                        continue
                                    else:
                                        add_follow_A = False
                                        break
                                else:
                                    beta_first.add(symbol)
                                    add_follow_A = False
                                    break
                            if beta_first - follow[B]:
                                follow[B] |= beta_first
                                changed = True
                            if add_follow_A:
                                if follow[A] - follow[B]:
                                    follow[B] |= follow[A]
                                    changed = True
                        else:
                            if follow[A] - follow[B]:
                                follow[B] |= follow[A]
                                changed = True
    return follow
