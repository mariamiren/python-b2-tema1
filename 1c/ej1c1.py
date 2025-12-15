"""
Enunciado:
Implementa y compara el rendimiento de dos algoritmos de ordenamiento clásicos con Quicksort y Mergesort, en Python.

Funciones a desarrollar:
- `quicksort(arr: List[int]) -> List[int]`:
    Descripción:
    Ordena una lista de números enteros utilizando el algoritmo Quicksort, dividiendo la lista en subconjuntos menores,
    mayores o iguales a un elemento pivote, y luego ordenando esos subconjuntos recursivamente.
    Parámetros:
        - `arr` (List[int]): Lista de números enteros a ordenar.

- `mergesort(arr: List[int]) -> List[int]`:
    Descripción:
    Ordena una lista de números enteros utilizando el algoritmo Mergesort, dividiendo la lista en mitades hasta obtener
    subconjuntos que se consideran ordenados, para luego mezclar esos subconjuntos de manera ordenada.
    Parámetros:
        - `arr` (List[int]): Lista de números enteros a ordenar.

- `merge(left: List[int], right: List[int]) -> List[int]`:
    Descripción:
    Función auxiliar para el Mergesort que mezcla dos sublistas ordenadas en una sola lista ordenada.
    Parámetros:
        - `left` (List[int]): Sublista izquierda ordenada.
        - `right` (List[int]): Sublista derecha ordenada.

Ejemplo:
    start = time.time()
    sorted_array_quicksort = quicksort(test_array.copy())
    end_time = time.time() - start
    print(f"Quicksort on {size} elements took: {end_time:.5f} seconds.")
    print("First 10 elements after Quicksort:", sorted_array_quicksort[:10])

Salida esperada:
- Demostración del proceso de ordenación de una lista de números enteros con Quicksort y Mergesort, incluyendo la
visualización del tiempo que cada algoritmo toma para ordenar la misma lista.
"""

import random
import time
from typing import List
from ej1c1 import quicksort
@pytest.mark.parametrize("test_imput, expected, message", [
    ([], [], "Quicksort should return an empty list when the input is empty."), 
    ([1], [1], "Quicksort shoyld return a single-element list unchanged."), 
    ([2, 1], [1, 2], "Quicksort should correctly sort a list of two elements."),
    ([3, 1, 2], [1, 2, 3], "Quicksort should correctly sort a list of three elements."),
    ([9, 3, 5, 1, 4, 2, 6, 8, 7], [1, 2, 3, 4, 5, 6, 7, 8, 9], "Quicksort should correctly sort of multiple elements."),
    (list(range(10, 0, -1)), list range(1, 11)), "Quicksort should correctly sort a list in descendind order.")
])
    
def quicksort(test_input, expected, message): 
   assert quicksort(test_input) == expected, message 

@pytest.mark.parametrize("test_input,expected,message", [
    ([], [], "Mergesort should return an empty list when the input is empty."), 
    ([1], [1], "Mergesort shoyld return a single-element list unchanged."), 
    ([2, 1], [1, 2], "Mergesort should correctly sort a list of two elements."),
    ([3, 1, 2], [1, 2, 3], "Mergesort should correctly sort a list of three elements."),
    ([9, 3, 5, 1, 4, 2, 6, 8, 7], [1, 2, 3, 4, 5, 6, 7, 8, 9], "Mergesort should correctly sort of multiple elements."),
    (list(range(10, 0, -1)), list range(1, 11)), "Mergesort should correctly sort a list in descendind order.")
])
def test_mergesort(test_input, expected, message):
    assert mergesort(test_input) == expected, message

@pytest.mark.parametrize("left,rigth,expected,message", [
    ([1], [2], [1, 2] "Merge should correctly combine two single-element list."), 
    ([2, 3], [1], [1, 2, 3]"Merge should place all elements from second list."), 
    ([1, 3], [2, 4], [1, 2, 3, 4] "Merge should interleave elements form both list."),
    ([], [1, 2, 3], [1, 2, 3] "Merge should resturn the non-empty list when one list is empty."),
    ([1, 2, 3], [], [1, 2, 3], "Merge should return the non-empty list when the other list is empty."),
    test_merge(left, rigth, expected, message):
    assert merge(left, rigth) == expected, message


# Para probar el código, descomenta las siguientes líneas
# if __name__ == "__main__":
#     sizes = [100]  
#     for size in sizes:
#         test_array = [random.randint(1, 100) for _ in range(size)]
        
#         print(f"\nOriginal array (first 10 elements of {size}):")
#         print(test_array[:10])  
        
#         start = time.time()
#         sorted_array_quicksort = quicksort(test_array.copy())
#         end_time = time.time() - start
#         print(f"Quicksort on {size} elements took: {end_time:.5f} seconds.")
#         print("First 10 elements after Quicksort:", sorted_array_quicksort[:10])
        
#         start = time.time()
#         sorted_array_mergesort = mergesort(test_array.copy())
#         end_time = time.time() - start
#         print(f"Mergesort on {size} elements took: {end_time:.5f} seconds.")
#         print("First 10 elements after Mergesort:", sorted_array_mergesort[:10])
