# CheesKick - API Documentation Strategy

## Goal
Maintain always-up-to-date, professional API docs without manual effort.

## Tools
- **drf-spectacular** — Auto OpenAPI 3.1 generation with excellent DRF support.
- **Swagger UI** — For internal testing.
- **GitBook** — Final public / team documentation.

## Workflow for Codex / Implementer

**After implementing any API**:
1. Add proper OpenAPI decorators (`@extend_schema`).
2. Run:
   ```bash
   python manage.py spectacular --file schema.yml