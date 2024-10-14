# Numpy

## Funkcja `size` w NumPy

Funkcja `size` w NumPy jest niezwykle przydatna, szczególnie gdy pracujesz z tablicami o różnych kształtach i rozmiarach.

### Co robi funkcja `size`?

W skrócie, funkcja `size` zwraca całkowitą liczbę elementów w tablicy NumPy. Mówiąc prościej, informuje nas, ile "komórek" zawiera nasza tablica.

### Przykład z życia

Wyobraź sobie, że masz pudełko czekoladek ułożonych w rzędach i kolumnach. Funkcja `size` powiedziałaby Ci, ile dokładnie czekoladek znajduje się w tym pudełku, niezależnie od tego, jak są ułożone.

### Jak używać funkcji `size`?

To bardzo proste! Wystarczy wywołać funkcję `size` na danej tablicy NumPy:

```python
import numpy as np

tablica = np.array([[1, 2, 3], [4, 5, 6]])
rozmiar = np.size(tablica)
print(rozmiar)  # Wynik: 6
```

### Co jeszcze warto wiedzieć?

* Funkcja `size` działa zarówno na tablicach jedno-, jak i wielowymiarowych.
* Możesz również użyć atrybutu `size` bezpośrednio na tablicy NumPy, aby uzyskać ten sam wynik: `tablica.size`.
* Jeśli chcesz poznać liczbę elementów wzdłuż konkretnej osi (np. liczbę wierszy lub kolumn), możesz użyć argumentu `axis` w funkcji `size`.

## Funkcja `shape` w NumPy

Funkcja `shape` w NumPy to kolejne niezwykle przydatne narzędzie, które pozwala nam poznać "kształt" naszej tablicy, czyli jej wymiary.

### Co robi funkcja `shape`?

Funkcja `shape` zwraca krotkę (tuple), której elementy reprezentują liczbę elementów wzdłuż każdej osi tablicy. Innymi słowy, mówi nam, ile wierszy, kolumn (i ewentualnie dodatkowych wymiarów) ma nasza tablica.

### Przykład z życia

Wyobraź sobie, że masz szachownicę. Funkcja `shape` powiedziałaby Ci, że ma ona 8 wierszy i 8 kolumn, czyli jej kształt to (8, 8).

### Jak używać funkcji `shape`?

To bardzo proste! Wystarczy wywołać funkcję `shape` na danej tablicy NumPy lub odwołać się do atrybutu `shape` tej tablicy:

```python
import numpy as np

tablica = np.array([[1, 2, 3], [4, 5, 6]])
kształt = np.shape(tablica)
print(kształt)  # Wynik: (2, 3)

# Można też użyć atrybutu shape
kształt2 = tablica.shape
print(kształt2)  # Wynik: (2, 3)
```

W tym przykładzie stworzyliśmy tablicę dwuwymiarową o dwóch wierszach i trzech kolumnach. Funkcja `shape` (lub atrybut `shape`) zwróciła krotkę (2, 3), co oznacza, że tablica ma 2 wiersze i 3 kolumny.

### Co jeszcze warto wiedzieć?

* Dla tablic jednowymiarowych `shape` zwraca krotkę z jednym elementem, np. (5,) dla tablicy o 5 elementach.
* Możesz użyć `shape` do zmiany kształtu tablicy "w miejscu" (in-place), przypisując nową krotkę do atrybutu `shape`. Pamiętaj jednak, że liczba elementów w tablicy musi pozostać taka sama.

## Atrybut `dtype` w NumPy

Atrybut `dtype` w NumPy to kluczowy element, który określa typ danych przechowywanych w tablicy. To jak etykieta na pudełku, która mówi nam, co znajduje się w środku.

### Co robi atrybut `dtype`?

Atrybut `dtype` informuje nas o typie danych każdego elementu w tablicy NumPy. Może to być liczba całkowita (`int`), liczba zmiennoprzecinkowa (`float`), wartość logiczna (`bool`) lub inny typ danych.

### Przykład z życia

Wyobraź sobie, że masz kilka pudełek. Na jednym jest napisane "owoce", na drugim "warzywa", a na trzecim "słodycze". Atrybut `dtype` jest jak te napisy - mówi nam, jakiego rodzaju dane przechowujemy w tablicy NumPy.

### Jak używać atrybutu `dtype`?

