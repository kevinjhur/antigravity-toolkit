# Antigravity Workspace Management Guide

This document explains how to efficiently manage workspaces (`.code-workspace`) in Antigravity and set up a Local + Remote hybrid environment.

## 1. Managing `.code-workspace` Files

The workspace configuration file (`.code-workspace`) contains folder structures and dedicated settings for a project.

### Location and Management
- **Location**: It is recommended to save this on a local path (e.g., `C:\Workspaces\MyProject.code-workspace` or `~/Workspaces/MyProject.code-workspace`).
- **Exclude from Git**: This file often contains user-specific absolute paths, so it should **NOT** be committed to Git.
- **.gitignore Setup**:
  ```gitignore
  *.code-workspace
  ```

### How to Open
Antigravity does not automatically open workspace files found in subdirectories.
1. **File Explorer**: Double-click the `.code-workspace` file.
2. **Menu**: `File > Open Workspace from File...`
3. **Recent**: `File > Open Recent` (Most convenient)

---

## 2. Hybrid Workspace (Local + Remote)

Antigravity natively separates Local and Remote (SSH) windows. However, by using **SSHFS**, you can manage them within a single window.

### Mounting Remote Folders as Local Drives (SSHFS)
Map a remote Linux folder to a local network drive (e.g., `Z:`) so Antigravity treats it as a local folder.

#### Windows Setup
1. **Install**:
   - [WinFsp](https://github.com/winfsp/winfsp/releases)
   - [SSHFS-Win](https://github.com/winfsp/sshfs-win/releases)
2. **Connect**:
   - Open File Explorer > **Map network drive**
   - Enter Folder address: `\\sshfs\username@remote_ip` (e.g., `\\sshfs\ubuntu@192.168.0.5`)
   - Enter password to connect -> **Z: Drive** is created.

#### macOS / Linux Setup
- Use `sshfs` via Homebrew (`brew install macfuse sshfs`) or apt (`sudo apt install sshfs`).
- Mount: `sshfs username@remote_ip:/remote/path /local/mount/point`

#### Workspace Configuration
1. Open your local project in Antigravity.
2. Select `File > Add Folder to Workspace...`.
3. Navigate to your mapped drive/mount point and add the remote folder.
4. `Save Workspace As...`
*Now you can edit local code and remote code simultaneously in one window!*

---

## 3. Utilizing Multi-Root Workspaces

Having multiple root folders in a single workspace provides several advantages:
- **Independent Settings**: Manage `.vscode/settings.json` separately for each folder.
- **Unified Search**: Search across all folders simultaneously using global search.
- **Extension Isolation**: Configure specific extensions to run only on designated folders.
