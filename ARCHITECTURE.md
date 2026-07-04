# CheesKick Architecture

## Purpose
This document captures the initial backend architecture so implementation stays consistent across future API slices.

## Core Principles
- API-first Django backend for the Flutter client.
- One feature or endpoint at a time.
- Thin views, business logic in services, validation in serializers.
- Use UUID primary keys and query-friendly indexes from the start.
- Keep the backend safe for the "stats presentation" model only; no real card ownership or NFT behavior.

## Initial Stack
- Django 5.x
- Django REST Framework
- PostgreSQL
- Redis
- Celery-ready foundation
- Poetry for dependency management

## Planned Layout
- `config/` for project settings and root URLs.
- `apps/users/` for the custom user model and profile foundation.
- `apps/` for future domain apps such as scanning, collections, social, and live features.
- `tests/` or app-level tests for pytest coverage.

## Phase 0 Decisions
- Use a custom user model from day one.
- Keep settings environment-driven so local, staging, and production can diverge cleanly.
- Containerize the stack with Docker and docker-compose.
- Add baseline linting and testing automation before feature work starts.

