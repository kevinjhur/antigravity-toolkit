# MCP (Model Context Protocol) Server Setup Guide

Antigravity uses MCP servers to extend its capabilities with external tools, APIs, and databases. This guide explains how to configure and troubleshoot the default MCP servers included in the toolkit.

## 🚀 Is Installation Required?

**No, manual installation of individual MCP servers is not needed!**
As long as the `mcp_config.json` file is properly configured, Antigravity will automatically download and run the necessary MCP server packages (via `npx`) upon startup.

## ⚙️ Configuration Location

The primary configuration file is located at:
- **IDE Global**: `~/.gemini/antigravity/mcp_config.json`
- **CLI Global**: `~/.gemini/antigravity-cli/mcp_config.json`
- **Universal Fallback**: `~/.gemini/config/mcp_config.json`

Use the `tools/setup/setup.py` script to automatically generate this file for your OS.

## 🧵 Server-Specific Guides

### 1. Stitch MCP
Connects Google's UI design capabilities to Antigravity.
- **Prerequisites**: Google Cloud SDK (`gcloud`) installed, billing enabled.
- **Authentication**: Run `gcloud auth application-default login`.
- **Config**: Ensure `GOOGLE_CLOUD_PROJECT` matches your GCP Project ID.

### 2. TestSprite MCP
Automated testing integration.
- **Prerequisites**: A TestSprite account.
- **Config**: Set the `TESTSPRITE_API_KEY` environment variable in the config.

### 3. Supabase MCP
Database integration.
- **Config**: Set `SUPABASE_ACCESS_TOKEN` and ensure the project URL is correctly mapped.
