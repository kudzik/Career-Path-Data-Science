# Rachunek prawdopodobienstwa

**1. Zmienna losowa:**

Zmienna losowa to zmienna, której wartość jest wynikiem zjawiska losowego. Na przykład, wynik rzutu kostką jest zmienną losową, ponieważ może przyjąć wartości od 1 do 6 z określonym prawdopodobieństwem.

**2. Wariancja:**

Wariancja to miara rozproszenia wartości zmiennej losowej wokół jej wartości oczekiwanej. Intuicyjnie, im większa wariancja, tym bardziej wartości są "rozrzucone".

**3. Kowariancja:**

Kowariancja to miara zależności liniowej między dwiema zmiennymi losowymi.

* Kowariancja dodatnia wskazuje na tendencję do jednoczesnego wzrostu lub spadku obu zmiennych.
* Kowariancja ujemna wskazuje na tendencję do wzrostu jednej zmiennej przy jednoczesnym spadku drugiej.
* Kowariancja bliska zeru wskazuje na brak liniowej zależności między zmiennymi.

**Macierz kowariancji:**

Macierz kowariancji to macierz kwadratowa, która zawiera wariancje i kowariancje dla zbioru zmiennych losowych. Element na przekątnej macierzy to wariancja danej zmiennej, a element poza przekątną to kowariancja między dwiema zmiennymi.

**Interpretacja macierzy kowariancji:**

* Wartości na przekątnej (wariancje) pokazują, jak bardzo "rozrzucone" są wartości poszczególnych zmiennych.
* Wartości poza przekątną (kowariancje) pokazują, jak silna jest liniowa zależność między parami zmiennych.

**Przykład:**

Załóżmy, że mamy dwie zmienne losowe: wzrost i wagę. Macierz kowariancji dla tych zmiennych może wyglądać następująco:

```
      wzrost    waga
wzrost  36      15
waga    15      25
```

Wariancja wzrostu wynosi 36, wariancja wagi wynosi 25, a kowariancja między wzrostem a wagą wynosi 15. Oznacza to, że istnieje dodatnia korelacja między wzrostem a wagą - osoby wyższe mają tendencję do bycia cięższymi.

Macierz kowariancji jest używana w wielu dziedzinach, takich jak statystyka, uczenie maszynowe i finanse. Na przykład, w uczeniu maszynowym jest ona używana w algorytmie PCA (Principal Component Analysis) do redukcji wymiarowości danych.

## Przestrzeń probabilistyczna

Przestrzeń probabilistyczna to matematyczny koncept, który służy do modelowania zjawisk losowych. Można ją sobie wyobrazić jako "pojemnik" zawierający wszystkie możliwe wyniki danego eksperymentu losowego oraz informacje o prawdopodobieństwie wystąpienia każdego z tych wyników.

Formalnie, przestrzeń probabilistyczna to trójka $(\Omega, \mathcal{F}, P)$, gdzie:

* **Ω** (omega) - to zbiór wszystkich możliwych wyników eksperymentu losowego, zwany **przestrzenią zdarzeń elementarnych**.
* **ℱ** (sigma-ciało) - to zbiór podzbiorów Ω, zwany **przestrzenią zdarzeń losowych**.  $\mathcal{F}$ musi spełniać pewne warunki, m.in. zawierać Ω i zbiór pusty, a także być zamknięte na dopełnienia i przeliczalne sumy.
* **P** - to funkcja prawdopodobieństwa, która przypisuje każdemu zdarzeniu z $\mathcal{F}$ liczbę z przedziału [0, 1], reprezentującą prawdopodobieństwo wystąpienia tego zdarzenia.

**Przykład:**

Rzucamy monetą.

* Ω = {orzeł, reszka} (dwa możliwe wyniki)
* ℱ = {∅, {orzeł}, {reszka}, {orzeł, reszka}}  (wszystkie możliwe podzbiory Ω)
* P({orzeł}) = 0.5, P({reszka}) = 0.5 (zakładając, że moneta jest symetryczna)

**Po co nam przestrzeń probabilistyczna?**

Pozwala ona na formalny opis zjawisk losowych i przeprowadzanie analizy probabilistycznej. Dzięki niej możemy obliczać prawdopodobieństwa zdarzeń, badać zależności między nimi, a także modelować procesy losowe.

**Zastosowania:**

Przestrzenie probabilistyczne są wykorzystywane w wielu dziedzinach, takich jak:

* Teoria gier
* Statystyka
* Finanse
* Fizyka
* Informatyka
* Uczenie maszynowe

```python
import numpy as np

# Przykład: symulacja rzutu kostką
wyniki = np.random.randint(1, 7, size=1000)  # 1000 rzutów kostką

# Obliczenie prawdopodobieństwa wyrzucenia 6
p_6 = np.sum(wyniki == 6) / len(wyniki)
print(f"Prawdopodobieństwo wyrzucenia 6: {p_6}")
```
