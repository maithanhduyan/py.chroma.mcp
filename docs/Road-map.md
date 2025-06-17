```
src/
├── config.py          # ✅ Enhanced với embedding config
├── server.py           # ✅ Thêm new tool endpoints  
├── tools.py            # 🔥 Major update với embedding 
├── embedding/          # 🆕 New module
│   ├── __init__.py
│   ├── manager.py      # Model loading & management
│   ├── chunker.py      # Intelligent text chunking
│   └── auth.py         # HF token management
├── utils/              # 🆕 New utilities
│   ├── __init__.py
│   ├── metrics.py      # Performance & quality metrics
│   └── validators.py   # Input validation
└── __init__.py         # ✅ Update version
```