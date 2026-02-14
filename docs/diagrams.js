export const diagrams = {
    'upgrade-django-system-architecture': `
        graph LR
        User[Client Browser] --> Route53[Route53 DNS]
        Route53 --> EB[AWS Elastic Beanstalk]

        subgraph EBHost [EB EC2 Runtime]
            Nginx[Nginx Proxy]
            Django[Django App Server]
        end

        EB --> Nginx
        Nginx --> Django

        Django --> RDS[(RDS PostgreSQL)]
        Django --> S3[(S3 Static/Media)]
        Django --> SMTP[Email Provider]
        Django --> PayPal[PayPal SDK]
        Django --> Kakao[KakaoPay REST API]

        AdminAttack[/admin attempt/] --> Honeypot[admin_honeypot]
        SecureAdmin[/securelogin/] --> Django

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        classDef g fill:#161b22,stroke:#238636,color:#c9d1d9
        classDef o fill:#161b22,stroke:#d29922,color:#c9d1d9
        class User,Route53,EB,Nginx,Django b
        class RDS,S3,SMTP g
        class PayPal,Kakao,Honeypot,SecureAdmin o
    `,

    'django-architecture-overview': `
        graph TD
        Root[greatkart root project] --> Accounts[accounts app]
        Root --> Store[store app]
        Root --> Carts[carts app]
        Root --> Orders[orders app]
        Root --> Category[category app]
        Root --> Tests[greatkart tests]

        Accounts --> AccountViews[views.py and views_api.py]
        Store --> StoreViews[store views and filters]
        Carts --> CartViews[session cart views]
        Orders --> OrderViews[payment and order views]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        classDef g fill:#161b22,stroke:#238636,color:#c9d1d9
        class Root,Accounts,Store,Carts,Orders,Category b
        class AccountViews,StoreViews,CartViews,OrderViews,Tests g
    `,

    'django-app-architecture': `
        graph TB
        URLRoot[greatkart urls.py] --> Web[Template Web Routes]
        URLRoot --> Api[DRF Router /api]

        Web --> AccountsWeb[accounts views]
        Web --> StoreWeb[store views]
        Web --> CartsWeb[carts views]
        Web --> OrdersWeb[orders views]

        Api --> AccountViewSet[accounts views_api AccountViewSet]
        AccountViewSet --> SerializerLayer[serializers validation]
        SerializerLayer --> AccountModel[(Account model)]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        classDef g fill:#161b22,stroke:#238636,color:#c9d1d9
        class URLRoot,Web,Api,AccountsWeb,StoreWeb,CartsWeb,OrdersWeb b
        class AccountViewSet,SerializerLayer,AccountModel g
    `,

    'auth-account-model': `
        graph LR
        RegisterForm[RegistrationForm] --> AccountCreate[Account create inactive]
        AccountCreate --> ProfileCreate[UserProfile default avatar]
        AccountCreate --> EmailToken[default_token_generator]
        EmailToken --> ActivationLink[uidb64 and token link]
        ActivationLink --> Activate[activate view]
        Activate --> ActiveUser[is_active true]

        Login[auth.authenticate email password] --> MergeHook[session cart merge]
        Login --> SessionLogin[auth.login session]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        classDef o fill:#161b22,stroke:#d29922,color:#c9d1d9
        class RegisterForm,AccountCreate,ProfileCreate,EmailToken,ActivationLink,Activate,ActiveUser b
        class Login,MergeHook,SessionLogin o
    `,

    'request-routing-map': `
        graph TB
        Client[HTTP Request] --> RootUrls[greatkart urls.py]

        RootUrls --> StoreUrls[store urls]
        RootUrls --> CartUrls[carts urls]
        RootUrls --> AccountUrls[accounts urls]
        RootUrls --> OrderUrls[orders urls]
        RootUrls --> ApiUrls[api router and schema]

        StoreUrls --> StoreViews[store, product_detail, search, update_results, submit_review]
        CartUrls --> CartViews[add/remove cart, checkout]
        AccountUrls --> AccountViews[register, login, activate, reset, dashboard]
        OrderUrls --> OrderViews[place_order, payments, kakao_pay, order_complete]
        ApiUrls --> AccountAPI[AccountViewSet actions]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class Client,RootUrls,StoreUrls,CartUrls,AccountUrls,OrderUrls,ApiUrls b
    `,

    'commerce-data-model': `
        graph LR
        Account[(Account)] --> CartItem[(CartItem)]
        Cart[(Cart session id)] --> CartItem
        Product[(Product)] --> CartItem
        Product --> Variation[(Variation)]

        Account --> Order[(Order)]
        Order --> Payment[(Payment)]
        Order --> OrderProduct[(OrderProduct)]
        Product --> OrderProduct
        Variation --> OrderProduct

        Account --> Review[(ReviewRating)]
        Product --> Review

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        classDef g fill:#161b22,stroke:#238636,color:#c9d1d9
        class Account,Cart,CartItem,Product,Variation b
        class Order,Payment,OrderProduct,Review g
    `,

    'email-verification-flow': `
        graph TB
        Signup[User submits register form] --> SaveInactive[Save Account is_active false]
        SaveInactive --> BuildLink[Build uidb64 and token]
        BuildLink --> SendMail[Send activation email]
        SendMail --> ClickLink[User clicks activation URL]
        ClickLink --> TokenCheck[default_token_generator check]
        TokenCheck -- valid --> Activate[Set is_active true]
        TokenCheck -- invalid --> Reject[Invalid activation link]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class Signup,SaveInactive,BuildLink,SendMail,ClickLink,TokenCheck,Activate,Reject b
    `,

    'session-cart-merge-flow': `
        graph TD
        Guest[Anonymous user] --> SessionKey[request.session.session_key]
        SessionKey --> GuestCart[Cart + CartItem with variations]
        GuestCart --> Login[User login]

        Login --> FetchGuest[Load guest cart items]
        Login --> FetchUser[Load existing user cart items]
        FetchGuest --> CompareVar[Compare variation sets]
        FetchUser --> CompareVar

        CompareVar -- same variation --> IncQty[increment quantity]
        CompareVar -- new variation --> RebindItem[assign item.user]
        IncQty --> Persist[save]
        RebindItem --> Persist

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        classDef g fill:#161b22,stroke:#238636,color:#c9d1d9
        class Guest,SessionKey,GuestCart,Login,FetchGuest,FetchUser,CompareVar b
        class IncQty,RebindItem,Persist g
    `,

    'payment-unified-order-flow': `
        graph TD
        Checkout[checkout page] --> PlaceOrder[place_order]
        PlaceOrder --> PendingOrder[Order is_ordered false]

        PendingOrder --> PayPalPath[PayPal SDK payments endpoint]
        PendingOrder --> KakaoPath[Kakao ready and approve]

        PayPalPath --> Finalize[Create Payment and set order.is_ordered true]
        KakaoPath --> Finalize

        Finalize --> MoveItems[Move CartItem to OrderProduct]
        MoveItems --> ReduceStock[Product stock minus quantity]
        ReduceStock --> ClearCart[Delete user cart items]
        ClearCart --> Receipt[order_complete response and email]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        classDef o fill:#161b22,stroke:#d29922,color:#c9d1d9
        class Checkout,PlaceOrder,PendingOrder,Finalize,MoveItems,ReduceStock,ClearCart,Receipt b
        class PayPalPath,KakaoPath o
    `,

    'review-authorization-flow': `
        graph TB
        ProductDetail[product_detail page] --> AuthCheck{is authenticated?}
        AuthCheck -- no --> LoginRequired[redirect login]
        AuthCheck -- yes --> PurchaseCheck{has OrderProduct?}
        PurchaseCheck -- no --> BlockReview[no review write]
        PurchaseCheck -- yes --> SubmitReview[submit_review]

        SubmitReview --> ExistingCheck{already reviewed?}
        ExistingCheck -- yes --> UpdateReview[update existing review]
        ExistingCheck -- no --> CreateReview[create new review]

        CreateReview --> Aggregate[averageReview and countReview]
        UpdateReview --> Aggregate

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class ProductDetail,AuthCheck,PurchaseCheck,SubmitReview,ExistingCheck,Aggregate b
    `,

    'search-filter-sort-flow': `
        graph TB
        StoreView[store view] --> BaseProducts[Product queryset]
        Search[search keyword] --> SearchQ[description or product_name icontains]

        UpdateResults[update_results] --> CategorySession[category session keep]
        UpdateResults --> OptionFilter[variation value filters]
        UpdateResults --> SortPolicy[low high new avg_review]

        BaseProducts --> Paginator[Paginator page size 9]
        SearchQ --> Paginator
        CategorySession --> Paginator
        OptionFilter --> Paginator
        SortPolicy --> Paginator

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class StoreView,BaseProducts,Search,SearchQ,UpdateResults,CategorySession,OptionFilter,SortPolicy,Paginator b
    `,

    'drf-account-api-flow': `
        graph LR
        Client[API Client] --> Register[POST /api/account/register]
        Client --> Verify[POST /api/account/check_email_verification]
        Client --> Login[POST /api/account/login]
        Client --> Forgot[POST /api/account/forgot_password]
        Client --> Reset[POST /api/account/resetpassword_validate]

        Register --> Serializer[UserRegisterSerializer]
        Serializer --> Account[Create Account + UserProfile]
        Login --> JWT[RefreshToken.for_user]
        JWT --> Tokens[access token and refresh token]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class Client,Register,Verify,Login,Forgot,Reset,Serializer,Account,JWT,Tokens b
    `,

    'serializer-validation-flow': `
        graph TB
        Request[Incoming API payload] --> RegisterSer[UserRegisterSerializer]
        Request --> LoginSer[UserLoginSerializer]
        Request --> VerifySer[EmailVerificationSerializer]
        Request --> ResetSer[ResetPasswordSerializer]

        RegisterSer --> Rule1[password equals confirm_password]
        RegisterSer --> Rule2[valid email and phone format]
        ResetSer --> Rule3[token and uid required]
        ResetSer --> Rule4[new password equals confirm password]

        Rule1 --> Action[execute view action]
        Rule2 --> Action
        Rule3 --> Action
        Rule4 --> Action

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class Request,RegisterSer,LoginSer,VerifySer,ResetSer,Rule1,Rule2,Rule3,Rule4,Action b
    `,

    'version2-separation-plan': `
        graph TD
        V1[V1 Django Template Fullstack] --> KeepStable[Maintain service stability]
        KeepStable --> AddAPI[Add DRF endpoints by domain]
        AddAPI --> AuthAPI[Account APIs first]
        AddAPI --> Docs[Schema and Swagger docs]
        Docs --> Tests[Expand unit and integration tests]
        Tests --> FESeparation[Frontend and Backend separation rollout]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class V1,KeepStable,AddAPI,AuthAPI,Docs,Tests,FESeparation b
    `,

    'pytest-test-structure': `
        graph TB
        Pytest[pytest runner] --> Conftest[conftest fixtures]
        Conftest --> APIClient[rest_framework APIClient fixture]
        Conftest --> Factories[factory_boy Account and UserProfile]

        Tests[greatkart/tests/test_accounts] --> ViewTests[test_views]
        Tests --> FormTests[test_forms]
        Tests --> ModelTests[test_models]
        Tests --> EndpointTests[test_endpoints]

        APIClient --> ViewTests
        Factories --> ViewTests
        Factories --> EndpointTests

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class Pytest,Conftest,APIClient,Factories,Tests,ViewTests,FormTests,ModelTests,EndpointTests b
    `,

    'aws-eb-topology': `
        graph LR
        Developer[Developer push] --> GitHub[GitHub repository]
        GitHub --> EBDeploy[Elastic Beanstalk deployment]

        User[Client user] --> Route53[Route53]
        Route53 --> ELB[ELB]
        ELB --> EC2[EB EC2 instances]

        EC2 --> App[Django app]
        App --> RDS[(RDS PostgreSQL)]
        App --> S3[(S3 static and media)]

        subgraph Network
            VPC[VPC]
            IAM[IAM]
        end

        EBDeploy --> EC2
        VPC --> EC2
        VPC --> RDS
        IAM --> S3

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class Developer,GitHub,EBDeploy,User,Route53,ELB,EC2,App,VPC,IAM,RDS,S3 b
    `,

    'static-media-s3-flow': `
        graph TB
        Settings[greatkart settings.py] --> Storages[django-storages]
        Storages --> StaticCfg[STATICFILES_STORAGE S3Boto3Storage]
        Storages --> MediaCfg[DEFAULT_FILE_STORAGE MediaStorage]

        CollectStatic[collectstatic] --> S3Static[S3 bucket static location]
        UploadMedia[Image upload] --> S3Media[S3 bucket media location]
        S3Static --> CDNURL[STATIC_URL from AWS custom domain]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class Settings,Storages,StaticCfg,MediaCfg,CollectStatic,S3Static,UploadMedia,S3Media,CDNURL b
    `,

    'migration-sqlite-to-postgres': `
        graph TD
        LocalSQLite[(Local SQLite DB)] --> Dump[dumpdata to datadump.json]
        Dump --> Transfer[Transfer dump file to cloud env]
        Transfer --> AWSApp[EB Django runtime]
        AWSApp --> Load[loaddata datadump.json]
        Load --> RDS[(RDS PostgreSQL)]
        RDS --> Validate[Data integrity check]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class LocalSQLite,Dump,Transfer,AWSApp,Load,RDS,Validate b
    `,

    'admin-honeypot-flow': `
        graph TB
        AttackBot[Bruteforce bot] --> AdminPath[/admin]
        AdminPath --> Honeypot[admin_honeypot fake login]
        Honeypot --> LogIP[record suspicious IP attempts]

        AdminUser[Real admin] --> SecurePath[/securelogin]
        SecurePath --> RealAdmin[Django admin site]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        classDef o fill:#161b22,stroke:#d29922,color:#c9d1d9
        class AttackBot,AdminPath,Honeypot,LogIP o
        class AdminUser,SecurePath,RealAdmin b
    `,

    'auth-hardening-case': `
        graph TB
        Threat1[Email spoofed registrations] --> Control1[Tokenized email ownership verification]
        Threat2[Admin bruteforce attacks] --> Control2[Honeypot plus hidden real admin path]

        Control1 --> Outcome1[Only verified users become active]
        Control2 --> Outcome2[Attack traffic diverted and observable]

        Outcome1 --> SecurityGain[Higher account trust and auth reliability]
        Outcome2 --> SecurityGain

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class Threat1,Threat2,Control1,Control2,Outcome1,Outcome2,SecurityGain b
    `,

    'commerce-integration-case': `
        graph TB
        Challenge[Commerce complexity] --> SessionNeed[Anonymous cart persistence]
        Challenge --> PaymentNeed[Dual payment provider integration]

        SessionNeed --> SessionDesign[Session cart_id and merge on login]
        PaymentNeed --> UnifiedService[Common order completion contract]

        UnifiedService --> PostProcess[Create order products reduce stock send mail]
        SessionDesign --> UX[Continuous user experience]
        PostProcess --> Reliability[Consistent business outcomes]

        classDef b fill:#161b22,stroke:#58a6ff,color:#c9d1d9
        class Challenge,SessionNeed,PaymentNeed,SessionDesign,UnifiedService,PostProcess,UX,Reliability b
    `
};
