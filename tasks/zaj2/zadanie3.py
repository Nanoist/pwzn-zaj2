# -*- coding: utf-8 -*-
#!/usr/bin/env python3

import math


class Integrator(object):

    """
    Klasa która implementuje całki metodą Newtona Cotesa z użyciem interpolacji
    N-tego stopnia :math:`n\in<2, 11>`.

    .. note::

        Używamy wzorów NC nie dlatego że są super przydatne (zresztą gorąco
        zniechęcam Państwa przed pisaniem własnych podstawowych algorytmów
        numerycznych --- zbyt łatwo o głupi błąd) ale dlatego żebyście
        jescze raz napisali jakiś algorytm w którym nie opłaca się zrobić 11
        ifów.

    """

    @classmethod
    def get_level_parameters(cls, level):
        """

        :param int level: Liczba całkowita większa od jendości.
        :return: Zwraca listę współczynników dla poszczególnych puktów
                 w metodzie NC. Na przykład metoda NC stopnia 2 używa punktów
                 na początku i końcu przedziału i każdy ma współczynnik 1,
                 więc metoda ta zwraca [1, 1]. Dla NC 3 stopnia będzie to
                 [1, 3, 1] itp.
        :rtype: List of integers
        """
        factor = [
            [1/2, 1/2],
            [1/3, 4/3, 1/3],
            [3/8, 9/8, 9/8, 3/8],
            [14/45, 64/45, 24/45, 64/45, 14/45],
            [95/288, 375/288, 250/288, 250/288, 375/288, 95/288],
            [41/140, 216/140, 27/140, 272/140, 27/140, 216/140, 41/140],
            [(7*751)/17280, (7*3577)/17280, (7*1323)/17280, (7*2989)/17280,
             (7*2989)/17280, (7*1323)/17280, (7*3577)/17280, (7*751)/17280 ],
            [(4*989)/14175, (4*5888)/14175, -(4*928)/14175 ,(4*10496)/14175,
             -(4*4540)/14175, (4*10496)/14175, -(4*928)/14175, (4*5888)/14175,
             (4*989)/14175],
            [(9*2857)/89600, (9*15741)/89600, (9*1080)/89600, (9*19344)/89600,
             (9*5778)/89600, (9*5778)/89600, (9*19344)/89600, (9*1080)/89600,
             (9*15741)/89600, (9*2857)/89600],
            [(5*16067)/299376, (5*106300)/299376, -(5*48525)/299376,
             (5*272400)/299376, -(5*260550)/299376, (5*427368)/299376,
             -(5*260550)/299376, (5*272400)/299376, -(5*48525)/299376,
             (5*106300)/299376, (5*16067)/299376]
        ]
        return factor[level]

    def __init__(self, level):
        """
        Funkcja ta inicjalizuje obiekt do działania dla danego stopnia metody NC
        Jeśli obiekt zostanie skonstruowany z parametrem 2 używa metody trapezów.
        :param level: Stopień metody NC
        """
        self.level = level

    def integrate(self, func, func_range, num_evaluations):
        """
        Funkcja dokonuje całkowania metodą NC.

        :param callable func: Całkowana funkcja, funkcja ta ma jeden argument,
                              i jest wołana w taki sposób: `func(1.0)`.
        :param Tuple[int] func_range: Dwuelementowa krotka zawiera początek i koniec
                                 przedziału całkowania.
        :param int num_evaluations: Przybliżona lość wywołań funkcji ``func``,
            generalnie algorytm jest taki:

            1. Dzielimy zakres na ``num_evaluations/self.level`` przdziałów.
               Jeśli wyrażenie nie dzieli się bez reszty, należy wziąć najmiejszą
               liczbę całkowitą większą od `num_evaluations/self.level``. 
            2. Na każdym uruchamiamy metodę NC stopnia ``self.level``
            3. Wyniki sumujemy.

            W tym algorytmie wykonamy trochę więcej wywołań funkcji niż ``num_evaluations``,
            dokłanie ``num_evaluations`` byłoby wykonywane gdyby keszować wartości
            funkcji na brzegach przedziału całkowania poszczególnych przedziałów.

        :return: Wynik całkowania.
        :rtype: float
        """
        interval = num_evaluations//self.level + 1
        a, b = func_range
        length = (b - a) / interval
        step = length / (self.level-1)
        params = self.get_level_parameters(self.level)
        result = 0
        for ii in range(interval):
            for jj in range(self.level+1):
                result += func(a + jj*step + ii*length)*params[jj]*step
        return result
    


if __name__ == '__main__':
    i = Integrator(3)
    print(i.integrate(math.sin, (0, 2*math.pi), 30))
    print(i.integrate(lambda x: x*x, (0, 1), 30))
