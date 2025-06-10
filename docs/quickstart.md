# Quickstart Guide

This guide will help you create a new Pantheon tool using this template.

## Step 1: Create Repository from Template

1. Click the green **"Use this template"** button at the top of this repository
2. Choose "Create a new repository"
3. Enter your new repository name (e.g., `my-awesome-tool`)
4. Choose visibility (public/private)
5. Click "Create repository from template"

## Step 2: Clone Your New Repository

```bash
git clone https://github.com/your-username/your-new-tool-repo.git
cd your-new-tool-repo
```

## Step 3: Rename `example_tool` (IMPORTANT!)

You **must** rename the `example_tool` directory and all references to match your new tool name:

1. **Rename the directory:**
   ```bash
   mv example_tool your_tool_name
   mv your_tool_name/example_tool your_tool_name/your_tool_name
   ```

2. **Update all code references:**
   - In `your_tool_name/your_tool_name/ray_entrypoint.py`: Change `from example_tool.main import main as tool_main` to `from your_tool_name.main import main as tool_main`
   - In `your_tool_name/tests/test_example.py`: Change `import example_tool` to `import your_tool_name` and update the test calls
   - In `your_tool_name/pyproject.toml`: Change `name = "example_tool"` to `name = "your_tool_name"` and update the entry point
   - In `your_tool_name/README.md`: Replace all mentions of `example_tool` with `your_tool_name`

3. **Update CI workflows:**
   - In `.github/workflows/lint.yml`: Change `poetry run ruff check .` and `poetry run ruff format --check .` to use your tool name in the working-directory
   - In `.github/workflows/test.yml`: Change `working-directory: example_tool` to `working-directory: your_tool_name` and update poetry commands accordingly

## Step 4: Install Dependencies

Navigate to your tool directory and install in development mode:

```bash
cd your_tool_name
pip install -e .[dev]
```

This will install your tool package along with all development dependencies including Ray and pytest.

## Step 5: Run Tests

Verify everything works by running the tests:

```bash
pytest
```

You should see all tests pass successfully.

## Step 6: Develop Your Tool

Now you can start developing your actual tool functionality:

1. **Edit `your_tool_name/main.py`**: Implement your core tool logic
2. **Update `your_tool_name/ray_entrypoint.py`**: Modify input/output models as needed
3. **Write tests**: Add comprehensive tests in `tests/`
4. **Update documentation**: Modify the README.md to describe your tool

## Step 7: Commit and Push

Once you've customized your tool:

```bash
git add .
git commit -m "Initial setup of my custom tool"
git push origin main
```

## Tips

- Keep the Ray and Pydantic structure intact for compatibility with Pantheon
- The CI workflows will automatically run on every push
- Follow the existing code patterns for consistency
- Add more tests as you develop new features

Happy building! 🚀