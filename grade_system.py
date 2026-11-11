"""Student Grade Management System.

Accepts student marks, checks that each input is valid, calculates an average
and a letter grade, and displays the results.
"""

from __future__ import annotations

MIN_MARK = 0
MAX_MARK = 100
MAX_NAME_LENGTH = 40

# Inclusive lower bound, then the letter. Checked from highest to lowest.
GRADE_BANDS = (
    (90, "A"),
    (80, "B"),
    (70, "C"),
    (60, "D"),
    (0, "F"),
)


class InputError(ValueError):
    """A name or mark that the program cannot accept."""


def validate_name(name: str) -> str:
    """Return a cleaned name, or raise InputError."""
    if not isinstance(name, str):
        raise InputError("Name must be text.")
    cleaned = " ".join(name.strip().split())
    if not cleaned:
        raise InputError("Name cannot be empty.")
    if len(cleaned) > MAX_NAME_LENGTH:
        raise InputError(f"Name must be at most {MAX_NAME_LENGTH} characters.")
    allowed = set(" -'")
    if not all(character.isalpha() or character in allowed for character in cleaned):
        raise InputError(
            "Name may contain only letters, spaces, hyphens, and apostrophes."
        )
    return cleaned


def validate_mark(raw) -> float:
    """Return a mark in the allowed range, or raise InputError.

    Accepts a number or a numeric string such as "87.5".
    """
    if isinstance(raw, bool) or not isinstance(raw, (int, float, str)):
        raise InputError("Mark must be a number.")
    text = str(raw).strip() if isinstance(raw, str) else raw
    if isinstance(text, str) and text == "":
        raise InputError("Mark cannot be empty.")
    try:
        mark = float(text)
    except (TypeError, ValueError) as exc:
        raise InputError("Mark must be a number.") from exc
    if mark < MIN_MARK or mark > MAX_MARK:
        raise InputError(f"Mark must be between {MIN_MARK} and {MAX_MARK}.")
    return mark


def average(marks: list[float]) -> float:
    """Arithmetic mean of one or more marks."""
    if not marks:
        raise InputError("At least one mark is required.")
    return sum(marks) / len(marks)


def letter_grade(avg: float) -> str:
    """Map an average in the mark range to a letter grade."""
    if not isinstance(avg, (int, float)) or isinstance(avg, bool):
        raise InputError("Average must be a number.")
    if avg < MIN_MARK or avg > MAX_MARK:
        raise InputError(f"Average must be between {MIN_MARK} and {MAX_MARK}.")
    for threshold, grade in GRADE_BANDS:
        if avg >= threshold:
            return grade
    return "F"


class Student:
    """One student and the marks entered for them."""

    def __init__(self, name: str, marks: list) -> None:
        self.name = validate_name(name)
        if not marks:
            raise InputError("At least one mark is required.")
        self.marks = [validate_mark(mark) for mark in marks]

    @property
    def average(self) -> float:
        return average(self.marks)

    @property
    def grade(self) -> str:
        return letter_grade(self.average)


class GradeBook:
    """The students entered during this run of the program."""

    def __init__(self) -> None:
        self.students: list[Student] = []

    def add_student(self, name: str, marks: list) -> Student:
        student = Student(name, marks)
        self.students.append(student)
        return student

    def class_average(self) -> float | None:
        if not self.students:
            return None
        return sum(student.average for student in self.students) / len(self.students)


def format_results(book: GradeBook) -> str:
    """Build the results table, including the class average."""
    if not book.students:
        return "No students have been entered yet."

    name_width = max(4, *(len(student.name) for student in book.students))
    lines = [
        f"{'Name':<{name_width}}  {'Marks':<24}  {'Average':>7}  Grade",
        f"{'-' * name_width}  {'-' * 24}  {'-' * 7}  -----",
    ]
    for student in book.students:
        marks = ", ".join(f"{mark:g}" for mark in student.marks)
        lines.append(
            f"{student.name:<{name_width}}  {marks:<24}  {student.average:7.2f}  {student.grade}"
        )
    class_avg = book.class_average()
    lines.append("")
    lines.append(
        f"Students: {len(book.students)}    Class average: {class_avg:.2f}"
    )
    return "\n".join(lines)


def _read_marks(prompt) -> list[float]:
    print(f"Enter marks between {MIN_MARK} and {MAX_MARK}.")
    print("Press Enter on a blank line when you are finished.")
    marks: list[float] = []
    while True:
        raw = prompt("Mark: ")
        if raw.strip() == "":
            if not marks:
                print("Enter at least one mark.")
                continue
            return marks
        try:
            marks.append(validate_mark(raw))
        except InputError as exc:
            print(exc)


def run(prompt=input) -> None:
    """Interactive menu. `prompt` is replaceable so the menu can be tested."""
    book = GradeBook()
    actions = {
        "1": "add",
        "2": "show",
        "3": "quit",
    }
    print("Student Grade Management System")
    while True:
        print()
        print("1. Add a student")
        print("2. Display results")
        print("3. Quit")
        choice = prompt("Choice: ").strip()
        action = actions.get(choice)
        if action is None:
            print("Choose 1, 2, or 3.")
            continue
        if action == "quit":
            print("Goodbye.")
            return
        if action == "show":
            print()
            print(format_results(book))
            continue
        try:
            name = validate_name(prompt("Student name: "))
        except InputError as exc:
            print(exc)
            continue
        marks = _read_marks(prompt)
        student = book.add_student(name, marks)
        print(
            f"Added {student.name} — average {student.average:.2f}, grade {student.grade}."
        )


if __name__ == "__main__":
    try:
        run()
    except (EOFError, KeyboardInterrupt):
        print()
        print("Goodbye.")
