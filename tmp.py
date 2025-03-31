class Prova:
    _myClassVariable = 0

    def __init__(self, input):
        self.myInstanceVariable = input

    def standardMethod(self):
        print(self.myInstanceVariable)

    @staticmethod
    def staticMethod():
        pass

    @classmethod
    def classMethod(cls):
        print(cls._myClassVariable)

newInstance = Prova("txt")
newInstance.standardMethod()