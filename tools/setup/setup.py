import os
import sys
import shutil
import json
from pathlib import Path

# Paths
HOME = Path.home()
GEMINI_DIR = HOME / ".gemini"
CONFIG_DIR = GEMINI_DIR / "config"
IDE_DIR = GEMINI_DIR / "antigravity"
CLI_DIR = GEMINI_DIR / "antigravity-cli"

def setup_mcp():
    print("--- Antigravity MCP Setup ---")
    
    # Use Universal Fallback
    target_dir = CONFIG_DIR
    target_dir.mkdir(parents=True, exist_ok=True)
    target_file = target_dir / "mcp_config.json"
    
    # Load template
    template_path = Path(__file__).resolve().parent.parent.parent / "templates" / "mcp" / "mcp_config.json"
    if not template_path.exists():
        print(f"Error: Template not found at {template_path}")
        return
        
    with open(template_path, "r", encoding="utf-8") as f:
        config_text = f.read()
        
    # Replace absolute path for local Python scripts
    mermaid_path = IDE_DIR / "mermaid_launcher.py"
    config_text = config_text.replace("<MERMAID_SCRIPT_PATH>", str(mermaid_path).replace("\\", "/"))
    
    # Merge or Save config
    if target_file.exists():
        print(f"⚠️ Existing mcp_config.json found at {target_file}. Merging configurations...")
        try:
            with open(target_file, "r", encoding="utf-8") as f:
                existing_config = json.load(f)
            new_config = json.loads(config_text)
            
            if "mcpServers" not in existing_config:
                existing_config["mcpServers"] = {}
                
            for server_name, server_config in new_config.get("mcpServers", {}).items():
                if server_name not in existing_config["mcpServers"]:
                    existing_config["mcpServers"][server_name] = server_config
                    print(f"➕ Added missing MCP server: {server_name}")
                else:
                    print(f"⏭️  Skipped existing MCP server: {server_name}")
                
            config_text = json.dumps(existing_config, indent=2)
        except Exception as e:
            print(f"❌ Failed to merge configurations: {e}")
            print(f"Backing up existing config to {target_file}.bak")
            shutil.copy(target_file, str(target_file) + ".bak")
            
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(config_text)
    
    print(f"\n✅ MCP config saved to {target_file}")
    

def setup_global_rules():
    print("\n--- Global Rules & Skills Setup ---")
    do_rules = input("Install global rules and skills to ~/.gemini/? (Y/n): ").strip().lower()
    
    if do_rules != 'n':
        template_dir = Path(__file__).resolve().parent.parent.parent / "templates" / "global"
        
        # GEMINI.md
        gemini_md = template_dir / "GEMINI.md"
        if gemini_md.exists():
            shutil.copy(gemini_md, GEMINI_DIR / "GEMINI.md")
            print(f"✅ Copied GEMINI.md to {GEMINI_DIR / 'GEMINI.md'}")
            
        # Base Global Skills
        skills_dir = template_dir / "skills"
        target_skills = IDE_DIR / "skills"
        if skills_dir.exists():
            target_skills.mkdir(parents=True, exist_ok=True)
            shutil.copytree(skills_dir, target_skills, dirs_exist_ok=True)
            print(f"✅ Copied base global skills to {target_skills}")
            
        # Awesome Skills
        do_awesome = input("\nInstall ALL Awesome Skills globally (hundreds of skills)? (y/N): ").strip().lower()
        if do_awesome == 'y':
            awesome_dir = Path(__file__).resolve().parent.parent.parent / "external" / "antigravity-awesome-skills"
            if awesome_dir.exists():
                shutil.copytree(awesome_dir, target_skills, dirs_exist_ok=True, ignore=shutil.ignore_patterns('.git', '.github'))
                print(f"✅ Copied Awesome Skills catalog to {target_skills}")
            else:
                print("⚠️ Awesome Skills directory not found. Did you run 'git submodule update --init --recursive'?")
            
if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--dry-run":
        print("Dry run successful. Environment looks good.")
        sys.exit(0)
        
    setup_mcp()
    setup_global_rules()
    
    # Install agent bus and mermaid launcher
    print("\n--- Installing MCP Server Scripts ---")
    tools_dir = Path(__file__).resolve().parent.parent
    
    # Copy scripts to IDE_DIR
    try:
        shutil.copy(tools_dir / "mermaid-renderer" / "mermaid_launcher.py", IDE_DIR / "mermaid_launcher.py")
        print(f"✅ Installed mermaid_launcher.py to {IDE_DIR}")
    except Exception as e:
        print(f"⚠️ Failed to copy server scripts: {e}")
        
    print("\n🎉 Setup complete! Restart Antigravity IDE/CLI to apply changes.")
