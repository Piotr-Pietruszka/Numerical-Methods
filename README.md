## Metody numeryczne

# 1) Rozwinięcie w szereg Taylora
Rozwinięcie w szereg Taylora funkcji sinh(x). Porównanie dokładności w zależności od liczby elementów w rozwinięciu oraz wykresy wielomianów aproksymujących, razem z właściwą funkcją.

# 2) Numeryczne przybliżenie pochodnej
Numeryczne przybliżenie pochodnej funkcji sinh(x) w punkcie x=0.5, w zależności od wielkości kroku użytego do przybliżania (znając rozwiązanie analityczne pochodnej można wyznaczyć prawdziwy błąd). Można zauważyć, że błąd nie jest najmniejszy dla najmniejszych wartości kroku, co wynika z większego wpływu błędów numerycznych. 

# 3) Rozwiązanie układu równań liniowych
Rozwiązanie układu równań liniowych, przy pomocy rozkładu LU.

# 4) Rozwiązanie układu równań nieliniowych
Rozwiązanie układu równań nieliniowych metodami: iteracyjną i Newtona-Raphsona, dla porównania również metodą graficzną. Jeden z plików odpowiedzialny jest za narysowanie wykresów równań (metoda graficzna), a kolejny z rozwiązanie układu powyższymi metodami. Startowanie z różnych punktów początkowych prowadzi do różnych rozwiązań (punkty, z których należy startować by osiągnąć dane rozwiązanie są umieszczone w komentarzach). Rysowany jest również błąd dla obydwu metod, służący jako porównanie szybkości ich zbieżności.

# 5) Sterowanie optymalne
Wyznaczenie modelu stanowego (postać regulatorowa) z danej transmitancji (w dziedzinie z). Znalezienie optymalnego sterownika LQR i narysowanie odpowiedzi skokowej układu ze sterownikiem.

# 6) Aproksymacja transmitancji
Wyznaczanie transmitancji układu drugiego rzędu, którego odpowiedź najlepiej pasuje do punktów pomiarowych.

# 7) Filtr Kalmana
Estymacja położenia na płaszczyźnie w punktach pośrednich oraz przewidywanie kolejnych położeń, przy użyciu filtru Kalmana.

# 8) Interpolacja
Interpolacja podanych punktów metodą wielomianu Newtona oraz funkcji sklejanych trzeciego rzędu. Punkty są wczytywane z pliku tekstowego.

# 9) Całkowanie numeryczne
Obliczanie całki z wielomianu,  w danych granicach. Przy użyciu metod: Romberga i trzypunktowej kwadratury Gaussa. Dla porównania całka jest również liczona analitycznie.

# 10) Równanie różniczkowe
Rozwiązanie podanego równania różniczkowego. stosując metody: Eulera, Heuna oraz punktu środkowego. Użytkownik specyfikuje parametry: tk - czas końcowy oraz n - liczba segmentów. Rozwiązania poszczególnymi metodami oraz rozwiązanie analityczne (dla porównania) są wyświetlane na wspólnym wykresie.

# 11) Układ równań różniczkowych
Rozwiązanie równania układu równań różniczkowych metodą Rungego-Kutty.
Wizualizacja w postaci wykresów przebiegu zmiennych w zależności od czasu oraz poprzez trajektorię fazową.

# 12) Warunki brzegowe
Rozwiązanie równanie różniczkowego, opisującego rozkład temperatury na płytce w stanie ustalonym, przy danych warunkach brzegowych. Wizualizacja wyniku w postaci mapy ciepła.



