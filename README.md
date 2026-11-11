# Student Grade Management System

A small console program that stores student marks for the current session, checks each input, and shows averages and letter grades.

## Run

```bash
python3 grade_system.py
```

## Menu

1. Add a student. Enter the name, then one or more marks from 0 to 100. Press Enter on a blank line to finish that student.
2. Display every student, their average, their letter grade, and the class average.
3. Quit.

## Letter grades

| Average | Grade |
| --- | --- |
| 90–100 | A |
| 80–89 | B |
| 70–79 | C |
| 60–69 | D |
| Below 60 | F |

A mark on a boundary takes the higher grade. 90 is an A.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Project records

- [Requirements](docs/requirements.md)
- [Design](docs/design.md)
- [Job Number Log](logs/job_number_log.md)
- [Daily Time Log](logs/daily_time_log.md)
