# Built-in Tools

Antigravity equips its agents with a powerful set of native tools that allow them to autonomously navigate, analyze, and modify codebases.

## File & File System Tools
- `view_file`: Read contents of files (supports text, images, PDFs, videos, and audio).
- `list_dir`: Recursively list all files and subdirectories within a path.
- `grep_search`: Find exact pattern matches within files or directories (equivalent to ripgrep).
- `write_to_file`: Create new files (supports artifact generation).
- `replace_file_content`: Make a single contiguous block of edits to an existing file.
- `multi_replace_file_content`: Make multiple, non-contiguous edits to an existing file.

## Execution & Task Management
- `run_command`: Propose a command to run on the user's terminal (requires user approval). Supports persistent terminals and async background execution.
- `manage_task`: Interact with background tasks (list, kill, status, send_input).
- `schedule`: Schedule one-shot timers or recurring cron jobs for background notifications.

## Information & Context
- `search_web`: Perform web searches and retrieve summarized information with URL citations.
- `read_url_content`: Fetch and convert HTML to markdown via HTTP request (for static pages).
- `ask_question`: Open an interactive modal to ask the user multiple-choice questions for clarification.

## Creative & Design
- `generate_image`: Generate UI mockups, design assets, and edit existing images based on text prompts.

## MCP Integration
- `list_resources`: List available resources from an MCP server.
- `read_resource`: Retrieve contents from a specific MCP resource.
- `call_mcp_tool`: Call lazily-loaded MCP tools (requires parsing schema first).
