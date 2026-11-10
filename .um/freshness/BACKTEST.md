# Docsify retrospective inventory replay

On November 9, 2026, one live run of the adapted seven-stage workflow investigated
three entries from the catalog immediately before [#306](https://github.com/docsifyjs/awesome-docsify/pull/306).
It found the intended framework change, retained an unchanged resource, and found
an additional supported stale browser-support claim. **Both correction proposals
were held by validation; this did not produce ready correction patches.**

| Entry | Observed recommendation | Independent evaluator check | Preview status |
| --- | --- | --- | --- |
| inlets | Remove from Showcase: deployed documentation uses MkDocs Material rather than Docsify | Official `inlets/docs.inlets.dev` build config and requirements establish MkDocs | Held: historical catalog lint errors |
| class-change.js | Keep | Official deployed/source HTML loads Docsify; README supports the listed capability description | No correction |
| docsify-themeable | Change IE10+ to IE11+, retaining the theme and author credit | Official current README explicitly says IE11+ | Held: historical catalog lint errors |

The protocol initially selected themeable as a keep control because it still uses
Docsify. Independent source inspection during the run found the IE11+ wording
before the model result was inspected. The original expected label was preserved,
not silently changed: this is a control-selection mistake and a supported additional
finding, not evidence of perfect control accuracy.

## Validation and costs

- All seven UM stages succeeded; total wall time **101.61 seconds**.
- Provider-reported cost **$0.7333336**, across two Opus 5.5 medium agent stages.
  This is an estimate, not an invoice or recurring-cost forecast.
- Historical baseline and both edited copies had the same **five native awesome-lint
  errors**. The workflow correctly withheld patches rather than repairing unrelated
  catalog lines. Supplemental link comparisons passed, with unrelated pre-existing
  failures reported separately.
- The unchanged current catalog at `b1db3f2b086e307f1337784ca96d1683a5098611`
  passes awesome-lint 2.3.0 (exit 0, one spelling warning). The blocking errors above
  are historical, not evidence that today's catalog fails its native check.
- Final adaptation: **25 offline tests pass**, UM 0.72.1 validates all seven stages,
  and actionlint passes both added Actions workflows.

[Generated historical report](backtests/inlets-report.md) and
[compact results](backtests/results.json) preserve the actual findings and holds.
No new model run, current-catalog audit, GitHub-hosted run or correction PR is claimed.

## Replay provenance and limits

Catalog source: `4188a1315701cbfa3d32c5cbe00ca93a04398738`. The evaluation used a
standalone checkout of that tree; its synthetic Git SHA appears in the generated
report. Project evidence was current, not reconstructed February 2025 web content.
This is one purposefully chosen case, not a blind or representative accuracy study.

The target issue/PR, outcome labels and evaluator source snapshots were outside
model inputs. The research prompt prohibited catalog history/outcome searches and
local evaluator files. Its five recorded research calls were audited and fetched
only public project sources; no target-outcome exposure was detected. This is
instruction-based isolation, not proof that leakage was impossible.

Evaluation-only code selected the three named entries, restricted collected history
to records created and last updated before `2025-02-12T00:48:07Z`, and compared
freshness with the frozen local catalog. The cutoff precedes issue #305 and can omit
legitimate older discussions updated later. The history stage found earlier additions
and related context, not the later removal. A historical preview cannot authorize
an edit to today's catalog. Production has none of these evaluation overrides and
rechecks the current upstream README.

The implementation derives from the existing inventory workflow at
`91ec0be3aecb93d17b6f18e771ea86b52022f2de`. After the live run, a narrow Markdown-label
guard was corrected to permit existing parenthesized names such as
`google-spreadsheet (npm module)`. An offline regression covers that case; applying
the final guard to the retained model assessment produces identical proposed patches.
Prompts, schema, research, history collection and validation behavior were not tuned
on the result. Raw run traces, exact source hashes, evaluator sources and the
predeclared protocol remain in the acquisition experiment.
