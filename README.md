# Career-Path-Data-Science

## Tablice

### Czym są tablice?

Tablice to struktury danych, które przechowują uporządkowane kolekcje elementów tego samego typu. Możemy sobie je wyobrazić jako szereg ponumerowanych "pudełek", gdzie każde pudełko zawiera jeden element. W kontekście AI, te elementy to zazwyczaj liczby, reprezentujące dane wejściowe, parametry modelu, wyniki obliczeń itp.

### Znaczenie tablic w AI

* **Reprezentacja danych:** Tablice są naturalnym sposobem reprezentowania wielu typów danych spotykanych w AI, takich jak:
  * Obrazy: Każdy piksel obrazu może być reprezentowany jako element tablicy, gdzie wartość elementu odpowiada kolorowi piksela.
  * Tekst: Każde słowo lub znak może być reprezentowane jako element tablicy, gdzie wartość elementu odpowiada numerycznej reprezentacji słowa/znaku (np. kodowanie one-hot).
  * Dane tabelaryczne: Każdy wiersz tabeli może być reprezentowany jako tablica, gdzie elementy odpowiadają wartościom w poszczególnych kolumnach.
* **Operacje na danych:** Biblioteki numeryczne, takie jak NumPy, dostarczają bogaty zestaw funkcji do wydajnych operacji na tablicach, takich jak:
  * Dodawanie, odejmowanie, mnożenie, dzielenie tablic element po elemencie.
  * Mnożenie macierzy.
  * Transpozycja macierzy.
  * Obliczanie średniej, wariancji, sumy itp.
  * Znajdowanie wartości maksymalnych, minimalnych.
  * Sortowanie, filtrowanie, przekształcanie tablic.
* **Implementacja modeli:** Wiele modeli AI, szczególnie sieci neuronowe, jest zbudowanych na operacjach na tablicach. Wagi sieci neuronowej, wejścia i wyjścia warstw są reprezentowane jako tablice, a proces uczenia polega na modyfikacji tych tablic w celu optymalizacji wydajności modelu.

### Niezbędne koncepty matematyczne

Aby skutecznie pracować z tablicami w kontekście AI, warto zrozumieć następujące koncepty matematyczne:

* **Algebra liniowa:**
  * Wektory i macierze: Tablice jednowymiarowe to wektory, a tablice dwuwymiarowe to macierze.
  * Operacje na wektorach i macierzach: Dodawanie, odejmowanie, mnożenie przez skalar, mnożenie macierzy.
  * Transpozycja macierzy.
  * Odwracanie macierzy.
  * Wyznacznik macierzy.
* **Rachunek różniczkowy i całkowy:**
  * Pochodne: Potrzebne do zrozumienia algorytmu wstecznej propagacji błędu w sieciach neuronowych.
  * Gradient: Wektor pochodnych cząstkowych, wskazujący kierunek największego wzrostu funkcji. Używany w optymalizacji modeli.

### Podsumowanie

Tablice to kluczowa struktura danych w AI, służąca do reprezentowania i przetwarzania danych. Zrozumienie podstaw algebry liniowej i rachunku różniczkowego jest niezbędne do efektywnej pracy z tablicami i budowania modeli AI.

## Tablice w Pythonie i NumPy

Tablice wielowymiarowe w Pythonie i bibliotece NumPy mogą wydawać się na pierwszy rzut oka trudne, ale można je porównać do rzeczy, które spotykamy w codziennym życiu, takich jak **pudełka, szafy czy regały**. Wyobraź sobie, że tablice NumPy to właśnie takie "pudełka", które mogą zawierać inne pudełka (czyli tablice w tablicach) na różnych poziomach. Chodźmy krok po kroku przez przykłady, aby lepiej zrozumieć tę koncepcję.

### 1. Tablica 1-wymiarowa (1D)

Tablica jednowymiarowa to po prostu lista elementów, np. coś jak rząd przedmiotów ustawionych obok siebie.

#### Przykład

```python
import numpy as np

# Tablica 1D
arr_1d = np.array([1, 2, 3, 4, 5])

print(arr_1d)
```

