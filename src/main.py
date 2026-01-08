from algorithms.quicksort import quicksort
from algorithms.combsort import combsort
from utils.generator import generate_ascending, generate_descending, generate_random
from utils.benchmark import run_benchmark

def main():
    sizes = [20000, 40000, 60000]
    algorithms = {
        "Quicksort": quicksort,
        "Combsort": combsort
    }
    generators = {
        "Crescente": generate_ascending,
        "Decrescente": generate_descending,
        "Aleatório": generate_random
    }
    
    for size in sizes:
        print(f"\n--- Tamanho: {size} elementos ---")
        for gen_name, gen_func in generators.items():
            print(f"\nCaso: {gen_name}")
            for alg_name, alg_func in algorithms.items():
                avg_time = run_benchmark(alg_func, gen_func, size)
                print(f"{alg_name}: {avg_time:.2f} ms")

if __name__ == "__main__":
    main()
# Função principal para rodar os benchmarks dos algoritmos de ordenação com diferentes tipos de dados