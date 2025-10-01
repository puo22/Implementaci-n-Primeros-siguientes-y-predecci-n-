#!/usr/bin/env python3
from utils import load_grammar_from_txt
from primeros import compute_first
from siguientes import compute_follow
from prediccion import compute_pred

def run_analysis(file_path, start_symbol="S"):
    try:
        grammar = load_grammar_from_txt(file_path)
    except FileNotFoundError:
        print(f"Error: archivo '{file_path}' no encontrado.")
        return
    except Exception as e:
        print(f"Error leyendo '{file_path}': {e}")
        return

    print(f"\n=== Analizando: {file_path} ===\n")
    print("GRAMÁTICA:")
    for A, prods in grammar.items():
        for p in prods:
            print(f"  {A} -> {' '.join(p)}")

    first = compute_first(grammar)
    print("\nFIRST:")
    for nt in sorted(first.keys()):
        print(f"FIRST({nt}) = {sorted(first[nt])}")

    follow = compute_follow(grammar, first, start_symbol)
    print("\nFOLLOW:")
    for nt in sorted(follow.keys()):
        print(f"FOLLOW({nt}) = {sorted(follow[nt])}")

    pred = compute_pred(grammar, first, follow)
    print("\nPRED:")
    for A in sorted(pred.keys()):
        for i in sorted(pred[A].keys()):
            rhs = ' '.join(grammar[A][i])
            print(f"PRED({A} -> {rhs}) = {sorted(pred[A][i])}")
    print("\n" + "="*50 + "\n")

def main():
    print("Ingrese el/los archivos .txt a analizar (uno por línea).")
    print("Presione Ctrl+D cuando termine.\n")
    try:
        while True:
            file_path = input("Archivo: ").strip()
            if not file_path:
                continue
            run_analysis(file_path, "S")
    except EOFError:
        print("\nFin de entrada. Programa terminado.")



main()
