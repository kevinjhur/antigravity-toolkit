# Built-in Settings

This document outlines the core configuration settings for the Antigravity IDE and CLI.

## Antigravity IDE
The IDE settings are largely managed through the VS Code settings UI (`settings.json`).
- **Model Selection**: Switch between models (e.g., Gemini 3.1 Pro, Claude Opus) via the UI dropdown.
- **MCP Config**: `~/.gemini/antigravity/mcp_config.json`

## Antigravity CLI (agy)
The CLI configuration is stored centrally.
- **Settings File**: `~/.gemini/antigravity-cli/settings.json`
- **Keybindings**: `~/.gemini/antigravity-cli/keybindings.json`
- **Management**: You can edit settings interactively within the CLI by typing `/config` or `/settings`.

## Knowledge Items (KI)
Knowledge Items are curated context summaries stored in `~/.gemini/antigravity/knowledge/`.
- The system automatically checks KI summaries at the start of conversations to recall established repository patterns and avoid redundant work.
