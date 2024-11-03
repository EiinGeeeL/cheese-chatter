from dataclasses import dataclass

## ShouldContinueConfig
@dataclass(frozen=True)
class ShouldContinueConfig:
    node_source: str = 'cheeseagent'
    node_path: str = 'tools'