Możesz sprawdzić typ danych tablicy, odwołując się do jej atrybutu `dtype`:

```python
import numpy as np

tablica_int = np.array([1, 2, 3])
tablica_float = np.array([1.5, 2.7, 3.14])

print(tablica_int.dtype)  # Wynik: int32 (lub int64, w zależności od systemu)
print(tablica_float.dtype)  # Wynik: float64
```

Możesz również określić typ danych podczas tworzenia tablicy, używając argumentu `dtype`:

```python
tablica_bool = np.array([True, False, True], dtype=bool)
print(tablica_bool.dtype)  # Wynik: bool
```

### Co jeszcze warto wiedzieć?

* NumPy oferuje wiele różnych typów danych, takich jak `int8`, `int16`, `int32`, `int64`, `float16`, `float32`, `float64`, `complex64`, `complex128`, `bool`, `string_`, `object` i inne.
* Wybór odpowiedniego typu danych może mieć wpływ na wydajność obliczeń i ilość zajmowanej pamięci.
* Możesz zmienić typ danych istniejącej tablicy za pomocą metody `astype()`.

## Budowanie Tablic

1. `np.array()`

   * To najbardziej podstawowa funkcja do tworzenia tablic NumPy. Przyjmuje jako argument listę lub krotkę Pythona i zwraca tablicę NumPy zawierającą te same dane.

   * Przykład:

   ```python
   import numpy as np

   lista = [1, 2, 3, 4]
   tablica = np.array(lista)
   print(tablica)  # Wynik: [1 2 3 4]
   ```

2. `np.zeros()` i `np.ones()`

   * Te funkcje tworzą tablice wypełnione odpowiednio zerami lub jedynkami. Jako argument przyjmują kształt tablicy (krotkę określającą wymiary).

   * Przykład:

   ```python
   import numpy as np

   tablica_zer = np.zeros((2, 3))  # Tablica 2x3 wypełniona zerami
   tablica_jedynek = np.ones((4, 1))  # Tablica 4x1 wypełniona jedynkami

   print(tablica_zer)
   print(tablica_jedynek)
   ```

3. `np.full()`

   * Ta funkcja tworzy tablicę wypełnioną określoną wartością. Jako argumenty przyjmuje kształt tablicy oraz wartość, którą chcemy wypełnić tablicę.

   * Przykład:

   ```python
   import numpy as np

   tablica_pelna = np.full((3, 2), 5)  # Tablica 3x2 wypełniona piątkami
   print(tablica_pelna)
   ```

4. `np.arange()`

   * Ta funkcja tworzy tablicę jednowymiarową zawierającą sekwencję liczb równomiernie rozmieszczonych w określonym zakresie. Jako argumenty przyjmuje wartość początkową, końcową oraz krok (opcjonalnie).

   * Przykład:

   ```python
   import numpy as np

   tablica_sekwencja = np.arange(0, 10, 2)  # Liczby od 0 do 10 (bez 10) z krokiem 2
   print(tablica_sekwencja)  # Wynik: [0 2 4 6 8]
   ```

5. `np.linspace()`

   * Ta funkcja tworzy tablicę jednowymiarową zawierającą określoną liczbę elementów równomiernie rozmieszczonych w określonym zakresie. Jako argumenty przyjmuje wartość początkową, końcową oraz liczbę elementów.

   * Przykład:

   ```python
   import numpy as np

   tablica_liniowa = np.linspace(0, 1, 5)  # 5 liczb równomiernie rozmieszczonych od 0 do 1 (włącznie)
   print(tablica_liniowa) 
   ```

## Podstawowe operacje na tablicach

Jasne, dodam te operacje do listy. Rozumiem, że chcesz poznać podstawowe operacje arytmetyczne na tablicach NumPy, takie jak dodawanie, odejmowanie, mnożenie i dzielenie elementów.

```python
import numpy as np

# Tworzymy dwie tablice NumPy
tablica1 = np.array([[1, 2, 3], [4, 5, 6]])
tablica2 = np.array([[7, 8, 9], [10, 11, 12]])

# Dodawanie tablic
suma = tablica1 + tablica2

# Odejmowanie tablic
roznica = tablica1 - tablica2

# Mnożenie tablic
iloczyn = tablica1 * tablica2

# Dzielenie tablic
iloraz = tablica1 / tablica2

# Wyświetlamy wyniki
print("Suma:\n", suma)
print("Różnica:\n", roznica)
print("Iloczyn:\n", iloczyn)
print("Iloraz:\n", iloraz)
```

