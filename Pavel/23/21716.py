def f(start, stop):
    #                       избегаемый этап
    if (start > stop) or (start == 56): return 0
    if start == stop: return 1

    return (
        f(start + 3, stop) +
        f(start + 7, stop) +
        f(start*3, stop)
    )

# обязательные этапы - разбивают промежуток на части
print(f(12, 40)*f(40, 72)*f(72, 89))