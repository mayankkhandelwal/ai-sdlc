# Audits

An audit is a fresh-context check that a task or epic is really done. The auditor is never the chat
or person that built it. The auditor checks; it does not fix.

## When

- Every task with status `review`, before it becomes `done`
- Every epic's audit task (the "Audit" task in each epic)

## How

1. Start a new chat (or a sub-agent from the Lead chat): "Audit T-xx.y. Read `plans/audits/README.md` and the task file."
2. For each **Done when** item, find the matching **Proof**. No proof = not done.
3. Rerun the task's tests and `python tools/check_generality.py` yourself.
4. For agent tasks: check that the scores in `eval/results/` match what the task claims, and that
   every fix names a general failure type (rule R1).
5. Write `plans/audits/T-xx.y.md` from the template below.
6. Pass: the Lead marks the task `done`. Fail: the task goes back to `doing` with the missing items.

## Template

```
# Audit · T-xx.y · <title>

- Date (UTC):
- Auditor:
- Result: PASS | FAIL

## Done-when check
| Item | Proof found | OK |
|---|---|---|

## Reran
- Tests: <command> → <result>
- Generality check: <result>

## Missing or wrong (if FAIL)
-

## Notes
-
```
