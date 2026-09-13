# Issue-Driven AI Development

An Agent Skill for building software with AI without overwhelming the model's context window.

An open-source project by **Sazan**.

Large prompts bury important requirements in noise. This skill turns substantial software work into a compact specification and small, dependency-aware issues. Each issue carries its own acceptance criteria and verification plan, then moves through implementation, testing, review, evidence, and documentation.

## What it improves

- Keeps the active context focused on one coherent work item
- Converts vague requests into testable acceptance criteria
- Makes dependencies and parallel work explicit
- Encourages test-first development when practical
- Prevents unverified work from being marked complete
- Preserves decisions and progress in durable project records
- Integrates with Walrus Memory as a long-term agent-memory layer when configured
- Supports GitHub parent/child issue tracking without requiring it

## Workflow

1. Ground the request and define non-goals.
2. Write a compact, testable specification.
3. Decompose it into independently verifiable work items.
4. Order dependencies and safe parallel work.
5. Execute one bounded item at a time.
6. Test and review against acceptance criteria.
7. Record evidence, decisions, limitations, and the next action.
8. Commit or update GitHub only when authorized.
9. Close the item only after verification succeeds.

For the owner's project environment, the intended continuity chain is: agent → Walrus Memory → Second Brain → Obsidian → Loop. Secrets and delegate keys are never written into project memory.

## Installation

Copy this repository into your Codex skills directory:

```bash
git clone https://github.com/samzandi/issue-driven-ai-development.git ~/.codex/skills/issue-driven-ai-development
```

Restart the relevant Codex session so the skill catalog refreshes. The skill allows implicit invocation for substantial software and digital-product work. You can also invoke it explicitly:

```text
Use $issue-driven-ai-development to plan and build this feature.
```

## Scope

Use it for new projects, multi-step features, migrations, and substantial refactors. It intentionally skips heavyweight planning for trivial edits and simple questions.

## Repository structure

- `SKILL.md`: routing and execution rules
- `agents/openai.yaml`: Codex UI metadata
- `references/project-record.md`: durable project-memory structure
- `references/work-item.md`: issue contract and sizing rules
- `references/github-mapping.md`: safe mapping to GitHub issues and pull requests
- `references/product-principles.md`: Sazan's product, quality, revenue, and distribution gate

## Design influences

The approach combines spec-driven development, issue-based decomposition, context engineering, test-driven development, and evidence-based completion. It is designed to be tool-agnostic while integrating cleanly with Codex and GitHub.

## Contributing

Open an issue with a concrete failure case or workflow improvement. Changes should remain focused, preserve user authorization boundaries, and include evidence that they improve real project execution.

## License

MIT
