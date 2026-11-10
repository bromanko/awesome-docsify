# Docsify inventory maintenance

This opt-in, manually triggered workflow investigates three entries from the pinned
catalog and previews one-entry corrections for a maintainer. It checks whether a
showcase still uses Docsify, whether a plugin is explicitly retired, and whether a
name, destination or description is still accurate. It never edits the catalog,
opens correction PRs, comments, reviews or merges.

## Output

The Actions summary records source observations, proposed keep/update/replace/remove
or uncertain decisions, prior discussion findings, validation results and remaining
questions. Only ready proposals receive patches in the downloadable ZIP. Model
sources are agent-reported evidence, not independently certified facts.

One UM workflow owns seven stages: prepare the pinned catalog, investigate entries,
collect prior issues/PRs, review that history, build one-entry proposals, validate
in disposable copies, and render the preview. Failed required stages block the
export. Missing/truncated history or unresolved proposal blockers hold a change.
A closed-unmerged PR alone is not a rejection. Current upstream README freshness
is checked before and after validation; a stale catalog cannot yield a ready patch.

The adapter preserves existing list order, author credits, reference links and
Enterprise Usage prefixes. It does not alphabetize renamed entries or impose
Ratatui-specific scope/typo rules. The catalog's current contribution rules are
included in every packet. A site changing framework is distinct from a temporary
HTTP failure; inactivity/archival alone never proves a plugin should be removed.

## Validation

Native awesome-lint 2.3.0 is pinned through a dependency lock. Supplemental Lychee
0.24.2 checks baseline and edited links; existing unrelated failures are reported
separately. New failures, failures/exclusions affecting the changed entry, missing
positive destination evidence, missing tools or timeouts hold the patch. Checks
have 180-second limits. The upstream README's lint directives are preserved.
These checks establish patch/lint/link behavior, not semantic correctness.

## Fork trial

1. Review and merge this draft integration into the fork's default branch.
2. Configure an `awesome-docsify-review` environment with required reviewers and
   an `ANTHROPIC_API_KEY` environment secret.
3. Set repository variable `UM_FRESHNESS_ENABLED=true`.
4. Manually run **UM freshness review** with a zero-based slice number.

The disabled-by-default workflow has no scheduler or persistent coverage cursor;
record reviewed entries manually. Slice membership can shift when the catalog changes.

The integration uses published UM 0.72.1, official Claude Code 2.1.284 and Opus 5.5
at medium effort. The pinned action is
`useful-machinery/run-action@3b5d29379bc349df8d95b29b599e71701aa1d017`.
The job has a 45-minute timeout but no dollar cap; enabled model usage is billable.
GitHub permissions are read-only and checkout does not persist credentials.
The provider key and read-only token are explicitly passed to the workflow. Normal
agent tools are available, with instructions against external writes or executing
project code; these instructions are not an execution sandbox.

## Local checks

```sh
python3 -m unittest discover -s .um/freshness/tests -v
um workflow validate --source-root .um/freshness --json .um/freshness/workflow.yaml
actionlint .github/workflows/um-freshness.yml .github/workflows/um-freshness-checks.yml
```

This is adapted from the existing seven-stage inventory integration at commit
`91ec0be3aecb93d17b6f18e771ea86b52022f2de`. Its earlier Ratatui results are not
Docsify results. The separate BACKTEST.md records this adaptation's actual run,
current-source replay limits and any held proposals. A GitHub-hosted trial has
not been performed.
