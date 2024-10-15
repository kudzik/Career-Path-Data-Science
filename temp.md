Aby omówić obiekt DataFrame, stworzę przykładowy DataFrame z użyciem biblioteki pandas. Następnie wyświetlę ten DataFrame wraz z jego typem, aby pokazać, jak wygląda i jakiego jest typu.

```python?code_reference&code_event_index=3
import pandas as pd

# Utwórz DataFrame
df = pd.DataFrame({'Imię': ['Jan', 'Anna', 'Piotr', 'Maria'],
                   'Wiek': [25, 30, 28, 22],
                   'Miasto': ['Warszawa', 'Kraków', 'Poznań', 'Gdańsk']})

# Wyświetl DataFrame
print("DataFrame:\n", df)

# Wyświetl typ DataFrame
print("\nTyp DataFrame:", type(df))
```

```text?code_stdout&code_event_index=3
DataFrame:
     Imię  Wiek    Miasto
0    Jan    25  Warszawa
1   Anna    30    Kraków
2  Piotr    28    Poznań
3  Maria    22    Gdańsk

Typ DataFrame: <class 'pandas.core.frame.DataFrame'>

```

DataFrame to dwuwymiarowa struktura danych,  która przypomina tabelę w bazie danych lub arkusz kalkulacyjny. Składa się z wierszy i kolumn, gdzie każda kolumna może mieć inny typ danych (liczby, tekst, daty itp.). DataFrame posiada etykiety wierszy (indeks) i etykiety kolumn.

### Tworzenie DataFrame

DataFrame można utworzyć na wiele sposobów, np. z:

* słownika list lub tablic
* listy słowników
* pliku CSV
* tabeli bazy danych

### Przykład

```python
import pandas as pd

# Utwórz DataFrame ze słownika list
df = pd.DataFrame({'Imię': ['Jan', 'Anna', 'Piotr', 'Maria'],
                   'Wiek': [25, 30, 28, 22],
                   'Miasto': ['Warszawa', 'Kraków', 'Poznań', 'Gdańsk']})

print(df)
```

### Wynik

```
    Imię  Wiek    Miasto
0    Jan    25  Warszawa
1   Anna    30    Kraków
2  Piotr    28    Poznań
3  Maria    22    Gdańsk
```

```
