# FastMCP TODO App

A lightweight, conversational TODO application demonstrating the Model Context Protocol (MCP) using [fastmcp](https://github.com/jlowin/fastmcp).  
Control your tasks entirely via natural-language prompts in [Claude Desktop](https://github.com/jlowin/claude-desktop), or via direct MCP JSON calls.

## 🔧 Tools & Resources

- `@mcp.tool()` endpoints for create/update/delete  
- `@mcp.resource()` endpoints for list/fetch

## ⚙️ Transport

- Server-Sent Events (SSE) on `http://localhost:8000/mcp`

## 🚀 Get Started

1. Clone this repo and `cd` into it:
   ```bash
   git clone https://github.com/hitenpratap/mcp-todo-python.git
   cd mcp-todo-python
   ```
2. Install dependencies via Pipenv and run the server:
   ```bash
   pipenv install
   pipenv run python main.py
   ```
3. In Claude Desktop, add an MCP server pointing either to your Python launcher or directly to the HTTP endpoint (see below).
4. Use prompts like “Add a TODO: Buy groceries” or “Show me my open tasks”.

## 🛠 Claude Desktop Configuration

### 1. Let Claude launch your server

Add this to `claude_desktop_config.json` (update paths to match your setup):

```jsonc
{
  "mcpServers": {
    "Todo Server": {
      "command": "/ABSOLUTE/PATH/TO/YOUR/venv/bin/python",
      "args": [
        "/ABSOLUTE/PATH/TO/YOUR/project/todo-mcp/main.py"
      ]
    }
  }
}
```

When you select **Todo Server** in Claude Desktop’s hammer menu, it will spawn:

```bash
/ABSOLUTE/PATH/TO/YOUR/venv/bin/python /ABSOLUTE/PATH/TO/YOUR/project/todo-mcp/main.py
```

and automatically connect to `http://localhost:8000/mcp`.

---

### 2. Connect to an existing HTTP server

If you prefer to run the MCP server yourself (e.g., `pipenv run python main.py`), use the `url` form:

```jsonc
{
  "mcpServers": {
    "Todo Server": {
      "url": "http://localhost:8000/mcp"
    }
  }
}
```

Claude will then send all MCP messages to that endpoint without launching a process.
