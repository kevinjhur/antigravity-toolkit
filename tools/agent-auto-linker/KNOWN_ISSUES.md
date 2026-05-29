# Known Issues: Agent Auto Linker

The Agent Auto Linker is a VS Code extension designed to automatically symlink a global `.agents` folder into every workspace you open.

## Current Bugs

1. **Unconditional Overwrite**: The extension overwrites the existing `.agents` folder or link on every workspace open, disregarding if the user has intentionally unlinked or modified it.
2. **`.gitignore` Duplication**: It appends `.agents` to `.gitignore` on every open without checking if it already exists, causing infinite duplication over time.
3. **Edge Case Failures**: It does not handle edge cases safely (e.g., if `.agents` is a real folder rather than a symlink, or if there are permission issues).

## Recommendation

Due to these bugs, **it is highly recommended to use the native global configuration system** instead of this extension.

Antigravity natively supports:
- `~/.gemini/GEMINI.md` for global rules
- `~/.gemini/antigravity/skills/` for global skills

You only need the `.agents` folder for project-specific overrides. If you still wish to use this extension, be aware of the issues above. Future versions will address these bugs.
