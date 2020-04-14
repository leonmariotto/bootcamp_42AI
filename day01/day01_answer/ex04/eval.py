class Evaluator():
    def zip_evaluate(coefs, words):
        if type(coefs) is not list and type(words) is not list:
            print(-1)
            return
        if len(coefs) != len(words):
            print(-1)
            return
        zipped = zip(coefs, words)
        c = 0
        for elem in zipped:
            c = c + len(elem[1]) * elem[0]
        print(c)

    def enumerate_evaluate(coefs, words):
        if type(coefs) is not list and type(words) is not list:
            print(-1)
            return
        if len(coefs) != len(words):
            print(-1)
            return
        c = 0
        words = list(enumerate(words))
        for i, val in words:
            c = c + len(val) * coefs[i]
        print(c)
