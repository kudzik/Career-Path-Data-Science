# Macierze

## Wyznacznik macierzy

```text
|a| lub det(A)
```

Wyznacznik macierzy to bardzo ważne pojęcie w algebrze liniowej. Można o nim myśleć jak o specjalnej liczbie, którą obliczamy dla macierzy kwadratowej (czyli takiej, która ma tyle samo wierszy co kolumn). Ta liczba mówi nam wiele o właściwościach macierzy, np. czy jest odwracalna, czy układ równań liniowych reprezentowany przez tę macierz ma jednoznaczne rozwiązanie, a także  jak bardzo przekształcenie liniowe reprezentowane przez tę macierz "rozciąga" lub "ściska" przestrzeń.

**Jak obliczyć wyznacznik?**

Sposób obliczania wyznacznika zależy od rozmiaru macierzy. Dla małych macierzy (2x2, 3x3) istnieją proste wzory.

* **Macierz 2x2:**

   ```text
   A = [[a, b],
        [c, d]]

   det(A) = a*d - b*c
   ```

* **Macierz 3x3:**  (metoda Sarrusa)

   ```
   A = [[a, b, c],
        [d, e, f],
        [g, h, i]]

   det(A) = a*e*i + b*f*g + c*d*h - c*e*g - b*d*i - a*f*h
   ```

Dla większych macierzy obliczenia są bardziej skomplikowane i często stosuje się metody rekurencyjne, takie jak rozwinięcie Laplace'a.

**Do czego przydaje się wyznacznik?**

Wyznacznik ma wiele zastosowań w matematyce, fizyce i informatyce, m.in.:

* **Rozwiązywanie układów równań liniowych:**  Jeśli wyznacznik macierzy współczynników układu równań jest różny od zera, to układ ma jednoznaczne rozwiązanie.
* **Odwracanie macierzy:** Macierz jest odwracalna tylko wtedy, gdy jej wyznacznik jest różny od zera.
* **Geometria:** Wyznacznik macierzy przekształcenia liniowego mówi nam o tym, jak to przekształcenie zmienia objętość figur geometrycznych.
* **Analiza danych:** Wyznacznik jest używany w niektórych metodach analizy danych, np. do analizy głównych składowych (PCA).

**Wyznacznik w NumPy:**

W NumPy możemy obliczyć wyznacznik macierzy za pomocą funkcji `np.linalg.det()`:

```python
import numpy as np

A = np.array([[1, 2], [3, 4]])
det_A = np.linalg.det(A)
print(det_A)  # Wynik: -2.0
```
