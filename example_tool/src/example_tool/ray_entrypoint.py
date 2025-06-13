from typing import Any

import ray
from pydantic import BaseModel, Json

from example_tool.main import main as tool_main


class InputModel(BaseModel):
    answer: Json[Any]


class OutputModel(BaseModel):
    result: Any


@ray.workflow.options(checkpoint=True)
@ray.remote(max_retries=3, retry_exceptions=True)
def main(*args, **kwargs):
    """
    Remote wrapper for executing the main function. It validates inputs using pydantic models, executes main
    function, and returns outputs as dict using pydantic models.

    (!!!) Please note, that this is done inside a distributed Ray environment
    and keep inputs/outputs serializable for agent use.
    """
    output = tool_main(**InputModel(*args, **kwargs).model_dump())
    return OutputModel(result=output).model_dump()


def run_remote():
    """
    Initializes Ray, executes the remote function, and prints the result.
    """
    ray.init(ignore_reinit_error=True)

    result = ray.get(main.remote({"answer": "{'answer': 'Hello, world!'}"}))
    print("Remote execution result:", result)
    ray.shutdown()


if __name__ == "__main__":
    run_remote()
