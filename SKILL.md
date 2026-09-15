---
name: issue-driven-ai-development
description: Plan and execute substantial software or digital-product work through a compact specification, small dependency-aware work items, bounded context, verification, review, and durable project notes. Use for new projects, multi-step features, refactors, migrations, or continuing an existing project; skip for trivial one-file edits or simple questions.
---

# Issue-Driven AI Development

Keep requirements visible and execution context small. Treat the approved project record—not chat memory—as the source of truth.

## Shared execution policy

Apply `sazan-efficient-operator` as the execution-efficiency layer. Minimize unnecessary token use, repeated context, narration, and interruptions. Retrieve only the context required for the active work item, continue consecutive safe steps without permission loops, and ask only for genuine blockers. Efficiency must never weaken specification quality, verification, security, durable records, or evidence.

## Scale gate

- For a simple, low-risk change that is clear and independently testable, implement and verify it directly.
- For substantial work, use the full loop below.
- For an existing project, inspect its current state, documentation, tests, and version-control status before proposing new structure. Preserve the user's work and existing conventions.

## Product gate

For a new public skill, agent, application, or monetizable feature, read [references/product-principles.md](references/product-principles.md) before committing to implementation. Public technology products use the Sazan brand, not Zandi Service Center.

## Project loop

1. **Ground the request.** State the problem, target user, desired outcome, constraints, assumptions, non-goals, and unresolved decisions. Ask only questions whose answers materially change the solution.
2. **Create a compact specification.** Define observable acceptance criteria, failure cases, security/privacy concerns, data or interface changes, rollout/rollback needs, and evidence required for completion. Use [references/project-record.md](references/project-record.md) when creating or updating the durable project record.
3. **Decompose the work.** Create small work items that can be understood and verified independently. Each item must include scope, dependencies, acceptance criteria, likely files/components, verification, and explicit exclusions. Use [references/work-item.md](references/work-item.md).
4. **Order execution.** Identify the critical path and safe parallel work. Do not parallelize tasks that modify the same state or depend on unresolved interfaces. Keep only the current item and the minimum relevant project context active.
5. **Execute one bounded item.** Inspect before editing. For behavior changes, prefer a failing test or reproducible check first when practical; then make the smallest coherent implementation. Do not silently expand scope.
6. **Verify and review.** Run the narrow checks first, then relevant broader checks. Review the diff for correctness, regressions, security, maintainability, unintended files, and conformance to the acceptance criteria. Evidence—not confidence—determines completion.
7. **Record the result.** Update the work item and durable project record with decisions, changed files, commands/checks and results, known limitations, blockers, and the next item. For the user's projects, use the established memory chain when its connections are available: agent → Walrus Memory → Second Brain → Obsidian → Loop. Walrus is the long-term agent-memory layer; Second Brain and Obsidian are the human-readable archive; Loop verifies consistency and completion. If a connection is unavailable, continue with the project record and report the unsynchronized layer rather than claiming it was updated.
8. **Version-control checkpoint.** Make a focused commit only when commits are within the user's authorization. Push, create or close GitHub issues, and merge only when explicitly requested or already authorized for the workflow. Never claim these happened without confirming the result.
9. **Close the loop.** Mark an item complete only when every acceptance criterion has evidence. If verification fails, keep it open and record the failure. Re-plan affected downstream items when assumptions or interfaces change.

## Context discipline

- Prefer links and concise summaries over repeatedly loading whole logs, transcripts, or unrelated files.
- Give every decision and requirement a stable identifier when the project is large enough to benefit.
- Separate facts, assumptions, decisions, and open questions.
- Start a fresh execution context for a new work item when the current context is noisy, while carrying forward the item, dependencies, decisions, and required evidence.
- Do not use task decomposition as a substitute for understanding the repository or the user's goal.
- Recall relevant Walrus project memory before substantial planning or resuming work when the configured Walrus/MemWal tools are available. Remember only durable project facts after material decisions or verified outcomes; do not store secrets, credentials, raw tokens, or noisy transient logs.

## Completion contract

Report: outcome, evidence, files or systems changed, unresolved risks, and the next safe step. Say **production-ready** only when production-like validation, operational readiness, security implications, and rollback have actually been checked.

## External tracking

Local project records are the default. When the user wants GitHub tracking, translate the approved work items into a parent issue and child issues without losing dependencies or acceptance criteria. Read [references/github-mapping.md](references/github-mapping.md) before creating or updating issues.
