# py.chroma.mcp

A modern Model Context Protocol (MCP) server with ChromaDB integration. This server provides a stdio-based interface following the MCP specification, allowing AI assistants to interact with ChromaDB for vector storage and retrieval operations.

## ✨ Features

- 🚀 **Vector Database**: Full ChromaDB integration with collection management
- 🧠 **Smart Embeddings**: Configurable embedding models with caching
- ⚡ **Fast Package Management**: UV-first approach for lightning-fast installations
- 🔧 **Environment-First**: Configuration via environment variables
- 📊 **Performance Monitoring**: Built-in metrics and cache optimization
- 🔄 **Batch Processing**: Efficient document processing with progress tracking
- 🌐 **Vietnamese Optimized**: Intelligent text chunking for Vietnamese content

## 🚀 Quick Start

### 1. Install UV (Recommended)
```powershell
# Windows
winget install --id=astral-sh.uv -e

# Or via pip
pip install uv
```

### 2. Clone and Setup
```powershell
git clone <repo-url>
cd py.chroma.mcp

# Easy installation with UV
./install-deps.ps1
# Choose option 2 (Standard) for most users
```

### 3. Configure Environment
```powershell
# Setup environment variables
./setup-env.ps1

# Or manually edit .env file
cp .env.example .env
```

### 4. Test Installation
```powershell
# Test configuration
python test_env_config.py

# Test model info
python test_model_info.py
```

## 📦 Installation Options

### UV Commands (Recommended)
```powershell
# Sync exact versions from lockfile
uv sync

# Add new packages
uv add package_name

# Remove packages
uv remove package_name

# Run with environment
uv run python script.py

# Update lockfile
uv lock
```

### Traditional pip (Fallback)
```powershell
# Standard installation
pip install -r requirements.txt

# Development tools
pip install -r requirements-dev.txt
```

### PowerShell Script (Best Experience)
```powershell
# Interactive installation with multiple options
./install-deps.ps1

# Options available:
# 1. Minimal (Core only)
# 2. Standard (Recommended)
# 3. Full (GPU + Advanced)
# 4. Development (Testing tools)
# 5. Custom (Choose components)
# 6. Sync (Exact versions)
```

## ⚙️ Configuration

### Environment Variables
```bash
# Embedding model settings
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2
EMBEDDING_DEVICE=cpu  # or cuda
EMBEDDING_CACHE_DIR=./models_cache

# ChromaDB settings
CHROMA_DB_PATH=./chroma_db
CHROMA_COLLECTION_METADATA={"description": "MCP Collection"}

# Performance settings
EMBEDDING_BATCH_SIZE=32
EMBEDDING_CACHE_SIZE=1000
```

### Quick Environment Setup
```powershell
# Automated setup
./setup-env.ps1

# Manual setup
$env:EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
$env:EMBEDDING_DEVICE = "cpu"
```

## 🧪 Testing & Development

### Quick Tests
```powershell
# Test environment configuration
python test_env_config.py

# Test model information
python test_model_info.py

# Analyze dependencies
python analyze_dependencies.py
```

### Development Setup
```powershell
# Install development dependencies
uv add --dev pytest black isort mypy

# Or use script
./install-deps.ps1  # Choose option 4
```

## 📊 Dependency Management

### Modern Approach with UV
- **10-100x faster** than pip
- **Better dependency resolution**
- **Consistent lockfile** support
- **Virtual environment** management

### Available Dependency Sets
- **Core**: ChromaDB, MCP, NumPy, PSUtil
- **AI/ML**: Sentence-transformers, Torch, Transformers
- **Server**: Protocol handling, async support
- **Text**: Processing, chunking, tokenization  
- **Database**: ChromaDB, SQLite, persistence
- **Development**: Testing, linting, typing
- **Optional**: GPU acceleration, advanced features

## 🔧 Usage Examples

### Basic MCP Server
```python
# Start the server
python -m src.server

# Or with UV
uv run python -m src.server
```

### Custom Embedding Model
```python
# Via environment variable
$env:EMBEDDING_MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

# Restart server to apply changes
```

### Performance Monitoring
```python
# Check model info and performance
python -c "
from src.tools import get_embedding_model_info
info = get_embedding_model_info()
print(info)
"
```

## 📚 Available MCP Tools

### Collection Management
- `create_collection` - Create new ChromaDB collection
- `delete_collection` - Remove collection
- `list_collections` - List all collections

### Document Operations
- `add_documents` - Add documents with embeddings
- `query_collection` - Semantic search in collection
- `batch_process_documents` - Efficient batch processing

### Text Processing
- `chunk_text_intelligent` - Vietnamese-optimized chunking
- `echo` - Simple connectivity test

### Model & Performance
- `get_embedding_model_info` - Model details and config
- `configure_embedding_model` - Switch models dynamically
- `get_performance_metrics` - Performance statistics
- `get_cache_stats` - Cache utilization info
- `clear_embedding_cache` - Free memory

## 🚨 Best Practices

### UV Package Management
```powershell
# Always sync first in new environment
uv sync

# Keep lockfile updated
uv lock --upgrade

# Use project isolation
uv venv
uv pip install -r requirements.txt

# Fast development iterations
uv run python script.py
```

### Environment Configuration
```powershell
# Use .env file for persistence
echo 'EMBEDDING_MODEL=your-model' >> .env

# Use PowerShell profile for global settings
echo '$env:EMBEDDING_DEVICE = "cuda"' >> $PROFILE
```

