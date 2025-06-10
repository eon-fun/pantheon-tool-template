# Pantheon Tool Template

A comprehensive template repository for creating new Pantheon tools. This template provides a production-ready foundation with best practices, example implementations, automated CI/CD pipelines, and comprehensive documentation to accelerate the development of robust tool packages for the Pantheon platform.

## 🎯 What are Pantheon Tools?

Pantheon tools are distributed, containerized microservices that provide specific functionality within the Pantheon ecosystem. Each tool is designed to:

- **Execute in distributed environments** using Ray for scalability
- **Validate inputs and outputs** with Pydantic for type safety
- **Integrate seamlessly** with the Pantheon agent platform
- **Scale horizontally** across multiple nodes and environments
- **Maintain reliability** through built-in retry mechanisms and checkpointing

## 🚀 Quick Start

### Option 1: Use GitHub Template (Recommended)

1. Click the green **"Use this template"** button above
2. Create your new repository
3. Follow the [quickstart guide](docs/quickstart.md)

### Option 2: Clone and Adapt

```bash
git clone https://github.com/eon-fun/pantheon-tool-template.git my-new-tool
cd my-new-tool
# Follow the quickstart guide to rename and customize
```

## 📁 Project Structure

```
pantheon-tool-template/
├── .github/workflows/          # CI/CD automation
│   ├── lint.yml               # Code quality checks (ruff)
│   └── test.yml               # Automated testing (pytest)
├── docs/                      # Documentation
│   └── quickstart.md          # Step-by-step setup guide
├── example_tool/              # Your tool implementation
│   ├── example_tool/          # Core tool package
│   │   ├── __init__.py        # Package initialization
│   │   ├── main.py            # Core business logic
│   │   └── ray_entrypoint.py  # Ray distributed execution wrapper
│   ├── tests/                 # Test suite
│   │   └── test_example.py    # Unit tests
│   ├── pyproject.toml         # Dependencies and configuration
│   └── README.md              # Tool-specific documentation
├── LICENSE                    # MIT License
└── README.md                  # This file
```

## 🛠 What's Included

### Core Components

- **🎛 Working Example Tool**: Complete implementation demonstrating best practices
- **🔧 Ray Integration**: Distributed execution with automatic retries and checkpointing
- **✅ Type Safety**: Pydantic models for input/output validation
- **🧪 Test Suite**: pytest-based testing with coverage reporting
- **📝 Documentation**: Comprehensive guides and examples

### Development Tools

- **🔍 Code Quality**: ruff linting and formatting
- **🚀 CI/CD Pipeline**: GitHub Actions for automated testing and validation
- **📦 Poetry Integration**: Modern Python dependency management
- **🔄 Pre-configured Workflows**: Ready-to-use GitHub Actions

### Best Practices

- **🎯 Type Hints**: Full type annotation coverage
- **📚 Documentation**: Inline docs and comprehensive README files
- **🧩 Modular Design**: Separation of concerns between business logic and infrastructure
- **🛡 Error Handling**: Robust error handling and retry mechanisms

## 🔧 Technologies & Dependencies

| Technology         | Purpose               | Version  |
| ------------------ | --------------------- | -------- |
| **Python**   | Core language         | ≥3.10   |
| **Ray**      | Distributed execution | ^2.42.1  |
| **Pydantic** | Data validation       | ≥2,<3   |
| **pytest**   | Testing framework     | ^8.3.4   |
| **ruff**     | Linting & formatting  | ^0.11.12 |
| **Poetry**   | Dependency management | Latest   |

## 📋 Development Workflow

1. **Create from Template**: Use GitHub's template feature or clone directly
2. **Customize Structure**: Rename `example_tool` to your tool name
3. **Implement Logic**: Add your business logic to `main.py`
4. **Configure I/O**: Update Pydantic models in `ray_entrypoint.py`
5. **Write Tests**: Add comprehensive tests to the `tests/` directory
6. **Update Documentation**: Modify README files and add usage examples
7. **Test Locally**: Run `poetry run pytest` and `poetry run ruff check`
8. **Deploy**: Push to GitHub for automatic CI/CD validation

## 🎯 Example Use Cases

This template is perfect for creating tools such as:

- **Data Processing Tools**: ETL pipelines, data transformers, analyzers
- **API Integrations**: External service connectors, webhook handlers
- **Computation Tools**: Mathematical operations, ML inference, algorithms
- **Utility Functions**: File processors, format converters, validators
- **Monitoring Tools**: Health checkers, metric collectors, alerting systems

## 🔍 Key Features Explained

### Ray Integration

```python
@ray.workflow.options(checkpoint=True)
@ray.remote(max_retries=3, retry_exceptions=True)
def main(*args, **kwargs):
    # Your tool logic runs in a distributed, fault-tolerant environment
```

### Pydantic Validation

```python
class InputModel(BaseModel):
    answer: Json[Any]  # Automatic validation and serialization

class OutputModel(BaseModel):
    result: Any  # Type-safe outputs
```

### Entry Point Configuration

```toml
[project.entry-points."tool.entrypoint"]
your-tool = "your_tool.ray_entrypoint:main"
```

## 🧪 Testing Your Tool

```bash
# Install dependencies
cd your_tool && poetry install

# Run tests
poetry run pytest

# Check code quality  
poetry run ruff check .
poetry run ruff format --check .

# Test tool functionality
poetry run python -c "import your_tool; print(your_tool.main({'test': 'data'}))"
```

## 🚀 Deployment & Integration

Once your tool is ready:

1. **Package**: Tools are automatically packaged with Poetry
2. **Registry**: Push to your preferred Python package registry
3. **Integration**: Tools integrate with Pantheon agents via entry points
4. **Scaling**: Ray handles distributed execution automatically

## 🤝 Contributing

When using this template:

1. Follow the established code structure
2. Maintain comprehensive test coverage
3. Update documentation as you add features
4. Use semantic versioning for releases
5. Keep dependencies up to date

## 📚 Additional Resources

- **[Quickstart Guide](docs/quickstart.md)**: Detailed setup instructions
- **[Ray Documentation](https://docs.ray.io/)**: Learn about distributed computing
- **[Pydantic Docs](https://docs.pydantic.dev/)**: Master data validation
- **[Poetry Guide](https://python-poetry.org/docs/)**: Dependency management

## 💡 Tips for Success

- **Start Simple**: Begin with the example and gradually add complexity
- **Test Early**: Write tests as you develop features
- **Document Everything**: Future you will thank present you
- **Follow Conventions**: Stick to Python and Ray best practices
- **Monitor Performance**: Use Ray's built-in monitoring tools

## 🆘 Troubleshooting

**Poetry installation issues?**

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

**Ray connection problems?**

```bash
# Check Ray installation
poetry run python -c "import ray; ray.init(ignore_reinit_error=True); print('Ray OK')"
```

**Import errors?**

```bash
# Ensure package is installed in development mode
poetry install
```

---

**Ready to build the next great Pantheon tool?** 🚀

[**Use This Template**](https://github.com/eon-fun/pantheon-tool-template/generate) to get started in seconds!
