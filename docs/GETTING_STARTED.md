# Getting Started with Claude Code Project Template

> A step-by-step guide to using this template for your projects.

## Table of Contents

- [Choosing Your Approach](#choosing-your-approach)
- [Quick Start](#quick-start)
- [Detailed Setup](#detailed-setup)
- [Customization Checklist](#customization-checklist)
- [Syncing Upstream Updates](#syncing-upstream-updates)
- [First Claude Code Session](#first-claude-code-session)

---

## Choosing Your Approach

There are three ways to use this template, each with different tradeoffs:

### Option 1: GitHub Template (Recommended for Most Users)

**Best for:** Starting fresh projects where you want a clean git history.

**Pros:**
- Clean commit history (starts fresh)
- Simple one-click setup on GitHub
- No upstream remote to manage
- Full ownership of your repository

**Cons:**
- Manual effort to sync template updates
- No automatic connection to upstream

**How it works:** GitHub creates a new repository with the template's files but without its git history.

### Option 2: Fork

**Best for:** When you want to contribute back to the template or easily pull updates.

**Pros:**
- Easy to sync upstream changes with `git fetch upstream`
- Can contribute improvements back via PR
- Maintains connection to original template

**Cons:**
- Inherits full commit history
- Fork relationship visible on GitHub
- May have merge conflicts when syncing

**How it works:** Creates a linked copy that maintains a relationship with the original repository.

### Option 3: Clone and Re-initialize

**Best for:** Maximum control, private repositories, or when you don't want any GitHub relationship.

**Pros:**
- Complete independence
- Works with any git hosting (GitLab, Bitbucket, self-hosted)
- Clean history
- Can still add upstream remote for updates

**Cons:**
- More manual setup steps
- No GitHub template/fork UI benefits

---

## Quick Start

### Using GitHub Template (Option 1)

1. Go to [github.com/brencon/claude-code-project-template](https://github.com/brencon/claude-code-project-template)
2. Click **"Use this template"** → **"Create a new repository"**
3. Name your repository and set visibility
4. Click **"Create repository"**
5. Clone your new repository:
   ```bash
   git clone https://github.com/YOUR_USERNAME/your-project.git
   cd your-project
   ```
6. Start Claude Code:
   ```bash
   claude
   ```

### Using Fork (Option 2)

1. Go to [github.com/brencon/claude-code-project-template](https://github.com/brencon/claude-code-project-template)
2. Click **"Fork"**
3. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/claude-code-project-template.git my-project
   cd my-project
   ```
4. (Optional) Rename the remote and add upstream:
   ```bash
   git remote rename origin upstream
   git remote add origin https://github.com/YOUR_USERNAME/my-project.git
   ```
5. Start Claude Code:
   ```bash
   claude
   ```

### Using Clone (Option 3)

```bash
# Clone the template
git clone https://github.com/brencon/claude-code-project-template.git my-project
cd my-project

# Remove original remote and reinitialize
rm -rf .git
git init
git add .
git commit -m "Initial commit from Claude Code project template"

# Add your own remote
git remote add origin https://github.com/YOUR_USERNAME/my-project.git
git push -u origin main

# (Optional) Add template as upstream for future updates
git remote add upstream https://github.com/brencon/claude-code-project-template.git
```

---

## Detailed Setup

### Prerequisites

- **Git** installed and configured
- **Claude Code CLI** installed ([installation guide](https://docs.anthropic.com/claude-code/install))
- **GitHub account** (if using GitHub)
- **Anthropic API key** or Claude subscription

### Step 1: Create Your Repository

Choose one of the approaches above and create your repository.

### Step 2: Customize CLAUDE.md

This is the most important step. Open `CLAUDE.md` and update:

```markdown
## Project Overview
[Describe YOUR project - what it does, who it's for, main features]

## Tech Stack
[List YOUR technologies - language, framework, database, etc.]

## Directory Structure
[Update to reflect YOUR project's structure]

## Development Commands
[Add YOUR build, test, lint, and run commands]

## Code Style
[Document YOUR conventions and preferences]
```

### Step 3: Configure Permissions

Edit `.claude/settings.json` to match your workflow:

```json
{
  "permissions": {
    "allow": [
      "Read(*)",
      "Glob(*)",
      "Grep(*)",
      "Bash(git status:*)",
      "Bash(YOUR_TEST_COMMAND:*)",
      "Bash(YOUR_LINT_COMMAND:*)"
    ]
  }
}
```

### Step 4: Set Up Hooks (Optional)

If you want auto-formatting or type-checking, copy from `settings.example.json`:

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

### Step 5: Review and Customize Commands

Check `.claude/commands/` and modify any commands to fit your workflow:

- `brainstorm.md` - Explore options before coding
- `plan.md` - Create implementation plans
- `debug.md` - Systematic debugging
- `review.md` - Code review checklist
- `test.md` - Test generation
- `refactor.md` - Safe refactoring
- `commit.md` - Commit message creation

### Step 6: Clean Up Template Files

Remove or customize files you don't need:

```bash
# Remove example workflow if not using GitHub Actions
rm .github/workflows/claude-code-review.yaml.example

# Or rename to activate it
mv .github/workflows/claude-code-review.yaml.example .github/workflows/claude-code-review.yaml
```

### Step 7: Commit Your Customizations

```bash
git add .
git commit -m "Customize template for [project name]"
git push
```

---

## Customization Checklist

Use this checklist when setting up a new project:

### Required
- [ ] Update `CLAUDE.md` project overview
- [ ] Add your development commands (build, test, lint, run)
- [ ] Update directory structure documentation
- [ ] Configure `.claude/settings.json` permissions

### Recommended
- [ ] Define code style conventions in `CLAUDE.md`
- [ ] Document architecture in `docs/architecture/`
- [ ] Customize slash commands for your workflow
- [ ] Add project-specific patterns to "Important Patterns" section

### Optional
- [ ] Set up hooks for auto-formatting
- [ ] Configure GitHub Actions for PR review
- [ ] Add MCP servers for your integrations
- [ ] Create custom sub-agents for specialized tasks
- [ ] Install skills (front-end design, etc.)

---

## Syncing Upstream Updates

When the template is updated with new best practices, you can pull those changes into your project.

### If You Used GitHub Template (Option 1)

Since there's no upstream relationship, you'll need to add one:

```bash
# Add template as upstream (one-time setup)
git remote add upstream https://github.com/brencon/claude-code-project-template.git

# Fetch upstream changes
git fetch upstream

# See what changed
git log upstream/main --oneline -10

# Merge specific files you want (recommended)
git checkout upstream/main -- docs/BEST_PRACTICES.md
git checkout upstream/main -- .claude/commands/new-command.md

# Or merge everything (may have conflicts)
git merge upstream/main --allow-unrelated-histories
```

### If You Forked (Option 2)

```bash
# Fetch upstream changes
git fetch upstream

# Merge upstream changes
git merge upstream/main

# Resolve any conflicts, then
git push origin main
```

### If You Cloned and Added Upstream (Option 3)

Same as GitHub Template approach above.

### Best Practices for Syncing

1. **Don't sync everything blindly** - Review changes first with `git diff`
2. **Sync specific files** - Cherry-pick useful updates:
   ```bash
   # Get just the best practices doc
   git checkout upstream/main -- docs/BEST_PRACTICES.md

   # Get a new slash command
   git checkout upstream/main -- .claude/commands/new-command.md
   ```
3. **Keep your CLAUDE.md** - Don't overwrite your project-specific configuration
4. **Sync periodically** - Check monthly for new patterns and commands

### Watching for Updates

Star and watch the template repository to get notified of updates:

1. Go to [github.com/brencon/claude-code-project-template](https://github.com/brencon/claude-code-project-template)
2. Click **"Watch"** → **"Releases only"** or **"All Activity"**
3. Click **"Star"** to bookmark

---

## First Claude Code Session

After setup, here's how to have a productive first session:

### 1. Verify Setup

```bash
cd your-project
claude
```

Claude will automatically read your `CLAUDE.md`.

### 2. Test the Commands

Try the included slash commands:

```
/brainstorm a user authentication system
```

```
/plan adding a REST API endpoint
```

### 3. Ask Claude to Review

A good first prompt:

```
Review the CLAUDE.md file and suggest any improvements
based on the actual codebase structure.
```

### 4. Start Building

Use the Brainstorm → Plan → Execute workflow:

1. `/brainstorm [your feature idea]`
2. Choose an approach
3. Let Claude plan (Shift+Tab twice for plan mode)
4. Execute the plan

---

## Troubleshooting

### Claude Doesn't See CLAUDE.md

- Verify you're in the project root: `pwd`
- Check file exists: `ls CLAUDE.md`
- Restart Claude Code: exit and run `claude` again

### Permissions Keep Prompting

- Review `.claude/settings.json`
- Add frequently-used commands to the allow list
- Use Shift+Tab for auto-accept mode during development

### Slash Commands Not Working

- Check `.claude/commands/` directory exists
- Verify `.md` extension on command files
- Commands are case-sensitive

### Upstream Sync Conflicts

- Use `git status` to see conflicting files
- Keep your customizations, take upstream's documentation updates
- When in doubt, cherry-pick specific files instead of merging all

---

## Next Steps

1. **Read the docs:**
   - [BEST_PRACTICES.md](BEST_PRACTICES.md) - Comprehensive Claude Code guidance
   - [UI_DESIGN_GUIDE.md](UI_DESIGN_GUIDE.md) - Better UI with design skills
   - [SKILLS_GUIDE.md](SKILLS_GUIDE.md) - Building specialized AI workflows

2. **Customize for your stack:**
   - Add language-specific linting commands
   - Configure framework-specific patterns
   - Document your testing conventions

3. **Iterate:**
   - Add memories with `#` as you work
   - Update CLAUDE.md when you find new patterns
   - Create custom commands for repetitive tasks

---

*Welcome to AI-assisted development. Build something great.*
