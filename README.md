# Biblioteka - Projekt końcowy na Bazy Danych

Jest to aplikacja webowa napisana przy użyciu frameworka Flask, która pozwala na przeglądanie książek dostępnych w bibliotece, członków biblioteki oraz książek według autorów. Umożliwia także zarządzanie wypożyczeniami książek.

### Wymagania
- Python 3.x
- Flask
- Flask_mysqldb
- MySQLdb

### Instalacja

```bash
git clone https://github.com/sqrasdf/biblioteka_bazy_danych.git
cd biblioteka_bazy_danych
```

```bash
pip install -r requirements.txt
```

Jeśli to konieczne, pliku `app.py` zmień wartości zmiennych na odpowiednie
```python
Skopiuj kod
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'LibraryDB'
```

### Uruchomienie

```bash
python app.py
```
Otwórz przeglądarkę i przejdź do http://127.0.0.1:5000/

### Aplikacja oferuje następujące funkcjonalności:

- Strona główna (/): Jest punktem wyjścia, z którego użytkownicy mogą przejść do różnych sekcji serwisu. Zawiera panel z przyciskami, które prowadzą do konkretnych podstron.

- Przeglądaj autorów (/authors): Na tej podstronie użytkownicy mogą zobaczyć listę wszystkich autorów, których książki są dostępne w bibliotece. Strona wyświetla podstawowe informacje o każdym autorze, takie jak imię i nazwisko. Może również zawierać linki do stron szczegółowych dla poszczególnych autorów, gdzie można znaleźć więcej informacji na ich temat oraz listę ich książek.

- Książki według autora (/author/<author_id>): Ta podstrona pokazuje wszystkie książki napisane przez wybranego autora. Wyświetla szczegóły takie jak tytuł książki, imię i nazwisko autora oraz rok wydania. Umożliwia użytkownikom przeglądanie dorobku literackiego konkretnego autora i szybkie odnalezienie interesujących ich tytułów.

- Przeglądaj książki (/books): Na tej podstronie znajduje się pełna lista książek dostępnych w bibliotece. Każda pozycja zawiera informacje o tytule, autorze, gatunku i roku wydania.

- Przeglądaj członków (/members): Podstrona wyświetlająca listę wszystkich członków biblioteki. Zawiera podstawowe informacje o członkach, takie jak imię, nazwisko oraz data przystąpienia do biblioteki. Może również umożliwiać przejście do szczegółowych informacji o konkretnym członku, takich jak historia wypożyczeń.

- Wypożyczenia członka (/member/<member_id>): Strona pokazuje historię wypożyczeń książek przez wybranego członka biblioteki. Wyświetla informacje takie jak tytuł książki, imię i nazwisko autora, data wypożyczenia oraz data zwrotu.

- Przeglądaj wypożyczenia (/loans): Na tej podstronie wyświetlana jest pełna lista wszystkich wypożyczeń książek w bibliotece. Zawiera informacje o wypożyczonych książkach, członkach, którzy je wypożyczyli, datach wypożyczenia oraz zwrotu. Umożliwia zarządzanie wypożyczeniami i monitorowanie aktywności wypożyczeń.

- Ranking wypożyczeń (/loans_ranking): Podstrona prezentująca ranking członków biblioteki według liczby wypożyczeń. Wyświetla imiona i nazwiska członków oraz liczbę wypożyczeń. Ranking pomaga zidentyfikować najbardziej aktywnych użytkowników biblioteki.

- Przeglądaj gatunki (/genres): Strona wyświetlająca listę wszystkich gatunków książek dostępnych w bibliotece. Zawiera nazwy gatunków, umożliwiając użytkownikom przeglądanie książek według ich preferencji gatunkowych. Może także zawierać linki do stron, na których wyświetlane są książki przypisane do danego gatunku.

