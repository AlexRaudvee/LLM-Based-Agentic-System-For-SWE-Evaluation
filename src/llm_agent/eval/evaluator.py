from typing import List, Dict, Any
from .pass_at_k import estimate_pass_at_k

def evaluate_agent(agent, tasks: List[Dict[str, Any]], pass_k: int = 1) -> Dict[str, Any]:
    """Evaluate the agent over tasks and compute pass@k.


    Returns summary dict with pass_at_k and per-item results.
    """
    pass
