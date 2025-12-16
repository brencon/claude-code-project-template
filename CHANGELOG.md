# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Interactive initialization scripts (`init-project.sh`, `init-project.ps1`) for guided project setup
- `/health` command for diagnosing project configuration
- Example CLAUDE.md templates for common tech stacks:
  - TypeScript + React (frontend)
  - Python + FastAPI (backend)
  - Node.js + Express (backend)
- Test example files for TypeScript, Python, and JavaScript
- Expanded troubleshooting section with 14 common issues and solutions
- Performance expectations section in LLM Council guide (timing, optimization)
- This CHANGELOG file

### Fixed
- Orphaned documentation references in CLAUDE.md (api.md, schema.md)
- Clarified settings.local.json purpose (gitignored, auto-populated)

## [1.1.0] - 2025-12-15

### Added
- **LLM Council** - Multi-model advisory board for decision-making
  - BYOK (Bring Your Own Keys) architecture
  - Support for Anthropic, OpenAI, Google AI, and xAI providers
  - Three-stage deliberation: responses, peer review, chairman synthesis
  - Three consultation modes: `quick`, `full`, `vote`
  - Cost optimization with configurable fast model overrides
- `/council` slash command for consulting the council
- `/council-config` slash command for checking configuration
- Comprehensive LLM Council documentation (`docs/LLM_COUNCIL_GUIDE.md`)
- Environment variable examples for all providers (`.env.example`)

## [1.0.0] - 2025-12-14

### Added
- Initial Claude Code project template
- Core slash commands:
  - `/brainstorm` - Explore options before committing to an approach
  - `/plan` - Create implementation plan before coding
  - `/debug` - Systematic issue investigation
  - `/review` - Code review with checklist
  - `/test` - Generate comprehensive tests
  - `/refactor` - Safe, test-verified refactoring
  - `/commit` - Create well-structured commits
- CLAUDE.md template with comprehensive sections
- Best practices documentation (`docs/BEST_PRACTICES.md`)
- Getting started guide (`docs/GETTING_STARTED.md`)
- UI design guide (`docs/UI_DESIGN_GUIDE.md`)
- Skills guide for building digital employees (`docs/SKILLS_GUIDE.md`)
- Settings configuration with hooks examples
- GitHub Actions workflow example for PR reviews
- Comprehensive .gitignore

---

## Upgrade Guide

### From 1.0.0 to 1.1.0

No breaking changes. To use the new LLM Council feature:

1. Copy `scripts/llm-council/config.example.yaml` to `config.yaml`
2. Set API keys in `.env` (at least 2 providers required)
3. Install dependencies: `pip install -r scripts/llm-council/requirements.txt`
4. Use `/council <question>` to consult the council

### From 1.1.0 to 1.2.0

No breaking changes. New features are additive:

- Run `./init-project.sh` (or `.ps1` on Windows) for guided setup
- Use `/health` to check your configuration
- Check `examples/` for tech stack-specific CLAUDE.md templates

[Unreleased]: https://github.com/brencon/claude-code-project-template/compare/v1.1.0...HEAD
[1.1.0]: https://github.com/brencon/claude-code-project-template/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/brencon/claude-code-project-template/releases/tag/v1.0.0
