def f(start, stop):
    if (start > stop) or (start == 15): return 0
    if start == stop: return 1

    return f(start + 1, stop) + f(start + 3, stop) + \
        f(start*3, stop)

# Сколько существует программ, для которых при 
# исходном числе 7 результатом является число 20
# не содержит 14
print(f(7, 14)*f(14, 20))
