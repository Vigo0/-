import itertools

posl = [1, 1]


class fib:
    class fibonachi:

        def __init__(self):
            self.i = 0
            self.els = posl

        def __next__(self):
            if self.i > 1:
                self.els += [posl[-1] + posl[-2]]
                j = self.i
                self.i += 1
                return (str(self.i) + ") " + str(self.els[j]))
            else:
                j = self.i
                self.i += 1
                return (str(self.i) + ") " + str(self.els[j]))

    def __iter__(self):
        return fib.fibonachi()


n = 20
f6 = fib()

for i, f in zip(
        itertools.count(3),
        itertools.islice(f6, n)
):
    print(f)
