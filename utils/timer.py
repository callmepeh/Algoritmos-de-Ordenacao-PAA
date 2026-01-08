#função simples usando o time.perf_conter para medir o tempo de execução de uma função de ordenação
import time

def measure_time(func, arr):
    start = time.perf_counter()
    result = func(arr.copy())
    end = time.perf_counter()
    return (end - start) * 1000, result  # retorna ms
