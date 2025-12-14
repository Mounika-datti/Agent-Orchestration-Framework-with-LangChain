# exceptions.py

class AgentError(Exception):
    """Base class for all agent-related exceptions."""
    pass


class ToolExecutionError(AgentError):
    """Raised when a tool fails to execute properly."""
    def __init__(self, tool_name: str, message: str = ""):
        self.tool_name = tool_name
        self.message = message or f"Tool '{tool_name}' failed to execute."
        super().__init__(self.message)


class MemoryError(AgentError):
    """Raised when there is a memory-related problem."""
    def __init__(self, message: str = "Memory operation failed."):
        super().__init__(message)


class APIKeyError(AgentError):
    """Raised when the API key is missing or invalid."""
    def __init__(self, service_name: str = "Unknown"):
        message = f"{service_name} API key is missing or invalid."
        super().__init__(message)


class LLMExecutionError(AgentError):
    """Raised when the LLM (Gemini) fails to generate a response."""
    def __init__(self, message: str = "LLM failed to generate a response."):
        super().__init__(message)
