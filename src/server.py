#!/usr/bin/env python3
"""
FastMCP ChromaDB Server with Advanced Embedding Integration
Supports ChromaDB, custom embeddings, Vietnamese text processing, and semantic search
Uses asyncio for optimal performance
Generated by Copilot
"""

import sys
import asyncio
import logging
import time
from typing import Dict, Any, Optional

# Import config to setup project paths automatically (main entry point)
import config

# Import FastMCP and tools
from tools import mcp

# Configure enhanced logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stderr),  # Log to stderr to avoid stdout pollution
    ],
)
logger = logging.getLogger(__name__)

# Ensure UTF-8 encoding for stdout
try:
    if hasattr(sys.stdout, "reconfigure"):
        getattr(sys.stdout, "reconfigure")(encoding="utf-8")
except (AttributeError, TypeError):
    import codecs

    if hasattr(sys.stdout, "buffer"):
        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer)


def log_server_startup():
    """Log server startup information."""
    startup_info = {
        "server": "ChromaDB FastMCP Server",
        "version": "2.0.0",
        "embedding_support": True,
        "vietnamese_support": True,
        "features": [
            "ChromaDB Integration",
            "Custom Embeddings (mixedbread-ai/mxbai-embed-large-v1)",
            "Vietnamese Text Processing",
            "Intelligent Chunking",
            "Semantic Search",
            "Cross-lingual Support",
        ],
        "tools": [
            "echo",
            "list_collections",
            "create_collection",
            "delete_collection",
            "add_documents",
            "query_collection",
            "get_embedding_model_info",
            "configure_embedding_model",
            "chunk_text_intelligent",
            "get_performance_metrics",  # New metrics tool
        ],
        "startup_time": time.strftime("%Y-%m-%d %H:%M:%S"),
    }

    logger.info("=" * 60)
    logger.info("🚀 FastMCP ChromaDB Server Starting")
    logger.info("=" * 60)
    logger.info(f"📋 Server: {startup_info['server']} v{startup_info['version']}")
    logger.info(f"🤖 Embedding: nomic-ai/nomic-embed-text-v1.5 (lightweight)")
    logger.info(f"🇻🇳 Vietnamese: Fully Supported")
    logger.info(f"🛠️ Tools: {len(startup_info['tools'])} available")
    logger.info(f"⏰ Started: {startup_info['startup_time']}")
    logger.info("=" * 60)


def initialize_systems_sync() -> Dict[str, Any]:
    """
    Initialize ChromaDB and embedding systems synchronously.
    FastMCP handles its own async operations internally.

    Returns:
        Dictionary with initialization results"""
    logger.info("🔧 Initializing embedding systems...")

    # Import to trigger initialization
    from tools import get_chroma_client, get_embedding_manager

    # Initialize ChromaDB
    chroma_client = get_chroma_client()
    logger.info(f"✅ ChromaDB initialized: {type(chroma_client).__name__}")

    # Initialize embeddings and try to load a fast model
    embedding_manager = get_embedding_manager()

    # Try to load a lightweight model for faster development
    logger.info("🚀 Pre-loading embedding model for better user experience...")

    # Check if any model is already loaded (from cache)
    model_info = embedding_manager.get_model_info()
    if model_info and model_info.get("name") != "chromadb-default":
        model_name = model_info.get("name", "unknown")
        model_dim = model_info.get("embedding_dim", "unknown")
        device = model_info.get("device", "unknown")
        logger.info(
            f"✅ Using cached embedding model: {model_name} ({model_dim}D) on {device}"
        )
    else:
        # Try to load the fastest model from our priority list
        logger.info("⚡ Loading lightweight model for fast development...")
        success = embedding_manager.load_best_available_model()

        if success:
            model_info = embedding_manager.get_model_info()
            model_name = model_info.get("name", "unknown")
            model_dim = model_info.get("embedding_dim", "unknown")
            device = model_info.get("device", "unknown")
            logger.info(
                f"✅ Pre-loaded embedding model: {model_name} ({model_dim}D) on {device}"
            )
        else:
            logger.info("⚠️ No custom model loaded, will use ChromaDB default")

    return {
        "chroma_client": chroma_client,
        "embedding_manager": embedding_manager,
        "model_info": model_info,
    }


def preload_embedding_model() -> bool:
    """
    Preload an embedding model for faster development.
    Tries to use cached models first for speed.

    Returns:
        True if a model was successfully loaded
    """
    logger.info("🚀 Pre-loading embedding model...")

    try:
        from tools import get_embedding_manager

        embedding_manager = get_embedding_manager()

        # Check if we already have a model loaded from cache
        model_info = embedding_manager.get_model_info()
        if model_info and model_info.get("name") != "chromadb-default":
            logger.info(f"✅ Model already loaded: {model_info.get('name')}")
            return True

        # Try to load the best available model
        success = embedding_manager.load_best_available_model()
        if success:
            model_info = embedding_manager.get_model_info()
            logger.info(
                f"✅ Pre-loaded: {model_info.get('name')} ({model_info.get('embedding_dim')}D)"
            )
            return True
        else:
            logger.warning("⚠️ No custom models could be loaded")
            return False

    except Exception as e:
        logger.error(f"❌ Failed to preload model: {e}")
        return False


def main():
    """
    Main server entry point.

    ASYNC DESIGN DECISION:
    - FastMCP handles its own asyncio event loop internally via mcp.run()
    - We do NOT wrap mcp.run() in asyncio.run() to avoid event loop conflicts
    - All MCP tools (@mcp.tool()) are async functions handled by FastMCP
    - Initialization is synchronous, letting FastMCP manage async operations
    - This prevents "RuntimeError: cannot be called from a running event loop"
    """
    try:
        # Log startup information
        log_server_startup()

        # Preload embedding model first for faster user experience
        logger.info("🔥 Pre-loading embedding model for faster development...")
        preload_success = preload_embedding_model()

        if preload_success:
            logger.info("⚡ Model pre-loaded successfully - development ready!")
        else:
            logger.info("⚠️ Model pre-loading failed - will use ChromaDB default")

        # Initialize remaining systems
        systems = initialize_systems_sync()

        logger.info("🎯 FastMCP server ready for connections")
        logger.info("=" * 60)

        # Import and start FastMCP server - it handles its own event loop
        from tools import mcp

        # FastMCP manages its own asyncio context
        mcp.run()

    except KeyboardInterrupt:
        logger.info("\n🛑 Server shutdown requested by user")
    except Exception as e:
        logger.error(f"💥 Server startup failed: {e}")
        logger.exception("Server startup error details:")
        raise
    finally:
        logger.info("🔚 FastMCP ChromaDB Server stopped")


if __name__ == "__main__":
    main()
