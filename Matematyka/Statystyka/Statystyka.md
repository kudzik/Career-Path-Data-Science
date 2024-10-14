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

### Odchylenie standardowe — wyjaśnienie

**Odchylenie standardowe** to statystyczna miara, która opisuje, jak bardzo wartości w zbiorze danych różnią się od średniej (średniej arytmetycznej). Mówiąc prościej, odchylenie standardowe wskazuje, jak bardzo dane są rozproszone lub rozciągnięte wokół średniej wartości.

* **Niskie odchylenie standardowe** oznacza, że większość wartości jest blisko średniej.
* **Wysokie odchylenie standardowe** wskazuje, że dane są bardziej rozproszone i wartości różnią się znacznie od średniej.

### Kroki do obliczenia odchylenia standardowego

Przejdźmy przez proces obliczania odchylenia standardowego krok po kroku, aby było to jasne.

1. **Oblicz średnią (średnią arytmetyczną)** zbioru danych.
2. **Znajdź różnicę** między każdą wartością a średnią.
3. **Podnieś do kwadratu** każdą z tych różnic.
4. **Oblicz średnią** z kwadratów różnic (to nazywamy **wariancją**).
5. **Znajdź pierwiastek kwadratowy** z wariancji — to jest odchylenie standardowe.

### Przykład obliczenia odchylenia standardowego

Weźmy przykład zbioru danych: **2, 4, 4, 4, 5, 5, 7, 9**

1. **Oblicz średnią**:
   * \( \text{Średnia} = \frac{2 + 4 + 4 + 4 + 5 + 5 + 7 + 9}{8} = 5 \)

2. **Oblicz różnice** między każdą wartością a średnią:
   * \( 2 - 5 = -3 \)
   * \( 4 - 5 = -1 \)
   * \( 4 - 5 = -1 \)
   * \( 4 - 5 = -1 \)
   * \( 5 - 5 = 0 \)
   * \( 5 - 5 = 0 \)
   * \( 7 - 5 = 2 \)
   * \( 9 - 5 = 4 \)

3. **Podnieś do kwadratu** każdą różnicę:
   * \( (-3)^2 = 9 \)
   * \( (-1)^2 = 1 \)
   * \( (-1)^2 = 1 \)
   * \( (-1)^2 = 1 \)
   * \( 0^2 = 0 \)
   * \( 0^2 = 0 \)
   * \( 2^2 = 4 \)
   * \( 4^2 = 16 \)

4. **Oblicz wariancję** (średnią z kwadratów różnic):
   * \( \text{Wariancja} = \frac{9 + 1 + 1 + 1 + 0 + 0 + 4 + 16}{8} = \frac{32}{8} = 4 \)

5. **Oblicz odchylenie standardowe** (pierwiastek kwadratowy z wariancji):
   * \( \text{Odchylenie standardowe} = \sqrt{4} = 2 \)

### Interpretacja wyniku

Odchylenie standardowe wynosi **2**, co oznacza, że większość wartości w zbiorze danych różni się od średniej o około 2 jednostki.

### Podsumowanie

Odchylenie standardowe to miara, która pomaga zrozumieć, jak bardzo dane są rozproszone wokół średniej. Jest użyteczna w statystyce, gdy chcesz zrozumieć zmienność i niejednorodność danych.

Jeśli potrzebujesz dalszych wyjaśnień lub dodatkowych przykładów, daj mi znać! 😊
