
# 쇼핑몰 프로젝트

- 마케터로 일할 때 플랫폼 사용에 대한 한계로 아쉬웠던 경험이 많아 쇼핑몰을 첫 프로젝트로서 만들게 되었습니다.
- 또한 회원가입, 인증, 결제 및 CRUD 등 기초적이지만 중요한 기술들을 연습하기에 좋다고 생각했습니다.

## About

- 개발 기간 : 2023.05 ~ 
- 개발 인원 : 1명 (개인 프로젝트)
- 사이트 바로가기 : 👉 https://yohanyohan.com/
- Version 1 : 장고 템플릿을 이용해 fullstack 개발
- Version 2 :
	- 1. 기존 사이트는 유지하면서 DRF를 이용해 백엔드와 프론트 엔드 분리 (개발중)
	- 2. 유닛/통합 테스트 진행

## 목차
- [Version 1 실행 방법]
- [Version 1 소개] -> 장고 만으로 쇼핑몰 구축
- [Version 2 소개] -> REST-API 도 함께 동작 가능하도록 구축 (유닛테스트 & 통합테스트) (개발중)

## Version 1 기술스택

| 개발환경   | -                |
| ---------- | ---------------- |
| 언어       | Python - 3.11      |
| 프레임워크 | Django - 4.2.2      |
| DB         | PostgreSQL - 15.3 |
| API        |       카카오페이, PayPal, Daum 주소           |
| Devops           |    AWS - EC2, S3, RDS, Route53, VPC, IAM, Beanstalk               |