```python
Suma:
 [[ 8 10 12]
 [14 16 18]]
Różnica:
 [[-6 -6 -6]
 [-6 -6 -6]]
Iloczyn:
 [[ 7 16 27]
 [40 55 72]]
Iloraz:
 [[0.14285714 0.25       0.33333333]
 [0.4        0.45454545 0.5       ]]

```

## Podstawowe operacje arytmetyczne na tablicach NumPy

NumPy ułatwia wykonywanie podstawowych operacji arytmetycznych na tablicach, takich jak dodawanie, odejmowanie, mnożenie i dzielenie elementów. Oto jak to działa:

### Dodawanie elementów

```python
import numpy as np

# Tworzymy dwie tablice NumPy
tablica1 = np.array([[1, 2, 3], [4, 5, 6]])
tablica2 = np.array([[7, 8, 9], [10, 11, 12]])

# Dodawanie tablic
suma = tablica1 + tablica2

# Wyświetlamy wynik
print("Suma:\n", suma)
```

Wynik:

```python
Suma:
 [[ 8 10 12]
 [14 16 18]]
```

### Odejmowanie elementów

```python
# Odejmowanie tablic
roznica = tablica1 - tablica2

# Wyświetlamy wynik
print("Różnica:\n", roznica)
```

Wynik:

```python
Różnica:
 [[-6 -6 -6]
 [-6 -6 -6]]
```

### Mnożenie elementów

```python
# Mnożenie tablic
iloczyn = tablica1 * tablica2

# Wyświetlamy wynik
print("Iloczyn:\n", iloczyn)
```

Wynik:

```
Iloczyn:
 [[ 7 16 27]
 [40 55 72]]
```

### Dzielenie elementów

```python
# Dzielenie tablic
iloraz = tablica1 / tablica2

# Wyświetlamy wynik
print("Iloraz:\n", iloraz)
```

Wynik:

```python
Iloraz:
 [[0.14285714 0.25       0.33333333]
 [0.4        0.45454545 0.5       ]]
```

**Ważne:**

* Operacje arytmetyczne w NumPy są wykonywane element po elemencie.
* Tablice muszą mieć ten sam kształt, aby można było na nich wykonywać operacje arytmetyczne (chyba że używamy broadcastingu).
* Dzielenie przez zero spowoduje błąd.

### Mnożenie macierzy - matematyka i NumPy

Mnożenie macierzy to operacja, która łączy dwie macierze, aby utworzyć trzecią.  Ma ona specyficzne zasady i jest szeroko stosowana w różnych dziedzinach, od grafiki komputerowej po uczenie maszynowe.

### Mnożenie macierzy w matematyce

Aby pomnożyć dwie macierze, **liczba kolumn w pierwszej macierzy musi być równa liczbie wierszy w drugiej macierzy.** Wynikiem mnożenia jest nowa macierz, której liczba wierszy jest taka sama jak w pierwszej macierzy, a liczba kolumn taka sama jak w drugiej.

**Przykład:**

Załóżmy, że mamy macierz A (2x3) i macierz B (3x2):

```
A = [[1, 2, 3],
     [4, 5, 6]]

B = [[7, 8],
     [9, 10],
     [11, 12]]
```

Wynikiem mnożenia A x B będzie macierz C (2x2):

```
C = [[1*7 + 2*9 + 3*11, 1*8 + 2*10 + 3*12],
     [4*7 + 5*9 + 6*11, 4*8 + 5*10 + 6*12]]

C = [[58, 64],
     [139, 154]]
```

Każdy element w macierzy C jest obliczony jako suma iloczynów elementów z odpowiedniego wiersza macierzy A i odpowiedniej kolumny macierzy B.

### Mnożenie macierzy w NumPy

NumPy udostępnia kilka sposobów mnożenia macierzy:

1. **Funkcja `np.dot()`:**

   ```python
   import numpy as np

   A = np.array([[1, 2, 3], [4, 5, 6]])
   B = np.array([[7, 8], [9, 10], [11, 12]])
   C = np.dot(A, B)
   print(C)
   ```

