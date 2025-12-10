# Claude Code Best Practices

> Synthesized from Anthropic documentation, expert guidance, and field experience.

## Understanding Claude Code

### How It Works
Claude Code is a **pure agent** architecture:
- Instructions + powerful tools + model running in a loop until completion
- No indexing or RAG - uses agentic search (glob, grep, find) to explore codebases
- 200K token context window with `/clear` and `/compact` for management
- Lightweight permission system for dangerous operations

### Mental Model
Think of Claude Code as a skilled terminal-native coworker who:
- Explores codebases the way a new team member would
- Uses standard tools (git, grep, find) rather than magic indexing
- Works iteratively, searching and refining understanding
- Can be interrupted and redirected at any time

---

## Configuration Best Practices

### CLAUDE.md Files

**Purpose**: Primary way to share state across sessions and team members.

**Locations** (in order of precedence):
1. Project root (`./CLAUDE.md`) - shared via version control
2. Home directory (`~/.claude/CLAUDE.md`) - personal defaults
3. Subdirectories - read by Claude when relevant, not auto-loaded

**Content Guidelines**:
- Keep it focused and concise
- Update when switching model versions
- Include only what Claude needs to know
- Remove outdated instructions

**Essential Sections**:
```markdown
## Project Overview
Brief description of what this project does

## Development Commands
How to build, test, lint, run

## Code Style
Specific conventions for this project

## Architecture
High-level structure and patterns
```

### Permission Management

**Speed up workflows by pre-approving safe commands**:
```json
{
  "permissions": {
    "allow": [
      "Read(*)",
      "Bash(npm test:*)",
      "Bash(npm run lint:*)",
      "Bash(git status:*)"
    ]
  }
}
```

**Use Shift+Tab** for auto-accept mode when in flow.

---

## Workflow Best Practices

### Planning First
Instead of diving straight into implementation:

```
❌ "Fix the login bug"
✅ "Search the codebase for the login implementation, understand
    how authentication works, and propose 2-3 options for fixing
    the bug. Don't start coding yet."
```

### Test-Driven Development
1. Write or verify tests exist
2. Make small changes
3. Run tests after each change
4. Commit when tests pass
5. Repeat

### Context Management

**Watch the context window**:
- `/clear` - Start fresh (keeps CLAUDE.md)
- `/compact` - Summarize and continue

**When to use each**:
- `/compact`: Continuing related work, need history
- `/clear`: Switching to unrelated task

### Using the Todo List
- Watch for items that don't make sense
- Press `Escape` to redirect if Claude is off track
- Use todos for visibility into Claude's plan

---

## Advanced Techniques

### Multiple Claude Instances
Run 2-4 instances for parallel work:
- Different features in different terminals
- Use shared markdown files for coordination
- Example: Write to `ticket.md` for context passing

### Escape Key Mastery
- **Single Escape**: Stop and redirect
- **Double Escape**: Jump back in conversation history
- Know when to escape vs. let Claude figure it out

### Screenshot-Driven Development
Claude is multimodal:
- Paste screenshots for visual debugging
- Reference mock images: "Build this UI from mock.png"
- Use for error screenshots, design specs

### Extended Thinking
For complex problems, add "think hard" to prompts:
```
"Think hard about this bug. Search the codebase,
understand the data flow, and explain what's causing it."
```

---

## Integration Tips

### CLI Tools vs MCP Servers
**Prefer CLI tools** when:
- Tool is well-known and documented
- Examples: `gh` (GitHub), `docker`, `aws`

**Use MCP servers** when:
- Need custom integrations
- CLI doesn't exist or is limited
- Need structured data exchange

### Git Integration
Claude excels at:
- Writing commit messages and PR descriptions
- Understanding code history (`git log`, `git blame`)
- Resolving merge conflicts
- Managing rebases

Tell Claude about sticky situations:
```
"I'm in the middle of a rebase with conflicts.
Help me resolve them and continue."
```

---

## Anti-Patterns to Avoid

### Over-Prompting
❌ Repeating instructions already in CLAUDE.md
✅ Trust that CLAUDE.md is loaded and followed

### Context Bloat
❌ Letting context fill up without compacting
✅ Regular `/compact` for long sessions

### Micro-Management
❌ Approving every single file read
✅ Configure permissions for read operations

### Ignoring the Todo List
❌ Not watching what Claude plans to do
✅ Review todo items, escape if off-track

### Skipping Tests
❌ "Just implement it, we'll test later"
✅ "Implement with tests, verify they pass"

---

## Sources

This document synthesizes best practices from:
- Anthropic official documentation
- Claude Code team recommendations
- Community patterns and experiences

*Last updated: [DATE]*
*Claude Code version: [VERSION]*
