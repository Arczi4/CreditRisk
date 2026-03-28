from pydantic import BaseModel
from typing import List


class Contributors(BaseModel):
    featureNames: List[str]
    contribution: List[float]


class ModelSignals(BaseModel):
    topPositive: Contributors
    topNegative: Contributors
