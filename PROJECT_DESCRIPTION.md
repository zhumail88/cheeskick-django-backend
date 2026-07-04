# PROJECT_DESCRIPTION.md

**Project Name**: CheesKick Backend

## Overview
CheesKick is a Flutter mobile application where users point their phone camera at a TV during a live sports match. The AI identifies the player on screen and surfaces rich, beautifully presented statistics in a gamified "digital card" format.

**Critical Constraint** (from client specs):
- The app **does not** allow true digital card **ownership** or NFT-like collectibles due to licensing and copyright restrictions on player likenesses.
- All "cards", collections, and trading features must be built around **stats presentation** + CheesKick branding only.

## Core Experience
- **Scan Flow**: Camera → AI Player Recognition → Instant "card" reveal with hero stat + detailed stats + live match context.
- **Gamification**: Card-like UI, rarity tiers (Legendary/Epic/Rare), albums/collections, duplicate trading, leaderboards, achievements, predictions.
- **Social**: Shareable stat graphics, friends, activity feed.

## Supported Sports
- Football (Soccer)
- Basketball
- American Football
- Golf
- Baseball
- Tennis
- Formula 1
- Extensible for future sports

## Main Data Source
**SportRadar** APIs (live summaries, player stats, timelines, match context).

## Key Features Groups
- Authentication & Profile (with PRO subscription)
- Scanning & Player Stats
- Head-to-Head Comparisons
- Collections / Albums
- Trading System (duplicates)
- Leaderboards & Achievements
- Live Match Companion
- Predictions & Rewards
- Social Features
- Monetization (PRO + Shop)

## Backend Requirements
- Django 5.x + DRF
- Scalable for 10k+ users
- PostgreSQL, Redis, Celery
- Clean, layered architecture
- Thorough testing and documentation
- API-by-API development with Postman steps

**Development Philosophy**: Production-grade code from day one. No shortcuts. Follow all practices in CODING_PRACTICES.md, ROADMAP.md, and AGENTS.md strictly.

This is the single source of truth for the project context.