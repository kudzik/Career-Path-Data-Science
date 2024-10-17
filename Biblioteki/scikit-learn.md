# Scikit-learn

Scikit-learn to potężna biblioteka Pythona do uczenia maszynowego. Oferuje szeroki wachlarz algorytmów i narzędzi do budowy modeli predykcyjnych, analizy danych i wizualizacji.

**Główne cechy:**

* **Różnorodność algorytmów:**  Regresja, klasyfikacja, klastrowanie, redukcja wymiarowości, selekcja modeli i wiele innych.
* **Prostota użycia:**  Spójny interfejs API ułatwiający naukę i stosowanie.
* **Efektywność:**  Zoptymalizowane algorytmy i struktury danych dla dużych zbiorów danych.
* **Wszechstronność:**  Współpracuje z innymi bibliotekami Pythona, takimi jak NumPy, SciPy i Pandas.

**Typowy przepływ pracy:**

1. **Przygotowanie danych:**  Wczytanie, czyszczenie, transformacja i podział na zbiory treningowe i testowe.
2. **Wybór modelu:**  Wybór odpowiedniego algorytmu uczenia maszynowego do danego problemu.
3. **Trenowanie modelu:**  Dopasowanie modelu do danych treningowych.
4. **Ewaluacja modelu:**  Ocena wydajności modelu na danych testowych.
5. **Strojenie hiperparametrów:**  Optymalizacja hiperparametrów modelu w celu poprawy wydajności.
6. **Wdrożenie modelu:**  Użycie modelu do przewidywania na nowych danych.

**Przykład:**

```python
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np

# Przygotuj dane
X = np.array([[1], [2], [3], [4], [5]])
y = np.array([2, 4, 5, 4, 5])

# Podziel dane na zbiory treningowe i testowe
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Utwórz model regresji liniowej
model = LinearRegression()

# Wytrenuj model
model.fit(X_train, y_train)

# Przewiduj na danych testowych
y_pred = model.predict(X_test)

# Wyświetl wyniki
print("Przewidywane wartości:", y_pred)
```

**Moduły:**

Scikit-learn zawiera wiele modułów, m.in.:

* `sklearn.linear_model`:  Modele regresji liniowej.
* `sklearn.tree`:  Drzewa decyzyjne.
* `sklearn.ensemble`:  Zespoły modeli (np. lasy losowe).
* `sklearn.cluster`:  Algorytmy klastrowania.
* `sklearn.metrics`:  Miary oceny modeli.

Scikit-learn to wszechstronne narzędzie do uczenia maszynowego, które jest szeroko stosowane w wielu dziedzinach, od analizy danych po sztuczną inteligencję.
