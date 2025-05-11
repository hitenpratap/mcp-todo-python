# main.py

from fastmcp import FastMCP
from pydantic import BaseModel
from typing import List, Optional

# 1. Instantiate your MCP server
#    - SSE transport on 0.0.0.0:8000
mcp = FastMCP(
    name="TodoServer",
    host="0.0.0.0",
    port=8000,
    transport="sse",  # Server-Sent Events for HTTP clients
    instructions="Manage your TODOs via MCP",
)

# 2. In-memory store (swap out for a DB in prod)
_todos: List["TodoItem"] = []


# 3. Schema
class TodoItem(BaseModel):
    id: int
    task: str
    done: bool = False


# 4. Resources
@mcp.resource("todo:///")
def list_todos() -> List[TodoItem]:
    """Return all TODO items."""
    return _todos


@mcp.resource("todo://{id}")
def get_todo(id: int) -> Optional[TodoItem]:
    """Fetch a single TODO by its ID."""
    for t in _todos:
        if t.id == id:
            return t
    return None


# 5. Tools
@mcp.tool()
def create_todo(task: str) -> TodoItem:
    """Create a new TODO with auto-incremented ID."""
    new_id = max((t.id for t in _todos), default=0) + 1
    todo = TodoItem(id=new_id, task=task)
    _todos.append(todo)
    return todo


@mcp.tool()
def update_todo(id: int, done: bool) -> Optional[TodoItem]:
    """Mark a TODO done or undone."""
    for t in _todos:
        if t.id == id:
            t.done = done
            return t
    return None


@mcp.tool()
def delete_todo(id: int) -> dict:
    """Remove a TODO by ID."""
    global _todos
    before = len(_todos)
    _todos = [t for t in _todos if t.id != id]
    return {"deleted": before - len(_todos)}


# 6. Run the server
if __name__ == "__main__":
    """
    Starts an HTTP‐accessible MCP server on port 8000.
    Clients (e.g. Claude Desktop) can now talk to:
      http://localhost:8000/mcp  (via SSE transport)
    """
    mcp.run()