2. **Operator `@`:**

   ```python
   import numpy as np

   A = np.array([[1, 2, 3], [4, 5, 6]])
   B = np.array([[7, 8], [9, 10], [11, 12]])
   C = A @ B
   print(C)
   ```

Oba sposoby dają ten sam wynik:

```
[[ 58  64]
 [139 154]]
```

**Ważne:**

* Mnożenie macierzy **nie jest przemienne**, tzn. A x B zazwyczaj nie jest równe B x A.
* NumPy oferuje również funkcje do innych operacji na macierzach, takich jak transpozycja, obliczanie wyznacznika, odwracanie macierzy itp.

## Macierz transponowana

Transpozycja macierzy to operacja, która polega na **zamianie wierszy na kolumny i kolumn na wiersze**. Innymi słowy, "obracamy" macierz wokół jej głównej przekątnej.

**Przykład:**

Załóżmy, że mamy macierz A:

```python
A = [[1, 2, 3],
     [4, 5, 6]]
```

Macierz transponowana A<sup>T</sup> będzie wyglądać tak:

```
A<sup>T</sup> = [[1, 4],
         [2, 5],
         [3, 6]]
```

Jak widzisz, pierwszy wiersz macierzy A stał się pierwszą kolumną macierzy A<sup>T</sup>, drugi wiersz macierzy A stał się drugą kolumną macierzy A<sup>T</sup>, itd.

**Własności macierzy transponowanej:**

* **(A<sup>T</sup>)<sup>T</sup> = A:** Transpozycja macierzy transponowanej daje macierz wyjściową.
* **(A + B)<sup>T</sup> = A<sup>T</sup> + B<sup>T</sup>:** Transpozycja sumy macierzy jest równa sumie transpozycji tych macierzy.
* **(A x B)<sup>T</sup> = B<sup>T</sup> x A<sup>T</sup>:** Transpozycja iloczynu macierzy jest równa iloczynowi transpozycji tych macierzy w odwrotnej kolejności.

**Transpozycja macierzy w NumPy:**

W NumPy możemy transponować macierz za pomocą atrybutu `T` lub funkcji `np.transpose()`:

```python
import numpy as np

A = np.array([[1, 2, 3], [4, 5, 6]])

# Transpozycja za pomocą atrybutu T
A_T1 = A.T

# Transpozycja za pomocą funkcji np.transpose()
A_T2 = np.transpose(A)

print(A_T1)
print(A_T2)
```

**Wynik:**

```
[[1 4]
 [2 5]
 [3 6]]

[[1 4]
 [2 5]
 [3 6]]
```

Świetnie, że chcesz zgłębić temat macierzy odwrotnej! To bardzo ważne pojęcie w algebrze liniowej, które ma wiele zastosowań w różnych dziedzinach, takich jak rozwiązywanie układów równań liniowych, kryptografia i grafika komputerowa.

**Czym jest macierz odwrotna?**

Macierz odwrotną możemy obliczyć tylko dla macierzy kwadratowej (o ile jest ona odwracalna). Macierz odwrotna do macierzy A oznaczamy jako A<sup>-1</sup>.

Najważniejszą własnością macierzy odwrotnej jest to, że po pomnożeniu jej przez macierz wyjściową otrzymujemy macierz jednostkową:

A x A<sup>-1</sup> = A<sup>-1</sup> x A = I

gdzie I to macierz jednostkowa (macierz, która ma jedynki na głównej przekątnej i zera w pozostałych miejscach).

**Przykład:**

Załóżmy, że mamy macierz A:

```
A = [[2, 1],
     [1, 1]]
```

Macierz odwrotna A<sup>-1</sup> będzie wyglądać tak:

A<sup>-1</sup> = [[1, -1],
          [-1, 2]]

Sprawdźmy, czy po pomnożeniu A x A<sup>-1</sup> otrzymamy macierz jednostkową:

A x A<sup>-1</sup> = [[2*1 + 1*(-1), 2*(-1) + 1*2],
                 [1*1 + 1*(-1), 1*(-1) + 1*2]]
              = [[1, 0],
                 [0, 1]] = I

**Jak obliczyć macierz odwrotną?**

Istnieje kilka metod obliczania macierzy odwrotnej, np. metoda eliminacji Gaussa-Jordana lub metoda dołączonej macierzy. Dla małych macierzy można też skorzystać z prostych wzorów.

