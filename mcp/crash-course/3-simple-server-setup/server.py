from mcp.server.fastmcp import FastMCP
from dotenv import load_dotenv
import os
import sys

load_dotenv("../.env")

# Create an MCP server
mcp = FastMCP(
    name="Calculator",
    host="0.0.0.0",  # only used for SSE transport (localhost)
    port=8050,       # only used for SSE transport
    stateless_http=True,
)

# Add a simple calculator tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together"""
    return a + b

# Run the server
if __name__ == "__main__":
    transport = "stdio"

    # If you really want to debug env vars, write to STDERR, not STDOUT
    print(
        f"OPENAI_API_KEY first 5 is: {os.getenv('OPENAI_API_KEY')[:5]}",
        file=sys.stderr,
    )

    if transport == "stdio":
        # NO prints to stdout here
        # If you want, this is fine (stderr):
        # print("Running server with stdio transport", file=sys.stderr)
        mcp.run(transport="stdio")
    elif transport == "sse":
        print("Running server with SSE transport")  # stdout is OK for SSE
        mcp.run(transport="sse")
    elif transport == "streamable-http":
        print("Running server with Streamable HTTP transport")
        mcp.run(transport="streamable-http")
    else:
        raise ValueError(f"Unknown transport: {transport}")
        