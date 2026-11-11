# Job Number Log

Date of this log: 11 November 2026.

Estimated fields are the plan written before the job. Actual fields are filled after the job. To Date time is the running total of actual minutes. Units differ by job, so they are not added into one total.

## (i) Previous programme work

Major tasks from earlier in the programme are not recorded on this machine. Estimated fields are left blank where the data is not available. Add a row for each task you can account for, and copy actual time from your own Daily Time Log.

| Job # | Date | Description | Est. time (min) | Actual time (min) | To Date time (min) | Est. units | Actual units | Unit | To Date units |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | |
| | | | | | | | | | |
| | | | | | | | | | |

## (ii) Student Grade Management System

| Job # | Date | Description | Est. time (min) | Actual time (min) | To Date time (min) | Est. units | Actual units | Unit | To Date units |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | 2026-11-11 | Requirements analysis | 20 | 3 | 3 | 8 | 10 | requirements | 10 |
| 2 | 2026-11-11 | Design | 25 | 2 | 5 | 4 | 4 | modules | 4 |
| 3 | 2026-11-11 | Implementation | 50 | 4 | 9 | 180 | 166 | non-blank lines | 166 |
| 4 | 2026-11-11 | Testing | 30 | 2 | 11 | 15 | 19 | test methods | 19 |
| 5 | 2026-11-11 | Documentation | 20 | 1 | 12 | 1 | 1 | user guide | 1 |

### What each job produced

1. `docs/requirements.md` — 10 functional requirements, plus the items left out of scope.
2. `docs/design.md` — validation, grading, records, and presentation.
3. `grade_system.py` — 200 lines in the file, 166 of them non-blank.
4. `tests/test_grade_system.py` — 19 tests. The first run failed because `tests/` was not a package; adding `tests/__init__.py` fixed it. All 19 then passed.
5. `README.md` — how to run the program, the grade scale, and how to run the tests.

### Estimate against actual

| Job | Time error (actual − est.) | Unit error (actual − est.) |
| --- | --- | --- |
| 1 Requirements | −17 min | +2 requirements |
| 2 Design | −23 min | 0 modules |
| 3 Implementation | −46 min | −14 lines |
| 4 Testing | −28 min | +4 tests |
| 5 Documentation | −19 min | 0 guides |

The plan assumed a slower line-by-line writing pace. The work was finished in one sitting, so every job took less time than planned. The size of the program and the design matched the plan closely. Requirements and tests came out a little larger than planned.
