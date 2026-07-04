# POSTMAN_GUIDE.md - CheesKick Backend

## Workspace Name
**`CheesKick - Backend API`**

## Collection Naming Convention

Create the following collections:

1. **CheesKick - Auth**
2. **CheesKick - Users & Profile**
3. **CheesKick - Scanning & Players** (Core)
4. **CheesKick - Collections & Cards**
5. **CheesKick - Trading**
6. **CheesKick - Social & Leaderboards**
7. **CheesKick - Live & Predictions**
8. **CheesKick - Admin / Internal** (for internal tools)

## Folder Structure (Inside Each Collection)
- `00 - Authentication` (if applicable)
- `01 - List & Retrieve`
- `02 - Create & Update`
- `03 - Actions` (e.g., Scan, Compare, Trade)
- `04 - Tests & Edge Cases`

## Environments
- `CheesKick - Local`
- `CheesKick - Staging`
- `CheesKick - Production`

**Important Variables**:
- `base_url` = `http://localhost:8000/api/v1`
- `access_token`
- `refresh_token`
- `player_id`
- `user_id`

## Best Practices for Codex / Implementer

**After implementing each API**:
1. Add the request to the correct collection.
2. Use clear naming: `POST Scan Player` , `GET Player Detail`, etc.
3. Add detailed description (what it does, parameters, expected behavior).
4. Add example request body + response.
5. Add basic tests (status code, response schema, etc.).
6. Use variables instead of hard-coded values.

## Authorization
- Use **Bearer Token** for most endpoints.
- Store `access_token` in environment variables.

## Versioning
All endpoints should be under `/api/v1/`

---

This completes your documentation set.

You now have:
- PROJECT_DESCRIPTION.md
- ROADMAP.md
- AGENTS.md
- CODING_PRACTICES.md
- GITHUB_SETUP.md
- POSTMAN_GUIDE.md

**Ready to start development.**