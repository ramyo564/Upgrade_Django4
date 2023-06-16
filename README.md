쇼핑몰 웹 페이지이며 아래와 같은 기능들을 구현했습니다.

- [Review](#review)
- [Search](#search)
- [Payment](#payment)
- [Pagenator](#pagenator)
- [Cart](#cart)
- [Sort by](#sort-by)
- [User](#user)

# About

개발 기간 : 2023.05 ~ 2023.06   
개발 인원 : 1명 (개인 프로젝트)

| 개발환경   | -                |
| ---------- | ---------------- |
| 언어       | Python - 3.11      |
| 프레임워크 | Django - 4.2.2      |
| DB         | PostgreSQL - 15.3 |
| API        |       카카오페이, PayPal, Daum 주소           |
| Devops           |    AWS - EC2, S3, RDS, Route53, VPC, IAM, Beanstalk               |

## Review

> Review 기능은 크게 두 가지로 나눠서 살펴볼 수 있습니다.
> 	1. 회원과 비회원 그리고 구매자와 비 구매자를 각각 나눠서 유저의 경로가 달라집니다.
> 	2. 아이템마다 각각 달리는 리뷰 개수 와 총 별점의 평균을 나타냅니다.


### 비회원일 때 댓글을 달 수 없는 기능

![](https://i.imgur.com/MlAW39u.gif)
- 로그인이 되어있지 않은 경우 로그인 페이지가 나옵니다.
- 로그인이 되어있는 상태이지만 물건을 구매한 적이 없다면 리뷰를 달 수 없습니다.


### 회원일 때 댓글을 달 수 있는 기능
![](https://i.imgur.com/oK37hjD.gif)
- 회원일 경우 리뷰를 남길 수 있으며 리뷰를 남김과 동시에 제품에 총 리뷰 개수가 카운팅 되며 별점은 전체 별점 총 평균에 반영됩니다.

### 평균 별점 반영 및 리뷰 개수 카운팅
![](https://i.imgur.com/bfLz6oI.gif)



## Search

> 검색 기능은 판매자가 상품을 등록할 때 설명이나 제품명이 키워드에 걸리면 반영해 주는 쿼리를 반영합니다.
> 해당 쿼리에 걸리는 상품 개수를 카운팅 합니다.

![](https://i.imgur.com/vNByR9X.gif)

## Payment
>  결제 방식은 SDK 와 REST API 두 가지 방법을 사용했고
>  SDK 방식은 페이팔, REST API 방식은 카카오 페이를 선택했습니다.

### 카카오페이 

![](https://i.imgur.com/Uvn04uA.gif)

### 페이팔 

![](https://i.imgur.com/bubUb5w.gif)


## Pagenator
> 장고에서 제공하는 Paginator를 사용하여 페이지 단위를 구현했습니다.  

![](https://i.imgur.com/52uAjlm.gif)

## Cart

> 1. 장바구니에서 아이템 추가 및 삭제를 구현했습니다.
> 2. 세션을 활용하여 비로그인 상태에서 장바구니에 물건을 담았다가 로그인을 했을 때 중복된 상품이 있을 경우는 해당 상품의 개수가 늘어나고 그렇지 않은 경우에는 새로 장바구니에 추가되도록 구현했습니다.
> 3. 주소 찾기는 DAUM API를 이용했습니다. 

![](https://i.imgur.com/KnIAk86.gif)

## Sort by

> 상품을 필터링할 때 다음과 같은 알고리즘으로 만들었습니다.

![](https://i.imgur.com/qdiJxze.png)



![](https://i.imgur.com/s6p3mMl.gif)



## User

> 1. 장고의 기본 BaseUserManager, AbstractBaseUser 를 이용해서 회원가입 모델을 구현했습니다.
> 2. 핸드폰 번호의 경우 `PhoneNumberField` 라이브러리를 사용해 유효성을 구현했습니다.
> 3. 회원가입을 할 때 사용한 이메일로 토큰을 보내고 해당 링크로 접속할 때의 pk와 토큰이 일치하도록 하여 본인인증이 될 경우에만 계정이 활성화 되도록 구현했습니다.

### 회원가입 및 본인인증

![](https://i.imgur.com/9sD4UjO.gif)

### 비밀번호 찾기
- 가입한 이메일 주소가 존재할 경우 해당 이메일이 전송됩니다.
- 회원가입과 같은 방식으로 본인인증이 진행되며 본인인증이 완료되면 새로운 비밀번호를 설정 할합니다.
- 새로운 비밀번호로 로그인에 성공하면 계정이 다시 활성화됩니다.

![](https://i.imgur.com/CTAytbI.gif)

### 프로필 사진 및 비밀번호 변경

- 회원가입 때 기본으로 생성된 프로필이 변경가능하며 비밀번호도 변경이 가능합니다.

![](https://i.imgur.com/Pssv5z9.gif)

### 주문번호 확인

![](https://i.imgur.com/7tOYvOQ.gif)
