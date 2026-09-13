# Work-item contract

Each work item should be independently understandable and small enough for a focused implementation context.

## Required fields

- ID and short title
- Parent goal or requirement IDs
- Why this item exists
- In scope
- Out of scope
- Dependencies and blockers
- Acceptance criteria stated as observable outcomes
- Likely files, components, data, or interfaces affected
- Verification plan, including failure and edge cases
- Completion evidence
- Status and next action

## Sizing test

Split an item when it contains unrelated outcomes, crosses several independent subsystems, needs different verification strategies, or cannot be reviewed as one coherent change. Do not split so finely that items become mechanical steps with no independently testable value.

## Execution note

Load only the work item, its direct dependencies, relevant decisions, and the necessary code or artifacts. When new scope appears, record a follow-up item instead of hiding it inside the current one.