**Wyjście:**

```
[1 2 3 4 5]
```

**Analogia z życia:**
Tablica jednowymiarowa jest jak rząd książek ustawionych na jednej półce. Każda liczba w tablicy jest jak pojedyncza książka.

### 2. Tablica 2-wymiarowa (2D)

Tablica dwuwymiarowa to jak **tablica w formie siatki**, w której masz **wiersze i kolumny**. To przypomina **szafę z półkami**, gdzie każda półka ma kilka przedmiotów.

#### Przykład

```python
import numpy as np

# Tablica 2D (2 wiersze i 3 kolumny)
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr_2d)
```

**Wyjście:**

```
[[1 2 3]
 [4 5 6]]
```

**Analogia z życia:**
Wyobraź sobie szafę z dwiema półkami. Na pierwszej półce masz trzy książki (1, 2, 3), a na drugiej również trzy książki (4, 5, 6). Tak wygląda tablica 2-wymiarowa.

* **Wiersze** to półki.
* **Kolumny** to książki na każdej półce.

### 3. Tablica 3-wymiarowa (3D)

Tablica trójwymiarowa to coś w rodzaju **regału z kilkoma szafkami, w każdej z których znajdują się półki z przedmiotami**.

#### Przykład

```python
import numpy as np

# Tablica 3D (2 szafki, w każdej 2 wiersze i 3 kolumny)
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], 
                   [[7, 8, 9], [10, 11, 12]]])

print(arr_3d)
```

**Wyjście:**

```
[[[ 1  2  3]
  [ 4  5  6]]

 [[ 7  8  9]
  [10 11 12]]]
```

**Analogia z życia:**
To jest jak regał z **dwiema szafkami**. Każda szafka ma **dwie półki**, a na każdej półce są **trzy książki**.

* Mamy dwie **szafki**.
* W każdej szafce są **dwie półki** (wiersze).
* Na każdej półce są **trzy książki** (kolumny).

### 4. Więcej wymiarów (np. 4D i więcej)

Tablice wyższych wymiarów mogą być trudniejsze do wizualizacji, ale możemy sobie wyobrazić np. **kilka regałów** w pokoju, z których każdy ma szafki, a te z kolei mają półki z książkami.

Tablice te są rzadko spotykane w codziennym programowaniu, ale są używane w zaawansowanych obliczeniach matematycznych i przetwarzaniu danych, np. w **grafice komputerowej** czy **naukach o danych**.

### Przykłady codzienne

* **1D**: Lista zakupów - pojedyncza lista przedmiotów, które chcesz kupić.
* **2D**: Plan klas - masz wiersze (rzędy), gdzie każda klasa (wiersz) ma kilka osób (kolumny).
* **3D**: Harmonogram lekcji - każdy dzień tygodnia (szafka) ma różne lekcje (półki), a każda lekcja ma listę zadań (kolumny).

### Jak działa indeksowanie w tablicach wielowymiarowych?

W tablicach wielowymiarowych możemy odwoływać się do konkretnych elementów, podając odpowiednie indeksy.

#### Przykład

```python
import numpy as np

# Tablica 3D
arr_3d = np.array([[[1, 2, 3], [4, 5, 6]], 
                   [[7, 8, 9], [10, 11, 12]]])

# Dostęp do pierwszej szafki, pierwszej półki, pierwszej książki
print(arr_3d[0, 0, 0])  # Wyjście: 1

# Dostęp do drugiej szafki, drugiej półki, trzeciej książki
print(arr_3d[1, 1, 2])  # Wyjście: 12
```

### Podsumowanie

* **1D**: Jak rząd książek na półce.
* **2D**: Jak szafa z kilkoma półkami i książkami na każdej półce.
* **3D**: Jak regał z szafkami, półkami i książkami.
* **Indeksowanie**: Możesz odwoływać się do dowolnego elementu, podając odpowiednie współrzędne (indeksy).

### MM

![Dostęp do tablic](/img/Dostep%20do%20tablic.png)

## Podstawowe operacje na tablicach

