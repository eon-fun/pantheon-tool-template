import example_tool


def test_main():
    result = example_tool.main({"name": "Test"})
    assert "name" in result and result["name"] == "Test"
