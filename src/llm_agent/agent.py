from typing import Dict, Any
from .scaffold import react_loop

class BugFixAgent:
    """High-level entrypoint for running the bug-fixing agent."""
    def __init__(self, model_name: str, max_iters: int = 6):
        self.model_name = model_name
        self.max_iters = max_iters

    def plan(self, example: Dict[str, Any]) -> str:
        """Create an initial plan or thought for how to approach the bug."""
        pass

    def propose_patch(self, example: Dict[str, Any], scratchpad: str) -> str:
        """Propose a code patch for the buggy function."""
        pass

    def verify(self, example: Dict[str, Any], patch: str) -> Dict[str, Any]:
        """Run tests in sandbox and return signals (passed, errors, logs)."""
        pass

    def run(self, example: Dict[str, Any]) -> Dict[str, Any]:
        """Run the ReAct loop (or other scaffold) for a single example."""
        return react_loop(agent=self, example=example, max_iters=self.max_iters)
