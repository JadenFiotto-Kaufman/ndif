from typing import Any, Dict, List, Union

from pydantic import BaseModel, Field

from ..util import Value


class PromiseModel(BaseModel):
    command: str
    id: str
    args: List


class RequestModel(BaseModel):
    
    args: List
    kwargs: Dict
    model_name: str
    execution_graphs: List[List[str]]
    promises: Dict[str, PromiseModel]
    prompts: List[str]

    id: str = None
    blocking:bool = False