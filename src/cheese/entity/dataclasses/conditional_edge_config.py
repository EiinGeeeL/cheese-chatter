from cheese.components.edges.evaluators.should_continue_evaluator import ShouldContinueEvaluator
from cheese.entity.edge import StateEvaluator
from dataclasses import dataclass

## ShouldContinueConfig
@dataclass(frozen=True)
class ShouldContinueConfig:
    node_source: str = 'cheeseagent'
    node_path: str = 'tools'
    callable: StateEvaluator = ShouldContinueEvaluator().condition