### Performance Optimization
- **GPU**: Set `EMBEDDING_DEVICE=cuda` if available
- **Caching**: Configure `EMBEDDING_CACHE_DIR` on fast storage
- **Batch Size**: Adjust `EMBEDDING_BATCH_SIZE` based on memory
- **Model Choice**: Smaller models for speed, larger for accuracy

## 🐛 Troubleshooting

### Common Issues

**UV not found**
```powershell
# Install UV
winget install --id=astral-sh.uv -e
# or
pip install uv
```

**Model loading fails**
```powershell
# Check environment variables
python test_env_config.py

# Clear cache and retry
python -c "from src.tools import clear_embedding_cache; clear_embedding_cache()"
```

**Slow performance**
```powershell
# Check model info
python test_model_info.py

# Enable GPU if available
$env:EMBEDDING_DEVICE = "cuda"
```

**Dependency conflicts**
```powershell
# Reset environment with UV
uv sync --force

# Or clean install
uv venv --force
uv sync
```

### Debug Commands
```powershell
# Check Python environment
uv run python --version

# Test MCP tools
python -c "from src.tools import echo; print(echo('test'))"

# Analyze dependencies
python analyze_dependencies.py

# Performance check
python -c "from src.tools import get_performance_metrics; print(get_performance_metrics())"
```

## 🔄 Migration from pip

### Existing pip Project
```powershell
# Generate uv.lock from requirements.txt
uv lock

# Or import existing environment
uv pip freeze > requirements.txt
uv sync
```

### Benefits of UV Migration
- **Speed**: 10-100x faster installation
- **Reliability**: Better dependency resolution
- **Consistency**: Deterministic lockfile builds
- **Modern**: Python packaging best practices

## 📈 Performance Benchmarks

| Operation | pip | UV | Improvement |
|-----------|-----|----| ------------|
| Install requirements.txt | 45s | 2s | 22.5x faster |
| Resolve dependencies | 15s | 0.5s | 30x faster |
| Create venv + install | 60s | 3s | 20x faster |

## 🤝 Contributing

```powershell
# Development setup
uv sync --dev

# Install pre-commit hooks
uv run pre-commit install

# Run tests
uv run pytest

# Code formatting
uv run black .
uv run isort .
```

## 📖 Resources

- [UV Documentation](https://docs.astral.sh/uv/)
- [ChromaDB Documentation](https://docs.trychroma.com/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Sentence Transformers](https://www.sbert.net/)


## 🚨 DISCLAIMERS / TUYÊN BỐ MIỄN TRỪ TRÁCH NHIỆM

### 🤖 AI-Generated Code / Mã nguồn được tạo bởi AI
**⚠️ Ứng dụng này và toàn bộ mã nguồn được tạo ra 100% bởi Artificial Intelligence (AI).**
- Không có sự can thiệp trực tiếp từ con người trong quá trình coding
- Code được sinh ra thông qua AI assistant và automated tools
- Chưa được kiểm thử đầy đủ bởi developer có kinh nghiệm

### 🚫 Commercial Use Warning / Cảnh báo sử dụng thương mại
**Không khuyến khích sử dụng cho mục đích thương mại mà không kiểm chứng kỹ lưỡng:**
- ❌ Không sử dụng trực tiếp trong production environment
- ❌ Không triển khai cho khách hàng mà không testing
- ✅ Chỉ dùng cho mục đích học tập, nghiên cứu, prototype
- ✅ Cần review và test kỹ lưỡng trước khi sử dụng thực tế

### 📜 Copyright & Intellectual Property / Bản quyền
**Miễn trừ trách nhiệm về bản quyền và sở hữu trí tuệ:**
- Code có thể chứa patterns/snippets tương tự các open source projects
- AI training data có thể bao gồm copyrighted materials
- Người dùng tự chịu trách nhiệm kiểm tra license compatibility
- Không đảm bảo code hoàn toàn original và không vi phạm bản quyền

### ⚖️ Legal Disclaimer / Miễn trừ trách nhiệm pháp lý
**PHẦN MỀM ĐƯỢC CUNG CẤP TRÊN TINH THẦN NGƯỜI DÙNG TỰ CHỊU TRÁCH NHIỆM VỀ MỌI RỦI RO:**
- Không bảo đảm chất lượng, hiệu suất, hoặc độ tin cậy
- Không chịu trách nhiệm về thiệt hại trực tiếp hoặc gián tiếp
- Không đảm bảo tương thích với mọi hệ thống
- Người dùng tự chịu trách nhiệm backup data và security

### 🔒 Security Warning / Cảnh báo bảo mật
**Cảnh báo về an ninh thông tin:**
- Code chưa được security audit
- Có thể tồn tại vulnerabilities
- Không sử dụng với sensitive data
- Cần implement additional security measures

### 📞 Support & Liability / Hỗ trợ & Trách nhiệm
- ❌ Không cam kết technical support
- ❌ Không chịu trách nhiệm về data loss
- ❌ Không đảm bảo compatibility với future updates
- ✅ Community contributions are welcome

---
**🎯 TÓM TẮT: Đây là experimental AI-generated code. Sử dụng cho mục đích học tập và nghiên cứu. Cần kiểm chứng kỹ lưỡng trước khi áp dụng thực tế. Sử dụng tự chịu rủi ro.**