---
mode: agent
---

# Darwin Testing Philosophy Prompt

## Testing Mindset
Embrace Charles Darwin's scientific method: hypothesis, experimentation, observation, and adaptation. Apply evolutionary thinking to testing - let the strongest tests survive and weak tests be eliminated.

## Core Testing Principles
1. **Scientific Method**: Every test is a hypothesis about system behavior
2. **Natural Selection**: Only robust, valuable tests should survive in the codebase
3. **Adaptation**: Tests must evolve with the codebase to remain relevant
4. **Survival of the Fittest**: High-quality tests that catch real bugs survive, flaky tests are eliminated
5. **Observation**: Tests should provide clear evidence of system health
6. **Reproducibility**: Every test result must be reproducible across environments

## Test Categories Evolution

### 1. Unit Tests (Cellular Level)
- Test individual functions and methods in isolation
- Fast execution (< 100ms per test)
- No external dependencies
- High coverage of edge cases and error conditions
- Mock external dependencies

### 2. Integration Tests (Organism Level)
- Test component interactions and data flow
- Include database operations, file I/O, network calls
- Test real ChromaDB operations with embeddings
- Validate MCP protocol communications
- Medium execution time (< 5 seconds per test)

### 3. End-to-End Tests (Ecosystem Level)
- Test complete workflows from client to database
- Include Docker container testing
- Validate full MCP server functionality
- Test performance under load
- Longer execution time acceptable (< 30 seconds)

## Testing Structure in `tests/` Directory

```
tests/
├── unit/
│   ├── test_config.py          # Test configuration management
│   ├── test_tools.py           # Test ChromaDB operations
│   └── test_server.py          # Test MCP server logic
├── integration/
│   ├── test_chroma_integration.py    # Test real ChromaDB operations
│   ├── test_mcp_protocol.py          # Test MCP communication
│   └── test_embedding_workflow.py    # Test embedding pipeline
├── e2e/
│   ├── test_docker_deployment.py     # Test containerized deployment
│   └── test_full_workflow.py         # Test complete user scenarios
├── fixtures/
│   ├── sample_documents.json         # Test data
│   └── mock_embeddings.json          # Mock embedding data
└── conftest.py                      # Pytest configuration and fixtures
```

## Test Writing Guidelines

### Test Naming Convention (Darwin Species Classification)
- `test_[component]_[behavior]_[condition]`
- Example: `test_chroma_query_returns_relevant_documents`
- Example: `test_server_handles_invalid_request_gracefully`

### Test Structure (Scientific Method)
```python
def test_hypothesis_name():
    # Arrange (Hypothesis Setup)
    # Act (Experiment)
    # Assert (Observation)
    # Cleanup (Reset Environment)
```

### Assertion Quality (Natural Selection)
- Use specific, meaningful assertions
- Test both positive and negative cases
- Include boundary conditions
- Validate error messages and types
- Check performance characteristics when relevant

## Required Test Coverage Areas

### 1. ChromaDB Operations
- Document addition and retrieval
- Vector similarity search
- Collection management
- Embedding generation and storage
- Error handling for invalid inputs

### 2. MCP Protocol
- Request/response handling
- Tool execution validation
- Error propagation
- Protocol compliance

### 3. Configuration Management
- Environment variable loading
- Default value handling
- Invalid configuration detection

### 4. Performance & Resource Management
- Memory usage under load
- Response time benchmarks
- Connection pooling efficiency
- Embedding computation performance

## Test Quality Metrics (Fitness Indicators)

### Code Coverage
- Aim for >90% line coverage
- Focus on branch coverage for decision points
- Exclude trivial getters/setters from coverage requirements

### Test Reliability
- Zero flaky tests tolerance
- Deterministic test results
- Independent test execution (no test dependencies)

### Performance Benchmarks
- Unit tests: < 100ms each
- Integration tests: < 5 seconds each
- Total test suite: < 2 minutes

## Mock Strategy (Controlled Environment)
- Mock external APIs and services
- Use real ChromaDB for integration tests with test data
- Mock file system operations in unit tests
- Provide fixture data for consistent testing

## Continuous Evolution
- Regularly review and refactor tests
- Remove obsolete tests when functionality changes
- Add tests for every bug discovered
- Update tests when requirements evolve

## Error Testing Philosophy
Test failure modes extensively:
- Network timeouts and connection errors
- Invalid input data and malformed requests
- Resource exhaustion scenarios
- Concurrent access patterns
- Database corruption recovery

Remember: "It is not the strongest tests that survive, but the most adaptable to change."
