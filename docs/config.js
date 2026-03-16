import { diagrams } from './diagrams.js';
import { learnMoreLinks } from './learnmore-links.js';

const cardMeta = {
    'django-app-architecture': {
        title: 'Django 앱 아키텍처',
        description: 'greatkart 루트 설정을 중심으로 accounts, store, carts, orders, category 앱 모듈로 분리하여 라우팅과 설계를 체계화했습니다.',
        cardClass: 'backend-card'
    },
    'commerce-data-model': {
        title: '커머스 데이터 모델',
        description: '장바구니, 주문, 결제, 상품, 옵션(Variation), 리뷰 엔티티를 연결하여 재고 관리와 구매 이력의 일관성을 보장합니다.',
        cardClass: 'backend-card'
    },
    'email-verification-flow': {
        title: '이메일 인증 워크플로우',
        description: '회원가입 시 비활성 사용자를 생성하고, uid/token 기반 인증 링크 검증을 통해 계정을 활성화하는 보안 흐름을 구축했습니다.',
        cardClass: 'backend-card'
    },
    'session-cart-merge-flow': {
        title: '세션 장바구니 병합',
        description: '비로그인 상태의 세션 기반 장바구니 데이터를 로그인 시 사용자 계정 장바구니와 옵션 단위로 중복 제거하여 병합합니다.',
        cardClass: 'backend-card'
    },
    'payment-unified-order-flow': {
        title: '통합 결제 주문 처리',
        description: 'PayPal SDK와 KakaoPay REST API를 단일 주문 완료 경로로 통합하여 재고 갱신과 장바구니 정리를 안정적으로 수행합니다.',
        cardClass: 'backend-card'
    },
    'drf-account-api-flow': {
        title: 'DRF 계정 API 전환',
        description: 'V2 버전으로의 전환을 위해 DRF ViewSet을 활용한 회원가입, 로그인, 비밀번호 재설정 및 JWT 발급 엔드포인트를 구현했습니다.',
        cardClass: 'frontend-card'
    },
    'version2-separation-plan': {
        title: 'V2 분리 및 확장 계획',
        description: '기존 V1 템플릿 서비스를 유지하면서 API 커버리지를 확장하고, 프론트엔드-백엔드 분리를 위한 로드맵을 설계했습니다.',
        cardClass: 'frontend-card'
    },
    'pytest-test-structure': {
        title: 'pytest 테스트 구조',
        description: 'FactoryBoy 기반의 픽스처와 계정 도메인 중심 테스트를 구축하여 유닛 및 통합 테스트 커버리지를 확보했습니다.',
        cardClass: 'frontend-card'
    },
    'aws-eb-topology': {
        title: 'AWS EB 배포 토폴로지',
        description: 'Elastic Beanstalk 환경에서 RDS, S3, Route53, VPC를 결합하여 관리형 클라우드 운영 및 확장성을 확보했습니다.',
        cardClass: 'devops-card'
    },
    'migration-sqlite-to-postgres': {
        title: '케이스 1: DB 마이그레이션',
        description: 'dumpdata와 loaddata 전략을 사용하여 개발용 SQLite 데이터를 운영용 PostgreSQL로 데이터 유실 없이 성공적으로 이전했습니다.',
        cardClass: 'devops-card'
    },
    'auth-hardening-case': {
        title: '케이스 2: 인증 보안 강화',
        description: '이메일 소유권 검증과 어드민 경로 보호(Honeypot)를 결합하여 비정상 접근 시도와 보안 리스크를 최소화했습니다.',
        cardClass: 'devops-card'
    },
    'commerce-integration-case': {
        title: '케이스 3: 커머스 통합',
        description: '세션 유지와 이중 결제 연동 로직을 단일 주문 계약으로 통합하여 예외 상황에서도 결제 안정성을 확보했습니다.',
        cardClass: 'devops-card'
    }
};

