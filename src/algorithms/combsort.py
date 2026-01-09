def combsort(arr):
    n = len(arr) # puxa o tamanho do array
    gap = n # inicia o gap com o tamanho do array, o gap funciona como um "pulo" para comparar elementos mais distantes.
    shrink = 1.3 # fator de redução do gap
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1 # garante que o gap nunca seja menor que 1
            sorted = True
        
        i = 0
        while i + gap < n: # percorre o array comparando elementos distantes pelo gap
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False
            i += 1
            
    return arr
