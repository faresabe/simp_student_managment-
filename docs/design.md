# Design — Student Grade Management System

## Modules

All of the program lives in `grade_system.py`. The pieces are separate so each can be tested without the menu.

| Piece | Responsibility |
| --- | --- |
| Validation | `validate_name`, `validate_mark` |
| Grading | `average`, `letter_grade` |
| Records | `Student`, `GradeBook` |
| Presentation | `format_results`, `run` |

`InputError` is the only error type the menu catches. Invalid input prints the message and lets the user try again. It does not stop the program.

## Data

A `Student` stores a cleaned name and a list of marks. Average and letter grade are calculated when needed, not stored.

A `GradeBook` stores students in the order they were added. The class average is the mean of the student averages. An empty book has no class average.

## Grade scale

| Average | Grade |
| --- | --- |
| 90–100 | A |
| 80 up to 90 | B |
| 70 up to 80 | C |
| 60 up to 70 | D |
| 0 up to 60 | F |

The boundary belongs to the higher grade: 90 is an A, 89.99 is a B.

## Menu

```
1 Add a student
    name -> validate
    marks until a blank line -> validate each mark
    save and show that student's average and grade
2 Display results
    table, or a message when the book is empty
3 Quit
```

Anything other than 1, 2, or 3 prints a short prompt and shows the menu again.
