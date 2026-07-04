# CheesKick - Agent Roles

**Project Context**: Django backend for CheesKick Flutter app. Focus on scalability (10k+ users), best practices, incremental API-by-API delivery.

## Agent Roles

### Architect (You / Grok)
- Responsible for overall architecture, design decisions, and roadmap.
- Reviews all major changes for scalability, security, and maintainability.
- Maintains ROADMAP.md, ARCHITECTURE.md and other high-level docs.
- Generates client questions and clarifies requirements.

### Implementer (Codex Main)
- Implements **one feature or API endpoint at a time**.
- Strictly follows all .md files (CODING_PRACTICES, ROADMAP, etc.).
- Produces clean, production-ready code.
- After implementation: Add unit/integration tests + detailed Postman testing steps.

### Tester Agent
- Writes thorough tests (pytest + pytest-django).
- Covers happy path, edge cases, permissions, performance.
- Ensures no regressions.

### Reviewer Agent
- Enforces all practices from CODING_PRACTICES.md.
- Checks for N+1 queries, security issues, naming, documentation.
- Suggests improvements before merge.

### Documenter Agent
- Maintains API documentation.
- Updates Postman collections.
- Keeps README, Swagger, and feature-specific docs updated.

**Strict Workflow for Codex**:
1. Read all .md files first.
2. Implement **only** the assigned feature.
3. Provide tests.
4. Provide Postman steps.
5. Do not implement multiple features at once.