const mapCards = (ids) => ids.map((id) => ({
    mermaidId: id,
    title: cardMeta[id]?.title ?? id,
    description: cardMeta[id]?.description ?? '',
    links: [
        { label: 'EVIDENCE', href: `./evidence/upgrade_django4/index.html#${id}`, variant: 'primary' },
        { label: 'README', href: learnMoreLinks[id] ?? '#', variant: 'ghost' }
    ],
    cardClass: cardMeta[id]?.cardClass ?? ''
}));

export const templateConfig = {
    system: {
        documentTitle: 'Yohan | Django Commerce 백엔드 아키텍트',
        systemName: 'DJANGO_COMMERCE_V2.1'
    },

    hero: {
        sectionId: 'system-architecture',
        panelTitle: 'SYSTEM_ARCHITECTURE',
        panelUid: 'ID: DJANGO-COMMERCE-01',
        diagramId: 'upgrade-django-system-architecture',
        metrics: [
            '서비스: Django 기반 커머스 (V1 템플릿) + DRF API 전환 진행 중 (V2)',
            '핵심 도메인: 계정, 스토어, 장바구니, 주문, 카테고리',
            '보안 체계: 이메일 토큰 활성화 + 어드민 허니팟 + 보안 경로 설정',
            '결제 통합: PayPal SDK 및 KakaoPay API 단일 주문 완료 계약 처리',
            '인프라: AWS Elastic Beanstalk, RDS PostgreSQL, S3, Route53, VPC'
        ],
        quickLinks: [
            { label: 'GITHUB_REPO', href: 'https://github.com/ramyo564/Upgrade_Django4', variant: 'primary' },
            { label: 'PROBLEM_SOLVING', href: 'https://ramyo564.github.io/Upgrade_Django4-portfolio/', variant: 'secondary' },
            { label: 'PORTFOLIO_HUB', href: 'https://ramyo564.github.io/Portfolio/', variant: 'ghost' }
        ]
    },

    topPanels: [
        {
            sectionId: 'django-architecture-panel',
            panelTitle: 'DJANGO_ARCHITECTURE',
            panelUid: 'ID: DJANGO-COMMERCE-02',
            diagramId: 'django-architecture-overview',
            navLabel: 'Django 구조',
            metrics: [
                '템플릿 서비스와 API 엔드포인트가 공존하는 하이브리드 앱 아키텍처',
                '서버 레이어에서 구현된 세션 장바구니 및 결제/주문 파이프라인 전 과정 제어',
                '데이터 마이그레이션, 인증 강화, 커머스 통합 등 3대 핵심 엔지니어링 사례 집중'
            ]
        }
    ],

    skills: {
        sectionId: 'skill-set',
        panelTitle: 'SKILL_SET',
        panelUid: 'ID: STACK-MAP',
        items: [
            { title: 'BACKEND CORE', stack: 'Python 3.11, Django 4.2, DRF, SimpleJWT' },
            { title: 'DATA', stack: 'PostgreSQL, SQLite, ORM 관계형 모델링' },
            { title: 'COMMERCE', stack: '세션 장바구니, 주문 오케스트레이션, 재고 동기화, 리뷰 시스템' },
            { title: 'API INTEGRATION', stack: 'KakaoPay REST, PayPal SDK, 이메일 토큰 발송' },
            { title: 'CLOUD', stack: 'AWS Elastic Beanstalk, RDS, S3, Route53, VPC, IAM' },
            { title: 'QUALITY', stack: 'pytest, factory_boy, drf-spectacular, 단계별 마이그레이션' }
        ]
    },

    serviceSections: [
        {
            id: 'backend-services',
            title: 'BACKEND_SERVICES',
            navLabel: '백엔드 서비스',
            theme: 'blue',
            cardVisualHeight: '280px',
            cardClass: 'backend-card',
            recruiterBrief: {
                kicker: 'ARCHITECTURE_QUICK_SCAN',
                title: '커머스 시스템 핵심 설계 요약',
                cases: [
                    {
                        id: 'Migration',
                        anchorId: 'migration-sqlite-to-postgres',
                        title: '운영 DB 마이그레이션',
                        problem: '로컬(SQLite) 데이터의 운영(PostgreSQL) 이전 시 호환성 리스크',
                        action: 'JSON 직렬화 기반 덤프 전략 및 제약 사항 사전 조정',
                        impact: '데이터 유실 Zero 및 운영 DB 전환 성공'
                    },
                    {
                        id: 'Payment',
                        anchorId: 'payment-unified-order-flow',
                        title: '이중 결제 플랫폼 통합',
                        problem: '다양한 결제 수단별 주문 처리 로직 파편화',
                        action: '단일 주문 최종화 계약(Finalization Contract) 구축',
                        impact: '결제 수단 추가 용이성 및 주문 정합성 확보'
                    },
                    {
                        id: 'Security',
                        anchorId: 'auth-hardening-case',
                        title: '인증 및 어드민 보안 강화',
                        problem: '무차별 대입 공격 및 어드민 노출 위험',
                        action: '어드민 허니팟 도입 및 이메일 소유권 기반 계정 활성화',
                        impact: '보안 취약점 방어 및 신뢰할 수 있는 사용자만 확보'
                    },
                    {
                        id: 'Cart',
                        anchorId: 'session-cart-merge-flow',
                        title: '하이브리드 장바구니 동기화',
                        problem: '비로그인 사용자 경험의 단절 및 데이터 유실',
                        action: '세션 기반-DB 기반 장바구니 병합 알고리즘 구현',
                        impact: '로그인 전환 시 장바구니 데이터 100% 보존'
                    }
                ]
            },
            groups: [
                {
                    title: 'CORE FLOW',
                    desc: '아키텍처 / 데이터 / 인증 / 장바구니 / 결제',
                    cards: mapCards([
                        'django-app-architecture',
                        'commerce-data-model',
                        'email-verification-flow',
                        'session-cart-merge-flow',
                        'payment-unified-order-flow'
                    ])
                }
            ]
        },
        {
            id: 'platform-quality-services',
            title: 'PLATFORM_AND_QUALITY',
            navLabel: '플랫폼 및 품질',
            theme: 'green',
            cardVisualHeight: '265px',
            cardClass: 'frontend-card',
            groups: [
                {
                    title: 'MIGRATION ROADMAP',
                    desc: 'DRF API 확장 및 분리 전략',
                    cards: mapCards([
                        'drf-account-api-flow',
                        'version2-separation-plan'
                    ])
                },
                {
                    title: 'QUALITY & OPERATION',
                    desc: '테스트 베이스라인 및 배포 구조',
                    cards: mapCards([
                        'pytest-test-structure',
                        'aws-eb-topology'
                    ])
                }
            ]
        },
        {
            id: 'core-case-studies',
            title: 'CORE_CASE_STUDIES',
            navLabel: '핵심 케이스 스터디',
            theme: 'orange',
            cardVisualHeight: '275px',
            cardClass: 'devops-card',
            groups: [
                {
                    title: 'THREE DEEP CASES',
                    desc: '마이그레이션 / 보안 / 커머스 통합',
                    cards: mapCards([
                        'migration-sqlite-to-postgres',
                        'auth-hardening-case',
                        'commerce-integration-case'
                    ])
                }
            ]
        }
    ],

    contact: {
        sectionId: 'contact',
        panelTitle: 'CONTACT',
        panelUid: 'ID: CONTACT-01',
        description: 'Django 커머스 아키텍처 및 마이그레이션 관련 협업을 위해 아래 채널로 연락 부탁드립니다.',
        actions: [
            { label: 'GITHUB_REPO', href: 'https://github.com/ramyo564/Upgrade_Django4' },
            { label: 'EMAIL', href: 'mailto:yohan032yohan@gmail.com' },
            { label: 'EVIDENCE', href: './evidence/upgrade_django4/index.html' },
            { label: 'DEMO_VIDEO', href: 'https://drive.google.com/file/d/16uyTOVPtCR6d_NeIkZWtBG7iAFALtgHX/view?usp=drive_link' }
        ]
    },

    mermaid: {
        theme: 'dark',
        securityLevel: 'loose',
        fontFamily: 'Inter',
        flowchart: {
            useMaxWidth: true,
            htmlLabels: true,
            curve: 'linear'
        }
    },

    diagrams
};
