# Durable project record

Use or adapt this structure; do not overwrite an established project format.

## Project snapshot

- Outcome and target user
- Current phase and status
- Constraints and non-goals
- Architecture or workflow summary
- Requirements with stable IDs
- Decisions with date, rationale, and affected work items
- Open questions and blockers
- Work-item index with dependencies and status
- Verification evidence
- Known limitations and risks
- Next safe action

Update the record after a material decision, interface change, completed work item, failed verification, or change of plan. Keep it concise enough to reload without flooding context. Link to detailed artifacts instead of duplicating them.

For an Obsidian vault, prefer normal Markdown, relative links, and the vault's existing folders and metadata. Do not create a second competing project record.

## Walrus memory mapping

When Walrus Memory through MemWal is configured and available:

- Recall by project name, stable requirement IDs, decision IDs, and active work-item IDs before resuming substantial work.
- Remember durable decisions, verified milestones, blockers, interface contracts, and the next safe action.
- Store concise facts with stable identifiers and links to the human-readable project record where possible.
- Mirror the readable record into Second Brain/Obsidian and use Loop to check that Walrus state and the readable archive do not contradict each other.
- Never store passwords, delegate keys, private keys, access tokens, credential files, or secret values in project memory.
- Treat an unavailable or failed memory call as an explicit synchronization gap, not as proof that no prior memory exists.
