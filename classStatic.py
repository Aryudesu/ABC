class testClass:
    data = dict()

    @classmethod
    def setData(cls, key, value):
        cls.data[key] = value

    def printData(self):
        print(self.data)

    def addData(self, key, value):
        testClass.setData(key, value)


data1 = testClass()
data2 = testClass()
data1.printData()
data2.printData()
data1.addData("A", 314)
data1.printData()
data2.printData()
data2.addData("B", 159)
data1.printData()
data2.printData()
data1.addData("C", 265)
data1.printData()
data2.printData()
