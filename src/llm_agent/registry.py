class ToolRegistry:
    """Simple registry for tools the agent can call."""
    def __init__(self):
        self._tools = {}

    def register(self, name: str, fn):
        self._tools[name] = fn

    def get(self, name: str):
        return self._tools.get(name)

    def names(self):
        return list(self._tools.keys())
