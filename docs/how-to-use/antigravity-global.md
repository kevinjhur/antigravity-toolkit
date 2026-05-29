# How to Use: Antigravity Global Settings

This guide explains the priority and structure of global settings across the Antigravity ecosystem. 

Antigravity categorizes customizations into two scopes: **Workspace** and **Global**.

| Feature | Workspace Scope | Global Scope | Shared Scope |
| :--- | :--- | :--- | :--- |
| **Path** | `<workspace-root>/.agents/` | `~/.gemini/antigravity/` (IDE) or `~/.gemini/antigravity-cli/` (CLI) | `~/.gemini/` |
| **Priority** | **Highest** (Overrides global) | Secondary (Fallback) | Shared across tools |

## 1. Global Rules
The primary file for global system behavior rules is located at:
`~/.gemini/GEMINI.md`

Rules defined here will apply to all Antigravity agents regardless of the project they are working on, unless explicitly overridden by a workspace rule.

## 2. Global Skills
Skills are reusable slash commands and knowledge packages.
- **IDE Global Skills**: `~/.gemini/antigravity/skills/`
- **CLI Global Skills**: `~/.gemini/antigravity-cli/skills/`
- **Shared Skills**: `~/.gemini/skills/` (Available to both IDE and CLI)

## 3. Global Workflows
Workflows are sequences of steps or prompts saved as markdown files.
- **Location**: `~/.gemini/antigravity/global_workflows/`

## Configuration Resolution Order
When conflicts occur (e.g., a skill named `lint.md` exists in multiple places), Antigravity resolves them in the following priority order:
1. Workspace (`.agents/`)
2. Tool-Specific Global (`~/.gemini/antigravity/` or `~/.gemini/antigravity-cli/`)
3. Shared Global (`~/.gemini/`)

Use global settings for overarching rules (like code quality standards) and workspace settings for project-specific contexts (like persona assignments and framework constraints).
