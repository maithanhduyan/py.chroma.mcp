from typing import Dict, List, TypedDict, Union
from enum import Enum
from mcp.server.fastmcp import FastMCP
import chromadb
import argparse
import os
from dotenv import load_dotenv
from chromadb.config import Settings
from typing_extensions import TypedDict

from utils.logger import get_logger

logger = get_logger(__name__)


# Initialize FastMCP server
mcp = FastMCP("chroma")

# Global variables
_chroma_client = None


def create_parser():
    """Create command-line argument parser for the MCP server."""
    parser = argparse.ArgumentParser(description="FastMCP server for Chroma DB")
    parser.add_argument(
        "--client-type",
        choices=["http", "cloud", "persistent", "ephemeral"],
        default=os.getenv("CHROMA_CLIENT_TYPE", "ephemeral"),
        help="Type of Chroma client to use",
    )

    return parser


def get_chroma_client(args=None):
    """Get or create the global Chroma client instance."""
    global _chroma_client
    if _chroma_client is None:
        _chroma_client = chromadb.PersistentClient(path="./chroma_db")
    return _chroma_client


##### Collection Tools #####
@mcp.tool()
async def echo(message: str) -> str:
    """Echo back the input message (useful for testing)."""
    return f"Echo: {message}"


def main():
    """Main entry point for the MCP server."""
    parser = create_parser()
    args = parser.parse_args()
    try:
        get_chroma_client(args)
        logger.info("Loading Chroma client...")
        logger.info(f"{str(args)}")
    except Exception as e:
        logger.info(f"Failed to initialize Chroma client: {str(e)}")
        raise

    # Initialize and run the server
    logger.info("Starting MCP server")
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
