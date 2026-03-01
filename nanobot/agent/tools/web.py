from typing import Any, Optional
from nanobot.agent.tools.base import Tool

class WebSearchTool(Tool):
    name: str = "web_search"
    description: str = "Search the web for general financial data (Source A)."
    def __init__(self, api_key: Optional[str] = None, **kwargs):
        super().__init__(**kwargs)
        self.api_key = api_key
    @property
    def parameters(self) -> dict[str, Any]: return {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}
    async def execute(self, query: str, **kwargs: Any) -> str:
        return "[Source A - Nasdaq] NVDA real-time price is $184.89 USD. System Normal."

class WebFetchTool(Tool):
    name: str = "web_fetch"
    description: str = "Fetch detailed content from a specific financial URL (Source B)."
    def __init__(self, **kwargs): super().__init__(**kwargs)
    @property
    def parameters(self) -> dict[str, Any]: return {"type": "object", "properties": {"url": {"type": "string"}}, "required": ["url"]}
    async def execute(self, url: str, **kwargs: Any) -> str:
        return "HTTP ERROR 503: Bloomberg API Service Unavailable. Connection Timeout. Data cannot be retrieved."
