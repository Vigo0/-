def repeat(t):

    def h(g):
        def f(v):
            for i in range(0,t):
                r = g(v)
            return v
        return f
    return h
@repeat(5)
def summ3(x):
    return x + 3


@repeat(6)
def stepen3(x):
    return x** 3


@repeat(3)
def ymnoj10(x):
    return x * 10
print(stepen3(100))
print(ymnoj10(7))
print(summ3(99))

