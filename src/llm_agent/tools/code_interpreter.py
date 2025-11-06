from typing import Dict, Any, Tuple

def run_in_sandbox(code: str, tests: str, timeout_sec: int = 5) -> Tuple[bool, Dict[str, Any]]:
    """Execute candidate code against tests in a restricted environment.

    Return:
        (ok, info) where ok indicates all tests passed; info may include
        stderr/stdout, traceback, and diagnostics.
    """
    pass
