# CheesKick Backend - Project Roadmap

**Name**: CheesKick  
**Type**: Django REST API for Flutter mobile app (sports stats + gamification)  
**Goal**: Scalable, maintainable backend for 10k+ users.

## Phases

**Phase 0: Setup (1 week)**
- Django 5.x project with Poetry.
- Docker + docker-compose (PostgreSQL, Redis).
- Custom User model.
- Basic CI (GitHub Actions).
- Pre-commit (black, ruff, mypy).

**Phase 1: Auth & Users (1-2 weeks)**
- Registration, login (JWT).
- Profile management.
- PRO subscription status.

**Phase 2: Core Stats & Scanning (2-3 weeks)**
- Player models.
- Scan history.
- SportRadar integration (polling initially).
- Player stats endpoints + comparisons.

**Phase 3: Gamification & Collections**
- Card-like stat snapshots.
- Albums, rarity, duplicates.
- Trading system.
- Leaderboards & achievements.

**Phase 4: Social & Live Features**
- Friends, activity.
- Predictions.
- Notifications.

**Phase 5: Monetization & Polish**
- Stripe integration.
- Admin panel.
- Caching, Celery tasks.

**Phase 6: Production Readiness**
- Performance optimization.
- Security audit.
- Monitoring (Sentry?).
- Full test coverage.

## Open Questions (Critical)
- AI recognition: Client or server side?
- SportRadar plan and exact data needs.
- Extent of "trading" and card ownership.
- Real-time requirements (WebSockets?).
- Image/media storage strategy.

**Rule**: One API/feature at a time. Thoroughly test before moving on.