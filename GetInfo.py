import xlrd
def makeDataSet(drwNo):
    dataSet = []
    wbk = xlrd.open_workbook('lotto.xls')
    wbk_name = wbk.sheet_by_name('sheet1')
    for i in range(1,drwNo+1):
        each_rows = wbk_name.row_values(i, 4, 11)
        dataSet.append(each_rows)
        for j in range(0, 7):
            dataSet[i-1][j] = int(dataSet[i-1][j])
    return dataSet
