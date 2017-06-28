import xlwt,json,requests
from bs4 import BeautifulSoup

# 로또 웹 사이트의 첫 주소
main_url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber"

# 각 회차별 당첨정보를 알 수 있는 주소
basic_url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo="


def makeExcel(drwNo):
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet('sheet1')
    sheet.write(0, 0, 'drwNo')
    sheet.write(0, 1, 'firstWinamnt')
    sheet.write(0, 2, 'totSellamnt')
    sheet.write(0, 3, 'returnValue')
    sheet.write(0, 4, 'drwtNo1')
    sheet.write(0, 5, 'drwtNo2')
    sheet.write(0, 6, 'drwtNo3')
    sheet.write(0, 7, 'drwtNo4')
    sheet.write(0, 8, 'drwtNo5')
    sheet.write(0, 9, 'drwtNo6')
    sheet.write(0, 10, 'bnusNo')
    sheet.write(0, 11, 'drwNoDate')
    sheet.write(0, 12, 'firstPrzwnerCo')

    for i in range(1, drwNo + 1):
        url = basic_url + str(i)
        source = requests.get(url).text
        soup = BeautifulSoup(source, 'lxml')
        data = soup.find_all('body')
        result = data[0].find('p').text
        dict = json.loads(result)

        sheet.write(i, 0, i)
        sheet.write(i, 1, dict['firstWinamnt'])
        sheet.write(i, 2, dict['totSellamnt'])
        sheet.write(i, 3, dict['returnValue'])
        sheet.write(i, 4, dict['drwtNo1'])
        sheet.write(i, 5, dict['drwtNo2'])
        sheet.write(i, 6, dict['drwtNo3'])
        sheet.write(i, 7, dict['drwtNo4'])
        sheet.write(i, 8, dict['drwtNo5'])
        sheet.write(i, 9, dict['drwtNo6'])
        sheet.write(i, 10, dict['bnusNo'])
        sheet.write(i, 11, dict['drwNoDate'])
        sheet.write(i, 12, dict['firstPrzwnerCo'])
    wbk.save('lotto.xls')