**Macierz odwrotna w NumPy:**

W NumPy możemy obliczyć macierz odwrotną za pomocą funkcji `np.linalg.inv()`:

```python
import numpy as np

A = np.array([[2, 1], [1, 1]])
A_inv = np.linalg.inv(A)
print(A_inv)
```

**Wynik:**

```
[[ 1. -1.]
 [-1.  2.]]
```

**Ważne:**

* Nie każda macierz kwadratowa ma macierz odwrotną. Macierz, która ma macierz odwrotną, nazywamy **macierzą odwracalną** lub **nieosobliwą**.
* Macierz jest odwracalna tylko wtedy, gdy jej **wyznacznik jest różny od zera**.

## Rząd macierzy — wprowadzenie

**Rząd macierzy** to jedna z podstawowych właściwości macierzy, która informuje nas, ile niezależnych wierszy lub kolumn znajduje się w macierzy. Rząd jest maksymalną liczbą liniowo niezależnych wierszy (lub kolumn) w macierzy.

* **Liniowo niezależne wiersze (kolumny)** to takie, które nie mogą być wyrażone jako kombinacja liniowa innych wierszy (kolumn).

Najprościej mówiąc, rząd macierzy to liczba wierszy lub kolumn, które są "unikalne" pod względem matematycznym, tzn. żadna z nich nie jest powtarzalną wersją innej.

### Przykład

Załóżmy, że mamy macierz:

\[
A =
\begin{bmatrix}
1 & 2 & 3 \\
2 & 4 & 6 \\
4 & 5 & 6
\end{bmatrix}
\]

* W tej macierzy drugi wiersz \( (2, 4, 6) \) jest kombinacją liniową pierwszego wiersza \( 2 \cdot (1, 2, 3) = (2, 4, 6) \).
* Rząd tej macierzy wynosi 2, ponieważ mamy dwa liniowo niezależne wiersze.

### Rząd macierzy w NumPy

Python z biblioteką NumPy pozwala na łatwe obliczanie rzędu macierzy. Użyjemy funkcji `numpy.linalg.matrix_rank()`, aby obliczyć rząd macierzy. Poniżej pokazuję krok po kroku, jak to zrobić.

#### Krok 1: Importuj bibliotekę NumPy

Najpierw musimy zaimportować bibliotekę NumPy, która jest standardowym narzędziem do pracy z macierzami w Pythonie.

```python
import numpy as np
```

#### Krok 2: Zdefiniuj macierz

Stwórzmy macierz, której rząd chcemy obliczyć. Możemy użyć tej samej macierzy co w przykładzie powyżej.

```python
A = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [4, 5, 6]
])
```

#### Krok 3: Oblicz rząd macierzy

Użyjemy funkcji `numpy.linalg.matrix_rank()` do obliczenia rzędu macierzy.

```python
rank = np.linalg.matrix_rank(A)
print(f'Rząd macierzy wynosi: {rank}')
```

#### Wynik

Wynik powinien pokazać, że rząd macierzy wynosi 2, co potwierdza naszą analizę teoretyczną.

### Podsumowanie

Rząd macierzy mówi nam o liczbie niezależnych wierszy lub kolumn w macierzy. Jest to ważne, ponieważ pokazuje nam, ile unikalnych informacji zawiera macierz. W Pythonie, za pomocą NumPy, możemy łatwo obliczyć rząd macierzy używając funkcji `numpy.linalg.matrix_rank()`.

## Generowanie liczb pseudolosowych

```python
np.random.seed(0)
```

```python
np.random.seed(10)
```

## Podstawowe funkcje

```python
np.all([1,2,3,4]) // Zwraca true jesli wszystkie elementy sa true
np.any([1,2,3,4]) // Zwraca true jesli co najmniej jeden element jest true
```

* Zwracanie indeks największej wartości

```python
A = np.random.rand(5) // [0.18048581 0.63260229 0.64625056 0.62434992 0.05933651]
np.argmax(A) // Zwraca indeks najwiekszej wartości
MaxValue = A[np.argmax(A)] // Zwraca wartość najwiekszej
MinValue = A[np.argmin(A)] // Zwraca wartość najmniejszej
ArgSort = np.argsort(A) // Zwraca indeksy posortowane według najwiekszych wartości

```
