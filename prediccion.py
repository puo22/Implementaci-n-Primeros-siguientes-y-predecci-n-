from collections import defaultdict

def compute_pred(grammar, first, follow):
    pred = defaultdict(dict)
    for A, prods in grammar.items():
        for i, prod in enumerate(prods):
            symbols_first = set()
            if prod == ["ε"]:
                symbols_first |= follow[A]
            else:
                add_nullable = True
                for symbol in prod:
                    if symbol in grammar:
                        symbols_first |= (first[symbol] - {"ε"})
                        if "ε" not in first[symbol]:
                            add_nullable = False
                            break
                    else:
                        symbols_first.add(symbol)
                        add_nullable = False
                        break
                if add_nullable:
                    symbols_first |= follow[A]
            pred[A][i] = symbols_first
    return pred
