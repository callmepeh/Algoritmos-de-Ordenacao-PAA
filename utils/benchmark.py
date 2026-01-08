from utils.timer import measure_time

def run_benchmark(algorithm, data_func, n, repetitions=5):
    times = []
    for _ in range(repetitions):
        arr = data_func(n)
        t, _ = measure_time(algorithm, arr)
        times.append(t)
    return sum(times) / len(times)

# Função para rodar benchmarks em algoritmos de ordenação, ela testa 5 vezes e retorna a média