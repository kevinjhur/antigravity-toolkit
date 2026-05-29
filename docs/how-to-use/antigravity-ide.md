# How to Use: Antigravity IDE

This guide explains how to apply the Antigravity Toolkit to the Antigravity IDE (the VS Code-based editor).

## 1. Global Setup (Recommended)

Antigravity IDE natively supports global configurations that apply to all your workspaces.

1. **Global Rules**: Copy the global rule template to your home directory.
   ```bash
   cp templates/global/GEMINI.md ~/.gemini/GEMINI.md
   ```
2. **Global Skills**: Copy any global skills you wish to use across all projects.
   ```bash
   mkdir -p ~/.gemini/antigravity/skills/
   cp -r templates/global/skills/* ~/.gemini/antigravity/skills/
   ```
3. **MCP Configuration**: Run the setup script to configure your MCP servers globally.
   ```bash
   python tools/setup/setup.py
   ```
   *(Select the option to install to `~/.gemini/config/mcp_config.json` when prompted).*

## 2. Workspace Setup (Per-Project)

If you need project-specific agent rules, workflows, or personas that override the global settings, use the `.agents/` folder.

1. Navigate to your project directory.
2. Copy the workspace template:
   ```bash
   cp -r /path/to/antigravity-toolkit/templates/workspace/.agents ./
   ```
3. Customize the files in `.agents/rules/` and `.agents/agents/` to fit your specific project needs.

## 3. Extension Recommendations

- **Agent Auto Linker**: (Optional) If you prefer symlinking a central `.agents` directory instead of using the global config, you can install the extension found in `tools/agent-auto-linker/`. *(Note: See KNOWN_ISSUES.md for current bugs).*
- **Mermaid Preview**: Standard VS Code extensions for previewing markdown and mermaid diagrams.
