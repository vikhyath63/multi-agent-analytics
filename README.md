# Multi-Agent Analytics (Clean-Room Reference)

A local natural-language analytics API over a seeded SQLite sales database. The intent router maps a small set of supported questions to parameterized SQL templates, applies a business-unit scope, and returns results plus a concise explanation.

## Run
```bash
pip install -e ".[dev]"
uvicorn app.main:app --reload
```
POST /query with `{"question":"revenue by region","business_unit":"Retail"}`. No external credentials required.

This is an independent reference implementation, not proprietary client code. It demonstrates safe query routing and scoped analytics; an LLM planner, Postgres/pgvector schema RAG and Redis cache are planned adapters.
