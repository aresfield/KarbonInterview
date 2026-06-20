"""Model + endpoint reference. Look up names/ports here, or import the names.

    from models import GEN_PRIMARY, EMBED, RERANKER, OLLAMA_HOST
"""
import os

# --- Endpoints ---
OLLAMA_HOST = "http://localhost:11434"          # Ollama default port: 11434
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"   # fallback, needs API key

# --- Cloud fallback API keys (read from shell env: ~/.zshrc) ---
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_FALLBACK_MODEL = "gpt-4o-mini-2024-07-18"   # role: generation — pinned snapshot

# --- Generation (backend: ollama) ---
GEN_PRIMARY = "qwen3:14b"        # role: generation — main workhorse, fast
GEN_BIG = "qwen3:30b-a3b"        # role: generation — best quality, MoE ~18GB
GEN_TINY = "qwen3:1.7b"          # role: generation — cheap/fast, smoke tests

# --- Embedding (backend: ollama) ---
EMBED = "bge-m3"                 # role: embedding — dim 1024
EMBED_DIM = 1024

# --- Reranking (backend: sentence-transformers CrossEncoder, NOT ollama) ---
RERANKER = "BAAI/bge-reranker-v2-m3"   # role: reranking
