# На сковороде k котлет, прожарка одной стороны m минут, дано n котлет, найти наименшую время полной готовности
# def kotlet(k,m,n):

#     if k >= n:
#         t = 2*m
#     elif n*2%k == 0:
#         t = m * (n * 2 // k)
#     else:
#         t = m * (1 + (n * 2) // k)
    
#     return t

#''' Требуется определить, бьет ли конь, стоящий на клетке с указанными координатами (номер строки и номер столбца), фигуру, стоящую на другой указанной клетке. Вводятся четыре числа: координаты коня и координаты другой фигуры. Вывод если бьет: "Да" Вывод если не бьет: "Нет"'''   

def elephant_beats_check(x1, y1, x2, y2):
    a1 = x1 + 2 == x2
    a2 = y1 + 1 == y2
    b1 = x1 + 1 == x2
    b2 = y1 + 2 == y2
    c2 = y1 - 1 == y2
    d2 = y1 - 2 == y2
    e1 = x1 - 1 == x2
    e2 = y1 - 2 == y2
    f1 = x1 - 2 == x2
    g1 = abs(x1 + 1) == x2
    if (a1 and a2) or (b1 and b2) or (a1 and c2) or (b1 and d2) or (e1 and e2) or (f1 and c2) or (f1 and a2) or(e1 and b2) or (g1 and b2):
        return "Да"
    else:
        return "Нет"

print(elephant_beats_check(0,-4,1,-6))