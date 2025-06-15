# py.chroma.mcp

A simple Model Context Protocol (MCP) server with ChromaDB integration. This server provides a stdio-based interface following the MCP specification, allowing AI assistants to interact with ChromaDB for vector storage and retrieval operations.

## Features

- **MCP Compliance**: Fully implements the Model Context Protocol specification
- **ChromaDB Integration**: Provides tools for creating, querying, and managing vector collections
- **Stdio Interface**: Uses standard input/output for communication
- **Simple Configuration**: Easy to set up and use
- **Extensible**: Easy to add new tools and capabilities

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install .
   ```
   Or install specific dependencies:
   ```bash
   pip install chromadb mcp
   ```

## Usage

### Running the Server

```bash
python run_server.py
```

The server will start and listen for JSON-RPC messages on stdin, responding on stdout.

### Available Tools

The server provides the following tools:

1. **echo** - Echo back a message (useful for testing)
2. **create_collection** - Create a new ChromaDB collection
3. **list_collections** - List all available collections
4. **add_documents** - Add documents to a collection
5. **query_collection** - Query a collection using semantic search
6. **delete_collection** - Delete a collection

### Testing

Run the test client to verify the server is working:

```bash
python test_client.py "python run_server.py"
```

### Example MCP Communication

#### Initialize the server:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "initialize",
  "params": {
    "protocolVersion": "2024-11-05",
    "capabilities": {},
    "clientInfo": {
      "name": "test-client",
      "version": "1.0.0"
    }
  }
}
```

#### List available tools:
```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/list"
}
```

#### Call the echo tool:
```json
{
  "jsonrpc": "2.0",
  "id": 3,
  "method": "tools/call",
  "params": {
    "name": "echo",
    "arguments": {
      "message": "Hello, MCP!"
    }
  }
}
```

## Configuration

### Environment Variables

The server can be configured through environment variables:

- `CHROMA_HOST`: ChromaDB host (default: localhost)
- `CHROMA_PORT`: ChromaDB port (default: 8000)
- `CHROMA_DB_PATH`: Path for persistent storage (default: ./chroma_db)

### Claude Desktop Integration

1. Copy `claude_desktop_config.json` to your Claude Desktop configuration
2. Update the paths in the config file to match your installation:
   ```json
   {
     "mcpServers": {
       "py-chroma-mcp": {
         "command": "python",
         "args": ["C:\\path\\to\\your\\project\\run_server.py"],
         "env": {
           "CHROMA_DB_PATH": "C:\\path\\to\\your\\project\\chroma_db"
         }
       }
     }
   }
   ```
3. Restart Claude Desktop

### Data Storage

- **Type**: Persistent local storage
- **Location**: `./chroma_db/` directory
- **Format**: SQLite + Binary vector files
- **Backup**: Simply copy the `chroma_db` folder

## Architecture

- `src/server.py`: Main MCP server implementation
- `src/config.py`: Configuration management
- `src/tools.py`: Tool definitions and ChromaDB integration
- `run_server.py`: Entry point script
- `test_client.py`: Test client for verification

## Development

The code follows Python best practices and includes:

- Type hints for better code maintainability
- Comprehensive error handling
- Logging for debugging and monitoring
- Modular design for easy extension

## License

This project is available under the MIT License.

## Contributing

Feel free to submit issues and enhancement requests!
