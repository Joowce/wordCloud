# word-cloud
> 키워드를 검색해  나온 뉴스를 스크랩해서 word cloud를 만드는 프로그램
> lambda 및 aws service를 이용해 architecture 구성

## requirements
```
python 3
docker
java
```
> **docker** 는 serverless-python-requirements에서 package를 설치하고 lambda 코드를 packaing할 때 필요합니다
> **java**는 형태소 분석기인 **konlpy** package에서 필요로 합니다

## install & deploy
```
npm install
npm run deploy
```

- - - -
## TO-DO
* 스크랩한 뉴스 전문또한 **s3**에 저장
* api gateway를 달아서 **Rest API**화 할 것
* npm script 로컬 invoke 추가할 것 (docker에 lambda 컨테이너 띄워서 실행)
* 메일 주소를 parameter로 받아서 word-cloud를 s3저장이 아닌 메일로 전송할 것