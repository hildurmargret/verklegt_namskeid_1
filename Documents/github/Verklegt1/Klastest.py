

class Klastest:
    def __init__(self,var1=0,var2=2):
        self._var1=var1
        self.var2=var2

    def hildurprint(self):
        for i in range(5):
            print(str(i)+": allir eru betri en palina")

    def hello(self,x):
        for _ in range(x):
            print("hello world")

    def test(self):
        self.hildurprint()
        self.hello(4)



if __name__ == "__main__":
    minnklasi=Klastest()
    minnklasi.hildurprint()
    minnklasi.test()
