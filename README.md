# CookieRunKingdom-Coupon
<div>
<img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fhappylie%2FCookieRunKingdom-Coupon&count_bg=%2379C83D&title_bg=%23555555&icon=github.svg&icon_color=%23E7E7E7&title=view&edge_flat=false"/>
<img src="https://img.shields.io/badge/Python->=3.5-blue?logo=python&logoColor=white" />
</div>

쿠키런 킹덤 쿠폰 손쉬운 입력 Tool
- https://happylie.tistory.com/136

## 쿠키런 킹덤 쿠폰 입력 Tool
### 설치 방법
1. Git Clone
```
$ https://github.com/happylie/CookieRunKingdom-Coupon.git
```
2. Requirements 설치
```
$ pip install -r requirements.txt
```
### 실행 방법
1. Help
```
$ python run.py -h                 
usage: Cookie Run Kingdom Coupon [-h] [-c COUPON_CODE] [-v]

쿠키런 킹덤 쿠폰 등록

optional arguments:
  -h, --help            show this help message and exit
  -c COUPON_CODE, --coupon COUPON_CODE
                        쿠키런 킹덤 쿠폰 번호
  -v, --version         show program's version number and exit
```
2. 쿠폰 등록 유저 등록
```
run.py 파일에서 15번째줄에 있는 user_data = ['GUEST-XXXXXXXX', 'aaa@aaa.com'] 과 같이 본인 유저 정보를 입력 한다.  
```
3. 쿠폰 등록
```
$ python run.py -c DEVNOW40MKINGDOM
GUEST-XXXXXXXX :: 상품이 정상적으로 지급되었습니다.
aaa@aaa.com :: DevPlay 계정을 다시 한번 확인해주세요.
```