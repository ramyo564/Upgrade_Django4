
# 쇼핑몰 프로젝트

- 마케터로 일할 때 플랫폼 사용에 대한 한계로 아쉬웠던 경험이 많아 쇼핑몰을 첫 프로젝트로서 만들게 되었습니다.
- 또한 회원가입,인증, 결제 및 CRUD 등 기초적이지만 중요한 기술들을 연습하기에 좋다고 생각했습니다.

## About

개발 기간 : 2023.05 ~ 
개발 인원 : 1명 (개인 프로젝트)
사이트 바로가기 : 👉 https://yohanyohan.com/
Version 1 : 장고 템플릿을 이용해 fullstack 개발
Version 2 : 1. 기존 사이트는 유지하면서 DRF를 이용해 백엔드와 프론트 엔드 분리 (개발중)
	    2. 유닛/통합 테스트 진행

## 목차
- [Version 1 실행 방법]
- [Version 1 소개]
- [Version 2 소개]

## Version 1 기술스택

| 개발환경   | -                |
| ---------- | ---------------- |
| 언어       | Python - 3.11      |
| 프레임워크 | Django - 4.2.2      |
| DB         | PostgreSQL - 15.3 |
| API        |       카카오페이, PayPal, Daum 주소           |
| Devops           |    AWS - EC2, S3, RDS, Route53, VPC, IAM, Beanstalk               |


## Version 1 목차
- Version 1 실행방법
- 데이터베이스 테이블 구조
- AWS Elastic Beanstalk 서비스 아키텍쳐
- Version 1 Structure


### Version 1 실행방법
#### 1. 프로젝트 다운로드

1. 깃 레파지토리 선택 -> `Version_1_only_Django_Local`

![깃 레파지토리 선택](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/5a3648e0-9784-40eb-bc34-479425035623)

2. 파일 다운로드

![깃 다운로드](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/a1692a2e-f9a2-4ab0-882c-b9111a556a21)

#### 2. 가상환경 셋팅

1. 로컬환경에 파이썬이 설치되어 있다면 (3.11) 터미널에서 requirements.txt 가 있는 경로로 이동해줍니다. 해당 경로에서 가상환경을 만들어줍니다.

```
python -m venv venv
```
![가상환경 셋팅](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/df3806c8-2781-4669-9a0e-39fc5c6b4d4a)


2. 가상환경 활성화

  - Windows
```
source venv/Scripts/activate
```
  - Mac
```
source venv/bin/activate
```

- 올바르게 실행 되었다면 터미널에 (venv)라고 터미널창에서 확인 가능합니다.

----- 
#### 4. 환경설정

1. 가상환경이 활성화 되어있다면 현재 라이브러리 목록을 확인해줍니다.

```python
pip list
```
  - 새로운 환경이므로 Package 리스트에 pip, setuptools 만 보이면 정상입니다.

![pip 리스트](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/bb67b0a6-097b-4417-bfb1-c52a60e4466d)


2. 필요한 라이브러리를 설치

```python
pip install -r requirements.txt
```

  - 설치시 몇 분 걸릴 수 있습니다.
  - 다시 pip list를 통해 requirements.txt에 있는 목록과 일치하는지 확인해줍니다.     

3. superuser 

```python
ID : test@naver.com
PASS : anwkrdnlqlalfqjsgh
```

4. Run server

  - 마이그레이션이 끝났다면 아래의 명령어를 실행해서 서버를 실행!

```python
python manage.py runserver
```


5. Admin page

  - http://127.0.0.1:8000/admin/ 은 fake 어드민 페이지입니다.
  - 위 주소로 로그인 시도를 하면 IP가 남도록 되어있고 해당 IP를 차단시켜 접속을 제한할 수 있습니다.
  - admin 페이지를 확인하시려면 밑의 주소로 접속하시면 됩니다.

```python
(http://127.0.0.1:8000/securelogin/)
```





### 데이터 베이스 테이블 구조

![UpgradeDjango4 drawio](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/9bd8a9ac-8b81-4491-a31f-60129e42553d)

### AWS Elastic Beanstalk 서비스 아키텍쳐

![Django4 쇼핑몰 AWS 아키텍쳐](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/e19728f1-ec2c-4357-a8bd-efe2fa8cf2f9)


### Version 1 Structure




