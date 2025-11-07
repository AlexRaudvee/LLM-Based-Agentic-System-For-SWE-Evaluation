from typing import TypedDict, List, Optional, Dict, Any

class AgentState(TypedDict, total=False):
    task_id: str
    buggy_code: str
    tests: str
    scratchpad: List[str]
    patch: Optional[str]
    passed: bool
    iter: int
    max_iters: int
    logs: List[Dict[str, Any]]
