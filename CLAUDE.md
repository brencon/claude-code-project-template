# Project Instructions for Claude Code

> This file is automatically loaded into context when Claude Code starts.
> It serves as the primary interface for providing Claude with project-specific knowledge.

## Project Overview

<!--
Describe your project here. Include:
- What the project does
- Core technologies and frameworks
- Target audience/users
-->

[PROJECT_NAME] is a [BRIEF_DESCRIPTION].

## Architecture

<!--
Describe the high-level architecture:
- System components
- Data flow
- Key design decisions
-->

```
[Add architecture diagram or description here]
```

## Directory Structure

```
├── .claude/              # Claude Code configuration
│   ├── commands/         # Custom slash commands
│   ├── settings.json     # Project-level settings (version controlled)
│   └── settings.local.json # Local settings (gitignored)
├── .github/
│   └── workflows/        # GitHub Actions (including Claude code review)
├── docs/                 # Project documentation
│   └── references/       # External references and research
├── src/                  # Source code
│   └── [module]/CLAUDE.md  # Optional: module-specific instructions
├── tests/                # Test files
└── CLAUDE.md            # This file - Claude's primary instructions
```

> **Note**: CLAUDE.md files are hierarchical. You can place them in subdirectories
> for module-specific instructions. The most specific (most nested) file takes
> priority when Claude is working in that directory.

## Development Commands

<!--
Document the essential commands Claude needs to know.
These are the commands Claude will use frequently.
-->

### Build & Run
```bash
# Build the project
[BUILD_COMMAND]

# Run the project
[RUN_COMMAND]

# Run in development mode
[DEV_COMMAND]
```

### Testing
```bash
# Run all tests
[TEST_COMMAND]

# Run tests with coverage
[COVERAGE_COMMAND]

# Run specific test file
[SPECIFIC_TEST_COMMAND]
```

### Linting & Formatting
```bash
# Lint the codebase
[LINT_COMMAND]

# Format code
[FORMAT_COMMAND]

# Type checking
[TYPE_CHECK_COMMAND]
```

## Code Style & Conventions

<!--
Define your coding standards. Be specific - Claude follows these closely.
-->

### General Principles
- Write clear, self-documenting code
- Prefer explicit over implicit
- Keep functions small and focused
- Follow the single responsibility principle

### Naming Conventions
- **Files**: `kebab-case.ts` or `PascalCase.tsx` for components
- **Functions**: `camelCase`
- **Classes/Types**: `PascalCase`
- **Constants**: `SCREAMING_SNAKE_CASE`
- **Private members**: Prefix with `_` or use `#` for true private

### Code Organization
- Group imports: external, internal, relative
- Export from index files for cleaner imports
- Keep related code close together

### Comments Policy
- Do NOT add comments that describe "what" the code does
- Only add comments for "why" when the reasoning isn't obvious
- Use JSDoc/TSDoc for public APIs only
- Prefer self-documenting code over comments

## Testing Requirements

<!--
Define testing expectations for new code.
-->

- All new features must include tests
- Aim for [X]% code coverage on new code
- Test file location: `tests/` or `__tests__/` adjacent to source
- Naming convention: `*.test.ts` or `*.spec.ts`

### Test Structure
```typescript
describe('[Feature/Module]', () => {
  describe('[method/function]', () => {
    it('should [expected behavior]', () => {
      // Arrange
      // Act
      // Assert
    });
  });
});
```

## Git Workflow

### Commit Messages
Follow conventional commits:
```
<type>(<scope>): <description>

[optional body]

[optional footer]
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

### Branch Naming
- Feature: `feature/[ticket-id]-brief-description`
- Bugfix: `fix/[ticket-id]-brief-description`
- Hotfix: `hotfix/[ticket-id]-brief-description`

## Important Patterns

<!--
Document patterns that are specific to this project.
Include examples when helpful.
-->

### Error Handling
```typescript
// Example pattern for this project
[ADD_ERROR_HANDLING_PATTERN]
```

### State Management
```typescript
// Example pattern for this project
[ADD_STATE_MANAGEMENT_PATTERN]
```

## External Integrations

<!--
Document APIs, services, and external dependencies.
Include links to documentation.
-->

| Integration | Purpose | Docs |
|-------------|---------|------|
| [SERVICE] | [PURPOSE] | [LINK] |

## Environment Variables

<!--
List required environment variables.
DO NOT include actual values - reference .env.example
-->

| Variable | Description | Required |
|----------|-------------|----------|
| `[VAR_NAME]` | [Description] | Yes/No |

See `.env.example` for all required variables.

## Common Tasks

<!--
Quick reference for tasks Claude will perform frequently.
-->

### Adding a New Feature
1. Create feature branch
2. Implement with tests
3. Run lint and type checks
4. Create PR with description

### Debugging
- Check logs at: `[LOG_LOCATION]`
- Use debugger: `[DEBUG_INSTRUCTIONS]`

### Deployment
- Staging: `[STAGING_DEPLOY_COMMAND]`
- Production: `[PRODUCTION_DEPLOY_COMMAND]`

## Known Issues & Gotchas

<!--
Document things that might trip up Claude or new developers.
-->

- [GOTCHA_1]: [Explanation and workaround]
- [GOTCHA_2]: [Explanation and workaround]

## Additional Context Files

<!--
Reference other documentation that Claude should read when relevant.
Use @ syntax to include files dynamically.
-->

For API documentation, see: @docs/api.md
For database schema, see: @docs/schema.md

---

## Notes for Claude

<!--
Special instructions for Claude Code behavior in this project.
-->

### Before Making Changes
1. Search the codebase to understand existing patterns
2. Check for similar implementations to follow
3. Propose a plan for significant changes
4. Ask clarifying questions when requirements are ambiguous

### When Writing Code
- Follow existing patterns in the codebase
- Run tests after changes
- Run linter and type checker
- Keep changes focused and atomic

### When Stuck
- Use `git log` to understand code evolution
- Search for similar patterns in the codebase
- Check docs/ for additional context
- Ask for clarification rather than guessing
