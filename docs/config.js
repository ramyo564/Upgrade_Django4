import { diagrams } from './diagrams.js';
import { learnMoreLinks } from './learnmore-links.js';

const cardMeta = {
    'django-app-architecture': {
        title: 'Django App Architecture',
        description: 'The project is organized as app modules (`accounts`, `store`, `carts`, `orders`, `category`) under `greatkart` root settings and URL routing.'
    },
    'commerce-data-model': {
        title: 'Commerce Data Model',
        description: 'Cart, order, payment, product, variation, and review entities are connected so checkout, stock handling, and purchase history stay consistent.'
    },
    'email-verification-flow': {
        title: 'Email Verification Flow',
        description: 'Registration creates inactive users, sends uid/token links, and activates accounts only when token verification succeeds.'
    },
    'session-cart-merge-flow': {
        title: 'Session Cart Merge Flow',
        description: 'Anonymous cart items keyed by session are merged with user cart on login using variation-level deduplication rules.'
    },
    'payment-unified-order-flow': {
        title: 'Unified Payment Order Flow',
        description: 'PayPal SDK and Kakao REST both converge into one order finalization path for stock update, order product creation, and cart cleanup.'
    },
    'drf-account-api-flow': {
        title: 'DRF Account API Flow',
        description: 'V2 account endpoints are exposed via DRF ViewSet actions for register/login/verification/password reset with JWT issuance.'
    },
    'version2-separation-plan': {
        title: 'Version 2 Separation Plan',
        description: 'The roadmap keeps V1 template service stable while expanding API coverage and progressing toward frontend-backend separation.'
    },
    'pytest-test-structure': {
        title: 'pytest Test Structure',
        description: 'Factory-based fixtures and account-focused tests in `greatkart/tests` provide the base for incremental unit/integration coverage.'
    },
    'aws-eb-topology': {
        title: 'AWS EB Topology',
        description: 'Deployment runs on Elastic Beanstalk with RDS, S3, Route53, and VPC boundaries for managed operation and cloud scalability.'
    },
    'migration-sqlite-to-postgres': {
        title: 'Case 1: SQLite -> PostgreSQL Migration',
        description: 'Data migration strategy used `dumpdata` and `loaddata` to move development SQLite data into production PostgreSQL with minimal risk.'
    },
    'auth-hardening-case': {
        title: 'Case 2: Auth Security Hardening',
        description: 'Authentication security combined email ownership verification and honeypot-based admin path defense to reduce abuse risk.'
    },
    'commerce-integration-case': {
        title: 'Case 3: Commerce Integration',
        description: 'Session persistence and dual-payment integration were unified into one reliable order completion contract across edge cases.'
    }
};

const mapCards = (ids) => ids.map((id) => ({
    mermaidId: id,
    title: cardMeta[id]?.title ?? id,
    description: cardMeta[id]?.description ?? '',
    learnMore: learnMoreLinks[id] ?? '#'
}));

export const templateConfig = {
    system: {
        documentTitle: 'Yohan | Upgrade Django4 Dashboard',
        systemName: 'UPGRADE_DJANGO4_V2.1'
    },

    hero: {
        sectionId: 'system-architecture',
        panelTitle: 'SYSTEM_ARCHITECTURE',
        panelUid: 'ID: UPGRADE-DJANGO4-01',
        diagramId: 'upgrade-django-system-architecture',
        metrics: [
            'Service Type: Django ecommerce (V1 templates) + DRF migration in progress (V2)',
            'Core Domains: accounts, store, carts, orders, category',
            'Security Baseline: email token activation + admin honeypot + secure admin path',
            'Payment Integration: PayPal SDK and Kakao REST unified into one order completion contract',
            'Cloud Runtime: AWS Elastic Beanstalk, RDS PostgreSQL, S3, Route53, VPC'
        ]
    },

    topPanels: [
        {
            sectionId: 'django-architecture-panel',
            panelTitle: 'DJANGO_ARCHITECTURE',
            panelUid: 'ID: UPGRADE-DJANGO4-02',
            diagramId: 'django-architecture-overview',
            metrics: [
                'App-based architecture with template and API endpoints coexisting during migration',
                'Session cart state + payment/order pipeline implemented end-to-end in server layer',
                'Three key cases highlighted: data migration, auth hardening, commerce integration'
            ]
        }
    ],

    skills: {
        sectionId: 'skill-set',
        panelTitle: 'SKILL_SET',
        panelUid: 'ID: STACK-MAP',
        items: [
            { title: 'BACKEND CORE', stack: 'Python 3.11, Django 4.2, DRF, SimpleJWT' },
            { title: 'DATA', stack: 'PostgreSQL, SQLite, ORM relational modeling' },
            { title: 'COMMERCE', stack: 'Session cart, order orchestration, stock update, reviews' },
            { title: 'API INTEGRATION', stack: 'KakaoPay REST, PayPal SDK, email token flow' },
            { title: 'CLOUD', stack: 'AWS Elastic Beanstalk, RDS, S3, Route53, VPC, IAM' },
            { title: 'QUALITY', stack: 'pytest, factory_boy, drf-spectacular, staged migration' }
        ]
    },

    serviceSections: [
        {
            id: 'backend-services',
            title: 'BACKEND_SERVICES',
            navLabel: 'BACKEND_SERVICES',
            theme: 'blue',
            cardVisualHeight: '280px',
            cardClass: 'backend-card',
            groups: [
                {
                    title: 'CORE FLOW',
                    desc: 'Architecture / Data / Auth / Cart / Payment',
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
            navLabel: 'PLATFORM_AND_QUALITY',
            theme: 'green',
            cardVisualHeight: '265px',
            cardClass: 'frontend-card',
            groups: [
                {
                    title: 'MIGRATION ROADMAP',
                    desc: 'DRF account API expansion and separation strategy',
                    cards: mapCards([
                        'drf-account-api-flow',
                        'version2-separation-plan'
                    ])
                },
                {
                    title: 'QUALITY & OPERATION',
                    desc: 'Testing baseline and AWS deployment topology',
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
            navLabel: 'CORE_CASE_STUDIES',
            theme: 'orange',
            cardVisualHeight: '275px',
            cardClass: 'devops-card',
            groups: [
                {
                    title: 'THREE DEEP CASES',
                    desc: 'Migration / Security / Commerce Integration',
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
        description: 'For collaboration, architecture discussion, or migration review, use one of the channels below.',
        actions: [
            { label: 'GITHUB', href: 'https://github.com/ramyo564/Upgrade_Django4' },
            { label: 'EMAIL', href: 'mailto:yohan032yohan@gmail.com' },
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
