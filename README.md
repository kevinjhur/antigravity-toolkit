# Antigravity 2.0 Toolkit

A comprehensive, cross-platform toolkit for optimizing the [Antigravity IDE](https://antigravity.google) and CLI environments. This toolkit consolidates best practices for agent personas, global configurations, and Model Context Protocol (MCP) server setups into a single repository.

## Features

- **Agent Personas & Workflows**: Pre-configured agent personas (PL, QA, BE, FE, SP, GD, SEO), system rules, and standardized workflows.
- **Cross-Platform MCP Setup**: Automated scripts to configure essential MCP servers on Linux, macOS, and Windows.
- **Global & Workspace Configurations**: Templates for `.agents/` (workspace-specific) and `~/.gemini/` (global) scopes.
- **Awesome Skills**: Built-in integration with the extensive [Antigravity Awesome Skills](https://github.com/sickn33/antigravity-awesome-skills) catalog.

## Quick Start

### 1. Clone the repository
```bash
git clone --recurse-submodules https://github.com/yourusername/antigravity-toolkit.git
cd antigravity-toolkit
git submodule update --remote
```

### 2. Run the setup script
Use the setup script appropriate for your operating system:

**For Linux or macOS:**
```bash
./tools/setup/setup.sh
```

**For Windows (PowerShell):**
```powershell
.\tools\setup\setup.ps1
```

### 3. Verify installation
Open the Antigravity IDE and verify your global rules and MCP servers are active. See `docs/how-to-use/antigravity-ide.md` for details.

## Documentation

- [Handbook](docs/handbook.md): The unified guide to the Antigravity multi-agent system.
- **How to Use:**
  - [Antigravity IDE Guide](docs/how-to-use/antigravity-ide.md)
  - [Antigravity CLI Guide](docs/how-to-use/antigravity-cli.md)
  - [Global Configuration Guide](docs/how-to-use/antigravity-global.md)
- [Default Features](docs/default-features/overview.md): Overview of built-in tools, MCPs, and commands.
- [MCP Setup Guide](docs/mcp-guide.md): Details on configuring specific MCP servers.
- [Workspace Guide](docs/workspace-guide.md): Tips for SSHFS and multi-root setups.

## Structure

- `docs/`: Extensive documentation and guides.
- `templates/`: Ready-to-use templates for `.agents/`, global rules, and `mcp_config.json`.
- `tools/`: Utility scripts (setup automation, mermaid renderer, etc.).
- `external/`: Submodules including the massive Awesome Skills catalog.

## License
MIT
