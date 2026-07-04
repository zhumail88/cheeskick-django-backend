# CheesKick - Coding Practices

**Must Follow** for all code.

## 1. Architecture
- Layered: `api/` → `services/` → `domain/` → `models/`.
- Thin views.
- Business logic in services.

## 2. Django Specific
- Use Class-based views / ViewSets.
- Serializers with validation.
- Custom managers for models.
- Indexes on query-heavy fields.
- UUID PKs.

## 3. Performance & Scale
- Always consider N+1.
- Use `select_related` / `prefetch_related`.
- Cache heavy queries (Redis).
- Rate limiting on all endpoints.

## 4. Testing
- 80%+ coverage.
- Use factories.
- Test permissions and edge cases.

## 5. Git & Commits
- Conventional Commits (`feat:`, `fix:`, `refactor:`).
- Descriptive PRs.
- Small, focused commits.

## 6. Code Quality
- Type hints.
- Meaningful names.
- No magic numbers.
- Comprehensive docstrings for complex logic.

**Never** write throwaway code. Everything must be production-grade.