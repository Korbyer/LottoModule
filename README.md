# LottoModule
LottoModule & MLModule 패키지를 하위항목으로 두고있는 가장 최상위 프로젝트 입니다. 이 프로젝트의 목적은 기존의 로또 당첨 정보들을 머신러닝을 통하여 정제하고 분석, 추출하여 가장 당첨확률이 높은 로또정보들을 서버에 전송하는 것입니다.
예상당첨금액, 예상당첨번호, 예상당첨확률 등이 서버에 전송될 것입니다.





## LottoModule 패키지
머신러닝을 통해 사용자에게 가장 당첨확률이 높은 번호들을 추출하고 분석하여 서버에 전송하는것이 이 모듈의 목적입니다.
그 중에서, **LottoModule**은 머신러닝 분석을 위한 정보를 추출하고 선별하여 보내주는 모듈입니다.





### GetInfo
GetInfo파일은 MakeExcel.py & Update.py 파일을 통해 만들어진 Lotto.xls 파일에서 1회차부터 가장 최신회차까지의 로또 당첨번호 정보를 리스트형식으로 리턴해주는 파일입니다. GetInfo 를 통해서 첫번째 당첨번호부터 보너스 당첨번호(dataSet[7]) 까지 dataSet에 저장됩니다.





### Lotto
LottoModule & MLModule 패키지 안에 존재하는 파일들의 기능들이 제대로 작동하는지 테스트하는 파일입니다.





### MakeExcel
MakeExcel 파일은 현재 존재하는 [로또 API](http://www.nlotto.co.kr/common.do?method=getLottoNumber&drwNo=) 를 통해 가장최근의당첨번호(*drwNo*)를 인자로 받아 최신회차까지의 모든정보를 .xls 형식의 파일로 만들어 저장해주는 파일입니다. 함수 *makeExcel(drwNo)* 을 통해 만들어집니다.

> 문제점: 
크롤링 정보가 700개가 넘는 정보임에도 불구하고 한번 파일을 만들기 위한 시간이 적어도 1분이상 걸리고 있습니다. 시간 단축을 위한 추가 코딩작업을 필요로 합니다.
로또API를 통한 크롤링 작업이 진행되므로 _의존성 주입_의 성격이 강합니다. 나중에 API기능이 비활성화 될 경우의 문제를 생각하여야 합니다.





### Update
해당 파일에는 두 가지 함수가 포함되어 있습니다.
* ReturnLastDrwNo
* UpdateExcel(drwNo)
입니다.









