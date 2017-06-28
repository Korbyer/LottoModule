import requests,json,xlrd
from xlutils.copy import copy
import datetime
from bs4 import BeautifulSoup

# 로또 웹 사이트의 첫 주소
main_url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber"

# 각 회차별 당첨정보를 알 수 있는 주소
basic_url = "http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo="

today = datetime.datetime.now()
checkDate = today.strftime('%Y-%m-%d')
demoNext = today + datetime.timedelta(7)
nextDate = demoNext.strftime('%Y-%m-%d')


def __init__():
    print("Class Update Initiated")


def ReturnLastDrwNo():
    url = main_url
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    data = soup.find_all('body')
    result = data[0].find('p').text
    dict = json.loads(result)
    s = int(dict['drwNo'])
    return s


def updateExcel(drwNo):
    print("Excel update Initiating...")
    url = basic_url + str(drwNo)
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    data = soup.find_all('body')
    result = data[0].find('p').text
    dict = json.loads(result)

    rbk = xlrd.open_workbook('lotto.xls')
    wbk = copy(rbk)
    sheet = wbk.get_sheet(0)

    sheet.write(drwNo, 0, drwNo)
    sheet.write(drwNo, 1, dict['firstWinamnt'])
    sheet.write(drwNo, 2, dict['totSellamnt'])
    sheet.write(drwNo, 3, dict['returnValue'])
    sheet.write(drwNo, 4, dict['drwtNo1'])
    sheet.write(drwNo, 5, dict['drwtNo2'])
    sheet.write(drwNo, 6, dict['drwtNo3'])
    sheet.write(drwNo, 7, dict['drwtNo4'])
    sheet.write(drwNo, 8, dict['drwtNo5'])
    sheet.write(drwNo, 9, dict['drwtNo6'])
    sheet.write(drwNo, 10, dict['bnusNo'])
    sheet.write(drwNo, 11, dict['drwNoDate'])
    sheet.write(drwNo, 12, dict['firstPrzwnerCo'])

    wbk.save('lotto.xls')

from LottoModule import Update
a=Update.updateExcel(Update.ReturnLastDrwNo())

