
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) #precisei dessa porra para rodar na minha maquina, nao retirar por favor. meu python é fresco.


from algorithms.quicksort import quicksort
from algorithms.combsort import combsort
from utils.generator import generate_ascending, generate_descending, generate_random
from utils.benchmark import run_benchmark
import matplotlib.pyplot as plt


def main():
    sizes = [20000, 40000, 60000]
    algorithms = {
        "Quicksort": quicksort,
        "Combsort": combsort
    }
    generators = {
        "Crescente": generate_ascending,
        "Decrescente": generate_descending,
        "Aleatorio": generate_random
    }

    # Variaveis para armazenar os dados dos graficos
    results = {alg: {case: [] for case in generators} for alg in algorithms}

    for size in sizes:
        print(f"\n--- Tamanho: {size} elementos ---")
        for gen_name, gen_func in generators.items():
            print(f"\nCaso: {gen_name}")
            for alg_name, alg_func in algorithms.items():
                avg_time = run_benchmark(alg_func, gen_func, size)
                print(f"{alg_name}: {avg_time:.2f} ms")
                results[alg_name][gen_name].append(avg_time)

    # Exemplo de plotagem (um grafico para cada caso)
    for gen_name in generators:
        plt.figure()
        for alg_name in algorithms:
            plt.plot(sizes, results[alg_name][gen_name], marker='o', label=alg_name)
        plt.title(f"Tempo medio - Caso {gen_name}")
        plt.xlabel("Tamanho do vetor")
        plt.ylabel("Tempo (ms)")
        plt.legend()
        plt.grid(True)
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()
