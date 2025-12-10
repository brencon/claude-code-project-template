# Claude Code Project Template

A comprehensive, best-practice template for AI-assisted software development with Claude Code.

## Quick Start

1. **Fork or clone this template**
   ```bash
   git clone https://github.com/[YOUR_USERNAME]/claude-code-project-template.git my-project
   cd my-project
   ```

2. **Customize CLAUDE.md**
   - Update project overview
   - Add your build/test/lint commands
   - Define your code style conventions

3. **Start Claude Code**
   ```bash
   claude
   ```

## Template Structure

```
├── .claude/
│   ├── commands/              # Custom slash commands
│   │   ├── brainstorm.md     # /brainstorm - Explore options first
│   │   ├── plan.md           # /plan - Plan before implementing
│   │   ├── debug.md          # /debug - Investigate issues
│   │   ├── review.md         # /review - Code review checklist
│   │   ├── test.md           # /test - Generate tests
│   │   ├── refactor.md       # /refactor - Safe refactoring
│   │   └── commit.md         # /commit - Structured commits
│   ├── settings.json          # Project settings (version controlled)
│   ├── settings.example.json  # Example settings with hooks
│   └── settings.local.json    # Local settings (gitignored)
├── .github/
│   └── workflows/
│       └── claude-code-review.yaml.example  # Auto PR review setup
├── docs/
│   ├── architecture/          # System design documentation
│   ├── decisions/             # Architecture Decision Records
│   ├── references/            # External references and research
│   ├── BEST_PRACTICES.md      # Claude Code best practices guide
│   └── UI_DESIGN_GUIDE.md     # UI/design skill and techniques
├── CLAUDE.md                  # Primary instructions for Claude
├── .gitignore                 # Comprehensive gitignore
└── README.md                  # This file
```

## Included Slash Commands

| Command | Purpose |
|---------|---------|
| `/brainstorm [idea]` | Explore options before committing to an approach |
| `/plan [feature]` | Create implementation plan before coding |
| `/debug [issue]` | Systematic issue investigation |
| `/review [file/path]` | Code review with checklist |
| `/test [target]` | Generate comprehensive tests |
| `/refactor [target]` | Safe, test-verified refactoring |
| `/commit` | Create well-structured commits |

## Customization Guide

### CLAUDE.md
The heart of your Claude Code configuration. Customize these sections:

- **Project Overview**: What your project does
- **Development Commands**: Build, test, lint, run commands
- **Code Style**: Your specific conventions
- **Architecture**: System structure and patterns
- **Important Patterns**: Project-specific patterns with examples

### Adding Custom Commands
Create `.claude/commands/[name].md`:

```markdown
# Command Title

Description of what this command does.

$ARGUMENTS will contain any text passed to the command.

## Instructions
1. Step one
2. Step two
```

Use with: `/name your arguments here`

### Permission Configuration
Edit `.claude/settings.json` to pre-approve safe operations:

```json
{
  "permissions": {
    "allow": [
      "Bash(npm test:*)",
      "Bash(npm run lint:*)"
    ]
  }
}
```

See `.claude/settings.example.json` for comprehensive examples including hooks.

### Hooks Configuration
Add hooks to run commands before/after Claude's tool use:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit",
        "hooks": [{ "type": "command", "command": "npx prettier --write $CLAUDE_FILE_PATH" }]
      }
    ]
  }
}
```

### GitHub PR Review
1. Run `/install-github-app` in Claude Code
2. Rename `.github/workflows/claude-code-review.yaml.example` to `.yaml`
3. Customize the review prompt for your needs

## Best Practices

See [docs/BEST_PRACTICES.md](docs/BEST_PRACTICES.md) for comprehensive guidance on:

- CLAUDE.md configuration
- Permission management
- Workflow optimization
- Advanced techniques
- Anti-patterns to avoid

See [docs/UI_DESIGN_GUIDE.md](docs/UI_DESIGN_GUIDE.md) for:

- Front-end design skill installation
- Design reference sources (Dribbble, V0.dev, Pinterest)
- The "black, white, and one color" rule
- Creating design systems
- Avoiding generic AI aesthetics

## Philosophy

This template embodies key principles:

1. **Keep It Simple**: Claude Code works out of the box. Don't over-engineer.
2. **Brainstorm → Plan → Execute**: Think before coding, get options, then implement.
3. **Test-Driven**: Verify behavior with tests.
4. **Minimal Changes**: Only touch what needs to change. Simple > clever.
5. **Claude as Partner**: Treat Claude as a creative collaborator, not just a code generator.

## Sources

This template synthesizes best practices from:
- Anthropic official documentation and talks
- Claude Code team recommendations
- Community patterns and field experience

## Contributing

Contributions welcome! Please:
1. Follow the existing patterns
2. Update documentation
3. Test with Claude Code
4. Submit a PR with clear description

## License

[Choose your license]

---

*Built for the AI-assisted development era.*
