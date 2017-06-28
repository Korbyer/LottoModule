import random
class Lotto:


    def makefile(self):
        from LottoModule import MakeExcel as excel
        from LottoModule import Update as up
        excel.makeExcel(up.ReturnLastDrwNo())


    def setSize(self):
        a=random.random()
        return a

    def updateLotto(self):
        from LottoModule import Update as up
        up.updateExcel(up.ReturnLastDrwNo())

    def makeData(self):
        from LottoModule import GetInfo as info
        from LottoModule import Update as up
        a=info.makeDataSet(up.ReturnLastDrwNo())
        return a


b=Lotto.makeData(Lotto)
a=Lotto.updateLotto(Lotto)
print(b)


