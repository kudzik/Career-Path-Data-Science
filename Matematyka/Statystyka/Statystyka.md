# Statystyka

## Mediana

### Mediana — co to jest?

**Mediana** to wartość, która dzieli uporządkowany zbiór liczb na dwie równe części. Połowa liczb w zbiorze jest mniejsza lub równa medianie, a druga połowa jest większa lub równa medianie. W skrócie, mediana to środkowa wartość w zbiorze danych.

Mediana jest bardziej odporna na wartości odstające (skrajne wartości) niż średnia, co sprawia, że jest dobrym miernikiem, gdy w danych są bardzo duże lub małe liczby.

### Jak obliczyć medianę?

Obliczanie mediany zależy od tego, czy liczba elementów w zbiorze jest parzysta, czy nieparzysta.

1. **Dla zbioru z nieparzystą liczbą elementów**:
   * Posortuj liczby rosnąco.
   * Wybierz środkową wartość.

2. **Dla zbioru z parzystą liczbą elementów**:
   * Posortuj liczby rosnąco.
   * Mediana to średnia arytmetyczna dwóch środkowych wartości.

### Przykłady

#### Przykład z nieparzystą liczbą elementów

Załóżmy, że mamy zbiór liczb: 3, 1, 9, 4, 7.

1. Sortujemy zbiór: 1, 3, 4, 7, 9.
2. Mediana to środkowa wartość, czyli **4**.

#### Przykład z parzystą liczbą elementów

Weźmy zbiór: 8, 3, 7, 5.

1. Sortujemy zbiór: 3, 5, 7, 8.
2. Środkowe wartości to 5 i 7.
3. Mediana to średnia z tych liczb: \( \frac{5 + 7}{2} = 6 \).

### Podsumowanie

Mediana to sposób na określenie centralnej wartości w zbiorze danych. Jest szczególnie użyteczna, gdy chcesz uniknąć wpływu wartości skrajnych na analizę danych.

## Odchylenie standardowe

Aby lepiej zrozumieć odchylenie standardowe, najpierw zdefiniuję to pojęcie i przedstawię przykład obliczenia odchylenia standardowego dla prostego zestawu danych. Następnie pokażę, jak obliczyć odchylenie standardowe w NumPy.

```python?code_reference&code_event_index=3
import numpy as np

# Przykładowa tablica
dane = np.array([2, 4, 6, 8, 10])

# Obliczenie średniej
srednia = np.mean(dane)

# Obliczenie wariancji
wariancja = np.var(dane)

# Obliczenie odchylenia standardowego
odchylenie_std = np.std(dane)

# Wyświetlenie wyników
print("Dane:", dane)
print("Średnia:", srednia)
print("Wariancja:", wariancja)
print("Odchylenie standardowe:", odchylenie_std)
```

```text?code_stdout&code_event_index=3
Dane: [ 2  4  6  8 10]
Średnia: 6.0
Wariancja: 8.0
Odchylenie standardowe: 2.8284271247461903

```

Odchylenie standardowe to miara rozproszenia danych wokół średniej. Im większe odchylenie standardowe, tym bardziej rozproszone są dane.

**Przykład:**

Załóżmy, że mamy zestaw danych: 2, 4, 6, 8, 10.

1. **Obliczenie średniej:**
   Średnia arytmetyczna to suma wszystkich wartości podzielona przez ich liczbę: (2 + 4 + 6 + 8 + 10) / 5 = 6

2. **Obliczenie wariancji:**
   Wariancja to średnia arytmetyczna kwadratów odchyleń od średniej:
   [(2-6)<sup>2</sup> + (4-6)<sup>2</sup> + (6-6)<sup>2</sup> + (8-6)<sup>2</sup> + (10-6)<sup>2</sup>] / 5 = 8

3. **Obliczenie odchylenia standardowego:**
   Odchylenie standardowe to pierwiastek kwadratowy z wariancji: √8 ≈ 2.83

**Obliczanie odchylenia standardowego w NumPy:**

W NumPy możemy obliczyć odchylenie standardowe za pomocą funkcji `np.std()`:

```python
import numpy as np

dane = np.array([2, 4, 6, 8, 10])
odchylenie_std = np.std(dane)
print(odchylenie_std)  # Wynik: 2.8284271247461903
```

**Podsumowanie:**

Odchylenie standardowe to ważna miara statystyczna, która informuje nas o tym, jak bardzo dane są rozproszone wokół średniej. NumPy udostępnia funkcję `np.std()`, która pozwala na łatwe obliczenie odchylenia standardowego dla tablic NumPy.