## Version 1 목차
- 1. [Project Structure](https://github.com/ramyo564/Upgrade_Django4/tree/main#1-project-structure)
- 2. [데이터베이스 테이블 구조](https://github.com/ramyo564/Upgrade_Django4/tree/main#2-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B2%A0%EC%9D%B4%EC%8A%A4-%ED%85%8C%EC%9D%B4%EB%B8%94-%EA%B5%AC%EC%A1%B0)
- 3. [Version 1 실행방법](https://github.com/ramyo564/Upgrade_Django4/tree/main#3-version-1-%EC%8B%A4%ED%96%89%EB%B0%A9%EB%B2%95)
- 4. [각 App의 기능 설명](https://github.com/ramyo564/Upgrade_Django4/tree/main#4-%EA%B0%81-app%EC%9D%98-%EA%B8%B0%EB%8A%A5-%EC%84%A4%EB%AA%85)
- 5. [이미지 및 소감](https://github.com/ramyo564/Upgrade_Django4/tree/main#5-%EC%9D%B4%EB%AF%B8%EC%A7%80-%EB%B0%8F-%EC%86%8C%EA%B0%90)

## 1. Project Structure
```
├─ accounts 
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ helpers.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ views_api.py
├─ carts
│  ├─ admin.py
│  ├─ apps.py
│  ├─ context_processors.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
├─ category
│  ├─ admin.py
│  ├─ apps.py
│  ├─ context_processors.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ views.py
│  └─ __init__.py
├─ data.json
├─ greatkart
│  ├─ asgi.py
│  ├─ settings.py
│  ├─ static
│  ├─ tests
│  │  ├─ conftest.py
│  │  ├─ factories.py
│  │  ├─ test_accounts
│  │  │  ├─ test_endpoints.py
│  │  │  ├─ test_forms.py
│  │  │  ├─ test_models.py
│  │  │  ├─ test_views.py
│  │  │  └─ __init__.py
│  │  └─ __init__.py
│  ├─ urls.py
│  ├─ views.py
│  ├─ wsgi.py
│  └─ __init__.py
├─ manage.py
├─ orders
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
├─ pytest.ini
├─ README.md
├─ requirements.txt
├─ static
├─ store
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
└─ templates
```


## 2. 데이터 베이스 테이블 구조

![UpgradeDjango4 drawio](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/9bd8a9ac-8b81-4491-a31f-60129e42553d)


## 3. Version 1 실행방법

## 실행방법 목차
[1. 프로젝트 다운로드](https://github.com/ramyo564/Upgrade_Django4/tree/main#1-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EB%8B%A4%EC%9A%B4%EB%A1%9C%EB%93%9C)

[2. 가상환경 셋팅](https://github.com/ramyo564/Upgrade_Django4/tree/main#2-%EA%B0%80%EC%83%81%ED%99%98%EA%B2%BD-%EC%85%8B%ED%8C%85)

[3. 환경설정](https://github.com/ramyo564/Upgrade_Django4/tree/main#3-%ED%99%98%EA%B2%BD%EC%84%A4%EC%A0%95)

### 1. 프로젝트 다운로드

1. 깃 레파지토리 선택 -> `Version_1_only_Django_Local`

![깃 레파지토리 선택](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/5a3648e0-9784-40eb-bc34-479425035623)

2. 파일 다운로드

![깃 다운로드](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/a1692a2e-f9a2-4ab0-882c-b9111a556a21)

### 2. 가상환경 셋팅

1. 로컬 환경에 파이썬이 설치되어 있다면 (3.11) 터미널에서 requirements.txt 가 있는 경로로 이동해 줍니다. 해당 경로에서 가상환경을 만들어줍니다.

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
### 3. 환경설정

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
  - http://127.0.0.1:8000/securelogin/ <- 진짜 어드민 페이지


6. API_KEY 설정

   - 로컬테스트에서 이메일 본인인증, 카카오페이, 페이팔 기능은 settings.py에서 따로 설정하셔야 합니다.
   - 로컬 환경에서 API_KEY를 설정 했을 경우 시범 영상 :
   - 동영상 👉👉👉  https://drive.google.com/file/d/16uyTOVPtCR6d_NeIkZWtBG7iAFALtgHX/view?usp=drive_link
   -  관리자 페이지 아이디와 비밀번호
```py
id : test@naver.com
pass : anwkrdnlqlalfqjsgh
```




### AWS Elastic Beanstalk 서비스 아키텍쳐

![Django4 쇼핑몰 AWS 아키텍쳐](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/e19728f1-ec2c-4357-a8bd-efe2fa8cf2f9)




## 4. 각 App의 기능 설명

## 목차
- [Version 1 처음 목차 돌아가기](https://github.com/ramyo564/Upgrade_Django4/tree/main#version-1-%EB%AA%A9%EC%B0%A8)
- [accounts](https://github.com/ramyo564/Upgrade_Django4/tree/main#accounts)
- [carts](https://github.com/ramyo564/Upgrade_Django4/tree/main#carts)
- [category](https://github.com/ramyo564/Upgrade_Django4/tree/main#category)
- [orders](https://github.com/ramyo564/Upgrade_Django4/tree/main#orders)
- [store](https://github.com/ramyo564/Upgrade_Django4/tree/main#store)




### accounts
```
├─ accounts 
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ helpers.py
│  ├─ models.py
│  ├─ serializers.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ views_api.py
```
- accounts 앱에서는 회원가입,로그인,로그아웃,대시보드,비밀번호 변경,재설정의 기능을 다루고 있습니다.
	- admin.py
		- AccountAdmin			
			- list_display : 관리자 페이지에서 사용자 프로필 목록에 표시할 정보 설정
			- list_display_links : 사용자 목록에서 특정 열을 클릭해서 사용자 상세 페이지로 이동할 수 있는 링크 설정
			- readonly_fields : 읽기 전용 필드로 사용자 계정에 대한 마지막 로그인 시간과 가입 날짜를 변경하지 못하도록 설정
			- ordering : 사용자 목록을 가입 날짜를 기준으로 내림차순으로 정렬
		- UserProfileAdmin
			- thumnail : 사용자 프로필 사진을 원형으로 표시하는 썸네일 이미지를 생성
			- list_display : 관리자 페이지에서 사용자 프로필 목록에 표시할 정보 설정
	- apps.py
		- AccountsConfig
			- default_auto_field : 모델 클래스에 대한 기본 자동 필드 타입을 지정
			- name : 앱의 이름을 지정, 해당 앱의 모든 기능과 리소스에 접근할 때 사용
	- forms.py
		- RegistrationForm
			- 사용자의 회원가입을 위한 폼 정의
			- 비밀번호와 확인 비밀번호 필드를 비교해 일치하는지 검사
			- 사용자의 이름, 성, 전화번호, 이메일, 비밀번호를 입력받음
			- 각 필드에 대한 플레이스 홀더와 클래스를 추가하고 필드들을 form-control 클래스로 스타일링
		- UserForm
			- 사용자 프로필 수정을 위한 폼 정의
			- 사용자의 이름과 성, 젆화번호를 수정할 수 있는 필드를 제공
			- 필드들을 form-control 클래스로 스타일링

	- models.py
		- MyAccountManager
			- create_user() : 사용자 생성을 담당하는 메서드
			- create_superuser() : 관리자 권한과 함께 슈퍼유저를 생성하고 저장
		- Account (AbstractBaseUser 상속)
			- 사용자 계정에 대한 정보 및 권한을 관리, AbstractBaseUser 를 상속받아 원하는 필드와 메서드를 추가로 정의 가능
			- 사용자 계정과 관련된 필드들과 권한 설정, 그리고 사용자 프로필과의 일대일 관계를 설정
		- UserProfile
			- 사용자의 프로필 정보, 프로필 사진, 주소등의 사용자 정보를 관리

	- urls.py
		- 클라이언트 요청을 처리하는 뷰에 있는 함수들과 연결

	- views.py
		- **`register`** : 사용자 회원가입을 처리하는 뷰, POST 요청을 통해 회원가입 정보를 받아 사용자 계정을 생성하고 이메일 인증 메일을 보내는 기능을 구현
		- **`login`** : 사용자 로그인을 처리하는 뷰. POST 요청을 통해 사용자의 이메일과 비밀번호를 받아 인증하고, 장바구니 정보를 사용자에게 연결하는 등의 기능도 포함
		- **`logout`** : 사용자 로그아웃을 처리하는 뷰. 인증된 사용자를 로그아웃시키고, 메시지를 표시
		- **`activate`** : 사용자 계정 활성화를 처리하는 뷰. 이메일 인증 링크를 통해 사용자 계정을 활성화하는 기능을 구현
		- **`dashboard`** : 사용자 대시보드 페이지를 보여주는 뷰. 사용자의 주문 목록과 프로필 정보를 표시
		- **`forgotPassword`** : 비밀번호 재설정을 위한 이메일 전송을 처리하는 뷰. 입력된 이메일로 비밀번호 재설정 링크를 보내는 기능을 구현
		- **`resetpassword_validate`** : 비밀번호 재설정을 위한 유효성 검사를 처리하는 뷰. 재설정을 위한 링크의 유효성을 검증하고 세션에 사용자 ID를 저장
		- **`resetPassword`** : 비밀번호를 재설정하는 뷰. 새로운 비밀번호를 입력받아 사용자의 비밀번호를 변경
		- **`my_orders`** : 사용자의 주문 목록을 보여주는 뷰
		- **`edit_profile`** : 사용자 프로필 정보를 수정하는 뷰. 사용자 정보와 프로필 정보를 입력받아 업데이트
		- **`change_password`** : 사용자의 비밀번호를 변경하는 뷰.
		- **`order_detail`** : 주문 상세 정보를 보여주는 뷰. 주문에 대한 상세 정보와 총 가격을 표시.

### carts
```
├─ carts
│  ├─ admin.py
│  ├─ apps.py
│  ├─ context_processors.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  └─ views.py
```

- carts 앱에서는 장바구니 기능을 다루고 있습니다.

	- context_processors.py
		- 장바구니 아이템 수를 계산해서 웹 페이지에 표시하는 기능을 구현
			- `cart_count` 변수를 초기화
			- 현재 요청의 경로(`request.path`)에 "admin"이 포함되어 있으면 빈 딕셔너리를 반환하여 관리자 페이지에서는 아무 작업도 수행 하지 않음.
			- 그렇지 않은 경우, 사용자의 장바구니를 확인하고 장바구니에 담긴 아이템 수를 계산
			- 사용자가 인증되어 있다면 해당 사용자와 연관된 장바구니 아이템을 검색하고, 그렇지 않으면 세션에 연결된 장바구니에서 아이템을 가져옴
			- 검색된 장바구니 아이템의 수량(`quantity`)을 더하여 `cart_count`를 계산
			- 장바구니가 없는 경우(`Cart.DoesNotExist` 예외) `cart_count`를 0으로 설정
			- 마지막으로, `cart_count`를 딕셔너리 형태로 반환하여 템플릿에서 장바구니 아이템 수를 표시
	- models.py
		-  Cart 
			- `cart_id`: 최대 250자까지의 문자열을 저장하는 필드로, 장바구니를 식별하는 고유한 식별자를 저장.
			- `date_added`: 아이템을 장바구니에 추가한 날짜를 자동으로 기록하는 필드로, `auto_now_add=True` 속성이 있다. 즉, 아이템을 추가할 때마다 현재 날짜 저장
			- `__str__(self)`: 객체를 문자열로 표현할 때 사용되며, 이 메서드를 통해 장바구니 객체를 식별하는 데 사용되는 `cart_id`를 반환
		- CartItem
			- `user`: `Account` 모델과의 외래 키 관계로, 사용자와 장바구니 아이템 간의 관계 ->> 사용자가 인증되어 있지 않은 경우 `null=True`로 설정
			- `product`: `Product` 모델과의 외래 키 관계로, 장바구니에 추가된 상품을 가져옴
			- `variations`: `Variation` 모델과의 Many-to-Many 관계로, 상품의 옵션 값(variation)을 나타낸다. 여러 옵션이 선택될 수 있으므로 `blank=True`로 설정
			- `cart`: `Cart` 모델과의 외래 키 관계로, 장바구니 아이템이 어떤 장바구니에 속하는지 나타냄. 사용자가 인증되어 있지 않은 경우 `null=True`로 설정
			- `quantity`: 장바구니에 추가된 특정 상품의 수량을 저장하는 필드로, 정수형으로 설정
			- `is_active`: 장바구니 아이템의 활성 여부를 나타내는 필드로, 기본값은 `True`로 설정
			- `sub_total(self)`: 장바구니 아이템의 총 가격을 계산하여 반환하는 메서드로, 상품의 가격(`product.price`)과 수량(`quantity`)을 곱한 값을 반환
	- views.py
		- `_cart_id(request)`:
			- 현재 세션에서 장바구니 식별자(`cart_id`)를 검색하거나 생성하여 반환
		- `add_cart(request, product_id)`:
			- 특정 상품을 장바구니에 추가
			- 인증된 사용자와 비인증된 사용자 각각을 고려하여 상품과 상품 변형(variation)을 처리
			- 이미 장바구니에 있는 상품인 경우 수량을 증가시키고, 그렇지 않은 경우 장바구니에 새로운 아이템을 추가
		-  `remove_cart(request, product_id, cart_item_id)`:
			- 장바구니에서 특정 상품의 수량을 1만큼 감소
			- 수량이 1인 경우 해당 아이템을 장바구니에서 제거
		- `remove_cart_item(request, product_id, cart_item_id)`:
			- 장바구니에서 특정 상품 아이템을 완전히 제거
		- `cart(request, total=0, quantity=0, cart_items=None)`:
			- 장바구니 페이지를 렌더링하고 장바구니에 있는 상품들을 표시
			- 인증된 사용자와 비인증된 사용자 각각을 고려하여 장바구니 내역을 가져옴
			- 상품 가격과 수량을 계산하여 총 가격 및 부가가치세를 계산
		- `checkout(request, total=0, quantity=0, cart_items=None)`:
			- 결제 페이지를 렌더링하고 장바구니에 있는 상품들을 표시
			- 인증된 사용자와 비인증된 사용자 각각을 고려하여 장바구니 내역을 가져옴
			- 상품 가격과 수량을 계산하여 총 가격 및 부가가치세를 계산
			- 로그인된 사용자만 결제 페이지에 액세스할 수 있도록 `@login_required` 데코레이터를 사용

### category
```
├─ category
│  ├─ admin.py
│  ├─ apps.py
│  ├─ context_processors.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ views.py
│  └─ __init__.py
```

- category 앱에서는 상품 목록을 관리하는 기능을 다루고 있습니다.
	- context_processors.py
		- `Category` 모델을 이용하여 모든 카테고리 목록을 `links` 변수에 저장
		- `links` 변수는 템플릿 컨텍스트에 추가되어, 웹 페이지에서 이 함수를 호출할 때 카테고리 목록을 사용
	- models.py
		- `category_name`: 
			- 최대 50자까지의 문자열을 저장하는 필드로, 카테고리의 이름을 나타냄
		- `slug`: 
			- 최대 100자까지의 Slug 문자열을 저장하는 필드로, 카테고리의 URL을 나타내고 `allow_unicode=True` 설정으로 유니코드 문자도 허용
		- `description`: 
			- 최대 255자까지의 텍스트를 저장하는 필드로, 카테고리에 대한 간단한 설명을 나타냄
		- `cat_image`: 
			- 카테고리에 대한 이미지를 업로드하는 필드로, 이미지는 "photos/categories" 디렉토리에 저장
		- `get_url(self)`: 
			- 카테고리의 URL을 반환하는 메서드로, `reverse` 함수를 사용하여 "products_by_category" 뷰와 연결된 URL을 생성
		- `__str__(self)`: 
			- 모델 객체를 문자열로 표현할 때 사용되며, 카테고리의 이름을 반환
		- `save(self, force_insert=False, force_update=False, using=None, update_fields=None)`: 
			- 모델 객체가 저장될 때 호출되는 메서드로, 카테고리 이름을 Slug로 변환하여 저장, Slugify 함수는 유니코드 문자도 허용하며, 부모 클래스의 `save` 메서드를 호출하여 저장 작업을 완료

 ### orders
```
├─ orders
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
```


- orders 앱에서는 주문,결제와 관련된 기능을 다루고 있습니다.
	- models.py
		- Payment
			- `user`: 주문을 한 사용자와의 외래 키 관계, 주문을 한 사용자를 참조
			- `payment_id`: 최대 100자까지의 문자열을 저장하는 필드로, 결제 식별자 기록
			- `payment_method`: 최대 100자까지의 문자열을 저장하는 필드로, 결제 방법
			- `amount_paid`: 최대 100자까지의 문자열을 저장하는 필드로, 결제한 총 금액
			- `status`: 최대 100자까지의 문자열을 저장하는 필드로, 결제 상태를 나타냄
			- `created_at`: 결제 정보가 생성된 날짜와 시간을 자동으로 기록하는 필드
			- `__str__(self)`: 객체를 문자열로 표현할 때 사용되며, 결제 식별자인 `payment_id`를 반환
		- OrderProduct
			- `order`: 주문과 상품 간의 관계를 나타내는 외래 키, 해당 주문을 참조
			- `payment`: 주문과 결제 정보 간의 외래 키 관계, 해당 주문과 관련된 결제를 참조
			- `user`: 주문한 사용자와의 외래 키 관계, 주문한 사용자를 참조
			- `product`: 주문한 상품과의 외래 키 관계로, 주문에 포함된 상품을 참조
			- `variations`: 상품의 옵션을 나타내는 Many-to-Many 관계로, 여러 변형 선택 가능
			- `quantity`: 주문한 상품의 수량을 나타내는 필드
			- `product_price`: 상품의 가격을 나타내는 필드
			- `ordered`: 주문이 완료된 상태인지 여부를 나타내는 불리언 필드
			- `created_at`: 주문 상품이 생성된 날짜와 시간을 자동으로 기록하는 필드
			- `updated_at`: 주문 상품 정보가 업데이트된 날짜와 시간을 자동으로 기록하는 필드
	-  views.py
		- `kakao_pay`:
			- POST 요청을 처리하여 KaKao Pay 결제를 시작
			- 현재 사용자의 카트 아이템을 검사하여, 카트에 상품이 있는지 확인
			- 결제할 상품의 총 가격을 계산하고 KaKao Pay 결제를 위한 정보를 준비
			- KaKao Pay API를 사용하여 결제 요청을 보내고, 결제 준비 URL로 리디렉션
		- `kakao_pay_approval` :
			- KaKao Pay 결제가 완료된 후, KaKao Pay에서 리디렉션되어 이 뷰를 호출
			- KaKao Pay API를 통해 결제를 승인하고, 결제 정보를 저장
			- 주문을 완료 상태로 변경하고, 카트 아이템을 주문 상품으로 이동하고, 상품 재고를 감소
			- 결제가 완료된 주문 정보를 템플릿으로 렌더링하여 사용자에게 표시
		- `kakao_pay_cancel`
			- KaKao Pay 결제가 취소된 경우를 처리하는 뷰
			- 결제 실패 페이지를 렌더링하여 사용자에게 표시
		- `payments`:
			- 주문이 완료된 후, PayPal 및 KaKao Pay 결제 정보를 처리하는 뷰
			- 주문 정보와 결제 정보를 저장하고, 카트 아이템을 주문 상품으로 이동하고, 상품 재고를 감소
			- 주문 완료 이메일을 사용자에게 보내고, 주문 번호 및 트랜잭션 ID를 JSON 응답으로 반환.
		- `place_order`:
			- 주문을 생성하는 뷰
			- 주문 폼을 통해 제출된 데이터를 처리하고, 주문 정보를 저장
			- 주문 번호를 생성하고, 주문 정보를 렌더링하여 사용자에게 표시
		- `order_complete`:
			- 주문이 완료된 후, 주문 완료 페이지를 렌더링하는 뷰
			- 주문 및 결제 정보를 템플릿으로 렌더링하여 사용자에게 표시


### store
```
├─ store
│  ├─ admin.py
│  ├─ apps.py
│  ├─ forms.py
│  ├─ models.py
│  ├─ tests.py
│  ├─ urls.py
│  ├─ views.py
│  └─ __init__.py
└─ templates
```

- store 앱에서는 상품 페이지에서 수행하는 것과 관련된 기능을 다루고 있습니다 (검색, 상품 상세페이지, 리뷰)
	- models.py
		- Product
			- `Product` 모델은 스토어에서 판매되는 제품 정보를 나타냄 , 제품 이름, 설명, 가격, 이미지, 재고량, 사용 가능 여부 등의 필드를 갖고 있음
			- `category` 필드는 외래 키(ForeignKey)로 카테고리 모델과 연결되어 해당 제품이 어떤 카테고리에 속하는지를 나타냄
			- `get_url` 메서드는 제품의 상세 페이지 URL을 생성
			- `averageReview` 메서드는 해당 제품의 리뷰 평균 평점을 계산
			- `countReview` 메서드는 해당 제품에 대한 리뷰 수를 계산

		- Variation
			- `Variation` 모델은 제품의 다양한 변형(색상, 크기 등)을 나타냄
			- `product` 필드는 외래 키로 해당 변형이 어떤 제품에 속하는지를 나타냄
			- `variation_category` 필드는 변형의 카테고리(색상 또는 크기)를 나타냄
			- `variation_value` 필드는 변형의 값(예: "Red" 또는 "Large")을 저장

		- ReviewRating
			- `ReviewRating` 모델은 제품에 대한 리뷰 및 평점 정보를 저장
			- `product` 필드는 외래 키로 어떤 제품에 대한 리뷰인지를 연결
			- `user` 필드는 외래 키로 리뷰를 작성한 사용자를 연결
			- `rating` 필드는 리뷰의 평점을 저장
			- `status` 필드는 리뷰의 상태를 나타냄(기본값은 True로 설정되어 있음)

		- ProductGallery
			- `ProductGallery` 모델은 제품의 갤러리 이미지를 관리
			- `product` 필드는 외래 키로 어떤 제품의 갤러리 이미지인지를 연결
			- `image` 필드는 이미지 파일을 저장
	- views.py
		- `store` : 
			- 온라인 스토어의 제품 목록을 표시, 카테고리별로 필터링되며, 카테고리 슬러그와 함께 URL을 통해 전달 및 상품 목록을 페이지별로 표시하고, 옵션(색상 및 크기)을 수집하여 필터링 옵션을 제공
		- `update_results`: 
			- 제품 목록을 필터링하고 정렬하는 기능을 제공, 이 함수는 AJAX를 통해 호출되며, 선택한 옵션과 정렬 기준에 따라 결과를 업데이트
		- `product_detail` : 
			- 특정 제품의 상세 정보 페이지를 표시. 제품 카테고리 슬러그와 제품 슬러그를 사용하여 제품을 식별. 장바구니에 제품을 추가할 수 있는 옵션과 사용자 리뷰 및 제품 갤러리를 표시
		- `search` : 
			- 제품 검색을 처리하고 키워드에 따라 제품을 검색하여 결과를 표시
		-  `submit_review` : 
			- 사용자 리뷰를 제출하거나 업데이트하는 기능을 제공 제품 페이지에서 리뷰를 작성하고 제출할 때 호출

## 5. 이미지 및 소감

## 목차
- [Version 1 처음 목차 돌아가기](https://github.com/ramyo564/Upgrade_Django4/tree/main#version-1-%EB%AA%A9%EC%B0%A8)
- [User](#user)
	- 로그인 / 로그아웃
	- 회원가입 
		- 이메일 토큰 링크를 통한 본인인증
	- 대시보드
		- 프로필, 마이페이지, 주문조회
- [Review](#review)
	- 각 리뷰 평균 및 카운팅
	- 회원 및 구매한 이력이 있을 경우만 댓글 달기 가능
- [Search](#search)
	- 쿼리에 걸리는 아이템 갯수 카운팅
	- 검색 기능
- [Payment](#payment)
	- SDK 와 REST API 두 가지 방법으로 개발
		- SDK 는 PayPal
  		- REST API 는 카카오 페이 
- [Paginator](#paginator)
	- Paginator 내장 함수로 구현
- [Cart](#cart)
	- 장바구니에서 아이템 추가 및 삭제
	- 세션을 통해 로근인 했을 때 중복된 상품이 있을 경우 상품 증가
	- 그렇지 않은 경우 장바구니에 새로 추가
	- 주소 찾기는 Daum API로 구현
- [Sort by](#sort-by)
	- 카테고리 및 필터기능 적용
		 - 폼 형식으로 랜더링

## User

> 1. 장고의 기본 BaseUserManager, AbstractBaseUser 를 이용해서 회원가입 모델을 구현했습니다.
> 2. 핸드폰 번호의 유효성 검사의 경우 `PhoneNumberField` 라이브러리를 사용해 구현했습니다.
> 3. 회원가입을 할 때 가입한 이메일로 토큰을 보내고 해당 링크로 접속했을 때의 pk와 토큰이 일치할 경우에만 본인인증이 확인되어 계정이 활성화 되도록 구현했습니다.

### 회원가입 및 본인인증
- 비밀번호 일치 및 핸드폰, 이메일 유효성 검사를 구현했습니다.
- 회원가입을 했을 경우 본인인증된 이메일을 통해서만 계정이 활성화 됩니다.
	- 회원 가입시 기재한 이메일 주소로 토큰과 uid와 대조하여 본인 인증을 진행합니다.

![register](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/22cbe0ec-4c48-4646-86e9-1deb2a45b891)


### 비밀번호 찾기
- 가입한 이메일 주소가 존재할 경우 해당 이메일이 전송됩니다.
- 회원가입과 같은 방식으로 본인인증이 진행되며 본인인증이 완료되면 새로운 비밀번호를 설정 할합니다.
- 새로운 비밀번호로 로그인에 성공하면 계정이 다시 활성화됩니다.

![비밀번호 찾기](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/16402f92-ec52-45eb-8ade-040bc6249c5f)


### 프로필 사진 및 비밀번호 변경

- 회원가입 때 기본으로 생성된 프로필이 변경 가능하며 비밀번호도 변경이 가능합니다.

![프로필 사진 및 비밀번호 변경](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/51bba84e-c82c-4d4c-98cb-d6d91372b1b6)


### 주문번호 확인

![주문번호 확인](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/75eeab29-e69c-479c-999a-b31682f457b4)


## Review

> Review 기능은 크게 두 가지로 나눠서 살펴볼 수 있습니다.
> 	1. 회원과 비회원 그리고 구매자와 비 구매자를 각각 나눠서 유저의 경로가 달라집니다.
> 	2. 아이템마다 각각 달리는 리뷰 개수 와 총 별점의 평균을 나타냅니다.


### 비회원일 때 댓글을 달 수 없는 기능

- 로그인이 되어있지 않은 경우 로그인 페이지가 나옵니다.
- 로그인이 되어있는 상태이지만 물건을 구매한 적이 없다면 리뷰를 달 수 없습니다.

## 페이지

### 회원일 때 댓글을 달 수 있는 기능

![댓글 달기](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/076be1fd-0784-4933-85ec-23e49fbbc3ec)

- 회원일 경우 리뷰를 남길 수 있으며 리뷰를 남김과 동시에 제품에 총 리뷰 개수가 카운팅 되며 별점은 전체 별점 총 평균에 반영됩니다.

### 평균 별점 반영 및 리뷰 개수 카운팅

![평균 별점 계산 카운팅](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/34c5ac3f-9269-4dca-b266-e3a44e769292)



## Search

> 검색 기능은 판매자가 상품을 등록할 때 설명이나 제품명이 키워드에 걸리면 반영해 주는 쿼리를 반영합니다.
> 해당 쿼리에 걸리는 상품 개수를 카운팅 합니다.

![검색기능](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/ff3d5d8a-0247-4728-a18c-54f4b494ec8a)


## Payment
>  결제 방식은 SDK 와 REST API 두 가지 방법을 사용했고
>  SDK 방식은 페이팔, REST API 방식은 카카오 페이를 선택했습니다.

### 카카오페이 

![카카오페이 결제](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/b814cd6a-0692-42bc-b81b-115e1a059cfd)


### 페이팔 

![페이팔 결제](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/0a4061ad-65dd-4a76-8dc8-ebc3afb5cc58)



## Paginator 
> 장고에서 제공하는 Paginator를 사용하여 페이지 단위를 구현했습니다.  

![페이지네이션](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/3a4ca17b-e9db-4b55-a83d-2a4add264263)


## Cart

> 1. 장바구니에서 아이템 추가 및 삭제를 구현했습니다.
> 2. 세션을 활용하여 비로그인 상태에서 장바구니에 물건을 담았다가 로그인을 했을 때 중복된 상품이 있을 경우는 해당 상품의 개수가 늘어나고 그렇지 않은 경우에는 새로 장바구니에 추가되도록 구현했습니다.
> 3. 주소 찾기는 DAUM API를 이용했습니다. 

![장바구니](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/c4783734-02a4-408f-aed8-b3fea6764b61)


## Sort by

> 상품을 필터링할 때 다음과 같은 알고리즘으로 만들었습니다.

![상품 알고리즘](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/3616acc6-fd8a-48a0-8e8a-0153f8b5e39d)

( 개발할 당시에는 자료구조에 대해 잘 몰라서 if문으로만 구현했지만 이번에 자료구조를 공부하면서 더 좋은 방법으로 만들 수 있을 것 같아 DRF 버전을 개발할 때 적용하려고 합니다!)

## 카테고리 및 필터링 적용

![카테고리 기능 및 필터링 기능](https://github.com/ramyo564/Upgrade_Django4/assets/103474568/7931c64d-2549-4096-accf-bff84d04ea04)


## 느낀점

막상 시작해 보니 생각보다 모르는 게 너무 많았고
특히 프론트 쪽의 자바스크립트가 정말 어려웠습니다.
단순히 AWS를 통해 서버를 올리는 것에도 정말 많은 오류들을 만났고
구글링을 하면서 1주일 정도 걸렸던 것 같습니다.

분명 어려운 도전이였지만 많은 걸 배울 수 있어서 재밌었습니다.
