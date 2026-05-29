# Built-in Slash Commands

Slash commands are user-facing shortcuts in the chat UI that automate complex workflows or trigger specialized agent behaviors. 

## Default Commands

- `/goal`: Instructs the agent to run a long-running task (e.g., overnight) and be extra thorough, not stopping until the goal is fully achieved.
- `/schedule`: Runs an instruction on a recurring schedule or sets a one-time timer for the agent to wake up and check status.
- `/grill-me`: Aligns on a plan through an interactive interview. The agent will ask targeted questions to resolve design decisions.

## Custom Commands (Skills)

Users can define custom slash commands by creating `.md` files in the `skills/` directories. For example, a file named `lint.md` placed in `~/.gemini/antigravity/skills/` will become available as the `/lint` command.

*For hundreds of custom slash commands, see the [Awesome Skills](../../external/antigravity-awesome-skills) repository.*
