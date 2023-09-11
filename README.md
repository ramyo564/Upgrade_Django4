
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
(작업중)

### 데이터 베이스 테이블 구조

![UpgradeDjango4 drawio](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/9bd8a9ac-8b81-4491-a31f-60129e42553d)

### AWS Elastic Beanstalk 서비스 아키텍쳐

![Django4 쇼핑몰 AWS 아키텍쳐](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/e19728f1-ec2c-4357-a8bd-efe2fa8cf2f9)


### Version 1 Structure




