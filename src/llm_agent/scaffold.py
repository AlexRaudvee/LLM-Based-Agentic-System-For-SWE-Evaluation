from typing import Dict, Any

def react_loop(agent, example: Dict[str, Any], max_iters: int = 6) -> Dict[str, Any]:
    """A minimal ReAct-style loop stub. The agent supplies plan/propose/verify."""
    # thought -> action(tool call) -> observation -> ... -> final
    pass
