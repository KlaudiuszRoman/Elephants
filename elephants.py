#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 10:40:40 2022

@author: user

Data input example:
4
3213 4643 5632 987
1 4 3 2
2 1 3 4

where first line is elephents count
      second line is elephants weight
      second line is elephants actual positions
      second line is elephants expected positions

program show in console optimal cost of achived
expected position

in one turn we can only change position between two
elephants and cost of this move is sum of their weight

"""
import sys


def solve():
    data = []
    data.append(input().split(' '))
    data.append(input().split(' '))
    data.append(input().split(' '))
    data.append(input().split(' '))

    # Pobranie liczby słoni do osobnej zmiennej
    elephant_count = int(data[0][0].strip())
    # Przepisanie wag słoni do osobnej listy
    elephant_weight = [-1]
    for weight in data[1]:
        elephant_weight.append(int(weight.strip()))
    # Lista z początkowymi pozycjami słoni
    a = [-1]
    for position in data[2]:
        a.append(int(position.strip()))
    # Lista z oczekiwanymi pozycjami słoni
    b = [-1]
    for position in data[3]:
        b.append(int(position.strip()))

    # Przepisanie wag słoni do słownika (dla wygodniejszej pracy)
    elephant_weight_dict = {}
    for i in range(elephant_count):
        elephant_weight_dict[i + 1] = elephant_weight[i + 1]

    del data

    # Konstrukcja permutacji p
    # Słoń o numerze x powinien znaleźć się w miejscu słonia y

    p = [-1]
    for i in range(1, elephant_count + 1):
        p.append(a[b.index(i)])

    # Rozkład p na cykle proste
    odw = [-1]
    for i in range(1, elephant_count + 1):
        odw.append(False)

    c = 0
    c_large = [[-1]]  # Lista cykli
    for i in range(1, elephant_count + 1):
        if not odw[i]:
            c += 1
            c_large.append([])
            x = i
            while not odw[x]:
                odw[x] = True
                c_large[c].append(x)
                x = p[x]

    # Wyznaczenie parametrów cykli

    suma_c = [-1]  # Suma mas słoni z poszczególnych cykli
    min_c = [-1]  # Masa najlżejszego słonia na cyklu
    min_m = float('inf')

    for i in range(1, c + 1):
        suma_c.append(0)
        min_c.append(float('inf'))
        for e in c_large[i]:
            suma_c[i] += elephant_weight_dict[e]
            min_c[i] = min(min_c[i], elephant_weight_dict[e])
        min_m = min(min_m, min_c[i])

    # Obliczenie wyniku

    w = 0
    for i in range(1, c + 1):
        metoda1 = suma_c[i] + (len(c_large[i]) - 2) * min_c[i]
        metoda2 = suma_c[i] + min_c[i] + (len(c_large[i]) + 1) * min_m
        w += min(metoda1, metoda2)

    return w


if __name__ == '__main__':
    print(solve())
