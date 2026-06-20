# Karbon Interview — Prewired Environment

Clean repo for the Karbon AI Engineer **online coding** interview. Code is written
live during the session; this repo only ships a **ready-to-run Python environment** so
no time is lost on `pip install`, Pylance red squiggles, or missing runtime config.

## What's preinstalled

- **Python 3.12** (pinned — hard constraint: `llm-guard <3.13`, `presidio <3.14`)
- Env managed by **uv** → `.venv/` at repo root, auto-selected by VSCode/Pylance.
- Ollama models already pulled: `qwen3:30b-a3b`, `qwen3:14b`, `qwen3:1.7b`, `bge-m3`.

Covers every interview scenario:

| Scenario | Key packages |
|---|---|
| 0 — Email priority API | fastapi, uvicorn, pydantic, pydantic-settings, ollama, httpx, tenacity, pybreaker, structlog, uuid6 |
| 1–3 — CSV pipelines | pandas, pandera, scikit-learn, numpy |
| 4 — LangChain single agent | langchain, langchain-ollama, langchain-openai, langchain-community |
| 5–7 — LangGraph (multi-)agent | langgraph |
| 8 — RAG | sentence-transformers, chromadb, faiss-cpu, rank-bm25, ragas, bge-m3 |
| 9 — Eval / LLM-as-judge | deepeval |
| 10 — Structured extraction | gliner, spacy (+ en_core_web_lg) |
| Guardrails (all) | llm-guard, presidio-analyzer/anonymizer, spacy |

## Quick start

```bash
uv sync                 # recreate the env if needed (warm cache → seconds)
uv run python -c "import fastapi, langgraph, deepeval; print('ok')"
ollama list             # confirm models are present
```

Run code / tests:

```bash
uv run uvicorn app.main:app --reload     # whatever FastAPI app you write
uv run pytest -q
```

## Notes

- `import ragas` is made to work on the langchain 1.x stack via a small compatibility
  shim (`langchain_community.chat_models.vertexai` was removed in community 0.4; ragas
  still imports it). See `.venv/.../sitecustomize.py`. Vertex AI is never used for local
  RAG eval, so it's a harmless stub.
- LLM defaults to local Ollama (`qwen3:14b`); no API key required. OpenRouter is an
  optional fallback — see `.env.example`.
- `transformers` is pinned to `4.51.3` by `llm-guard`; do not upgrade it.
