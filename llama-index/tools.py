from llama_index.tools.duckduckgo import DuckDuckGoSearchToolSpec
from llama_index.core.tools import FunctionTool
import os

## Internet search Tool
def internet_search(query: str):
    duckduckgo_spec = DuckDuckGoSearchToolSpec()
    return duckduckgo_spec.duckduckgo_full_search(query)[0]['body']

internet_search_tool = FunctionTool.from_defaults(
    fn=internet_search,
    name="Internet_search",
    description="this tool makes a search on the internet for any topic"
)

## Write not