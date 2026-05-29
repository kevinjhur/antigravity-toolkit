# How to Use: Antigravity CLI (agy)

This guide explains how to apply the Antigravity Toolkit to the Antigravity CLI environment (`agy`).

## 1. Global Setup

The CLI manages its global configuration separately from the IDE, typically in `~/.gemini/antigravity-cli/`.

1. **Global Skills**: Copy global skills to the CLI's skill directory.
   ```bash
   mkdir -p ~/.gemini/antigravity-cli/skills/
   cp -r templates/global/skills/* ~/.gemini/antigravity-cli/skills/
   ```
2. **Settings**: Use the interactive CLI commands to manage settings. Type `/config` or `/settings` while in the `agy` interface to safely modify colors, models, and permissions.
3. **MCP Configuration**: Run the setup script to configure MCP servers for the CLI.
   ```bash
   python tools/setup/setup.py
   ```
   *(Select the option to install to `~/.gemini/antigravity-cli/mcp_config.json` when prompted).*

## 2. Shared Setup

If you want skills to be available in BOTH the IDE and the CLI, you can place them in the shared skills directory:
```bash
mkdir -p ~/.gemini/skills/
cp -r templates/global/skills/* ~/.gemini/skills/
```

## 3. Workspace Setup (Per-Project)

The CLI also respects project-level overrides.
1. Navigate to your project directory.
2. Copy the workspace template:
   ```bash
   cp -r /path/to/antigravity-toolkit/templates/workspace/.agents ./
   ```
3. Any skill placed in `.agents/skills/` will be available as a slash command (e.g., `.agents/skills/lint.md` becomes `/lint`) when you launch `agy` from that directory.
