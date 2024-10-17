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

## Statystyka opisowa

Statystyka opisowa to dział statystyki, który zajmuje się opisem i podsumowaniem danych. Używa się jej do przedstawienia charakterystyki zbioru danych za pomocą tabel, wykresów i miar statystycznych, takich jak średnia, mediana, odchylenie standardowe itp.

**Wyobraź sobie:**

Masz wyniki testu z matematyki całej klasy. Statystyka opisowa pozwoli Ci na:

* **Uporządkowanie danych:** Możesz stworzyć tabelę z wynikami, posortować je rosnąco lub malejąco.
* **Obliczenie miar statystycznych:** Możesz obliczyć średnią ocenę, medianę, odchylenie standardowe, aby dowiedzieć się, jak  ogólnie  klasa napisała test i jak bardzo wyniki się różnią.
* **Wizualizację danych:** Możesz narysować histogram, aby zobaczyć rozkład ocen,  lub wykres pudełkowy, aby porównać wyniki  z  wynikami  innych klas.

**Podstawowe miary statystyczne:**

* **Miary tendencji centralnej:**  Średnia, mediana, moda –  pokazują,  wokół  jakiej  wartości  skupiają się dane.

  * Średnia to suma wszystkich wartości podzielona przez ich liczbę.
  * Mediana to wartość środkowa w uporządkowanym zbiorze danych. Jeśli zbiór ma parzystą liczbę elementów, mediana jest średnią arytmetyczną dwóch środkowych wartości.
  * Moda to wartość, która występuje najczęściej w zbiorze danych.

* **Miary rozproszenia:**  Odchylenie standardowe, wariancja, rozstęp –  pokazują, jak bardzo dane  są  rozrzucone.

  * Odchylenie standardowe to pierwiastek kwadratowy z wariancji. Jest to najczęściej używana miara rozproszenia. Im większe odchylenie standardowe, tym bardziej dane są rozrzucone.
  * Wariancja to średnia arytmetyczna kwadratów odchyleń od średniej. Jest to miara mniej intuicyjna niż odchylenie standardowe, ale ma pewne zastosowania w statystyce.
  * Rozstęp to różnica między największą a najmniejszą wartością w zbiorze danych. Jest to najprostsza miara rozproszenia, ale jest wrażliwa na wartości odstające.

* **Miary kształtu:**  Skośność, kurtoza –  opisują  kształt  rozkładu  danych.

  * Skośność mierzy asymetrię rozkładu.

    * Skośność dodatnia: Ogon rozkładu jest dłuższy po prawej stronie (więcej wartości po prawej stronie średniej).
    * Skośność ujemna: Ogon rozkładu jest dłuższy po lewej stronie (więcej wartości po lewej stronie średniej).
    * Skośność zerowa: Rozkład jest symetryczny.

  * Kurtoza mierzy "spiczastość" rozkładu.

    * Kurtoza dodatnia: Rozkład jest bardziej spiczasty niż rozkład normalny (więcej wartości skupionych wokół średniej i w ogonach).
    * Kurtoza ujemna: Rozkład jest bardziej płaski niż rozkład normalny (mniej wartości skupionych wokół średniej i w ogonach).
    * Kurtoza zerowa: Rozkład ma podobną spiczastość jak rozkład normalny.

**Zastosowania:**

Statystyka opisowa jest  używana  w  wielu  dziedzinach,  np.:

* **Biznes:**  Analiza  sprzedaży,  badania  rynku.
* **Nauka:**  Analiza  wyników  eksperymentów.
* **Medycyna:**  Analiza  danych  pacjentów.

```python
import numpy as np
from scipy import stats

# Przykładowe dane
dane = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Obliczenie średniej
srednia = np.mean(dane)
print(f"Średnia: {srednia}")

# Obliczenie mediany
mediana = np.median(dane)
print(f"Mediana: {mediana}")

# Obliczenie mody
moda = stats.mode(dane)

# Obliczenie odchylenia standardowego
odchylenie_std = np.std(dane)
print(f"Odchylenie standardowe: {odchylenie_std}")

# Przykładowe dane
dane = np.array([1, 2, 2, 3, 3, 3, 4, 4, 5, 10])

# Obliczenie skośności
skosnosc = stats.skew(dane)

# Obliczenie kurtozy
kurtoza = stats.kurtosis(dane)
```
