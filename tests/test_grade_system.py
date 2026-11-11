"""Tests for mark validation, averages, letter grades, and the results table."""

import unittest
from io import StringIO
from unittest.mock import patch

from grade_system import (
    GRADE_BANDS,
    GradeBook,
    InputError,
    Student,
    average,
    format_results,
    letter_grade,
    run,
    validate_mark,
    validate_name,
)


class ValidateNameTests(unittest.TestCase):
    def test_strips_and_collapses_spaces(self):
        self.assertEqual(validate_name("  ada   lovelace  "), "ada lovelace")

    def test_allows_hyphen_and_apostrophe(self):
        self.assertEqual(validate_name("Mary-Jane O'Neil"), "Mary-Jane O'Neil")

    def test_rejects_empty_name(self):
        with self.assertRaises(InputError):
            validate_name("   ")

    def test_rejects_digits(self):
        with self.assertRaises(InputError):
            validate_name("Student 1")

    def test_rejects_overlong_name(self):
        with self.assertRaises(InputError):
            validate_name("A" * 41)


class ValidateMarkTests(unittest.TestCase):
    def test_accepts_bounds(self):
        self.assertEqual(validate_mark(0), 0)
        self.assertEqual(validate_mark("100"), 100)
        self.assertEqual(validate_mark(" 87.5 "), 87.5)

    def test_rejects_out_of_range(self):
        with self.assertRaises(InputError):
            validate_mark(-0.1)
        with self.assertRaises(InputError):
            validate_mark(100.1)

    def test_rejects_text_and_blank(self):
        with self.assertRaises(InputError):
            validate_mark("eighty")
        with self.assertRaises(InputError):
            validate_mark("  ")

    def test_rejects_boolean(self):
        with self.assertRaises(InputError):
            validate_mark(True)


class GradingTests(unittest.TestCase):
    def test_average(self):
        self.assertEqual(average([90, 80, 70]), 80)

    def test_average_requires_a_mark(self):
        with self.assertRaises(InputError):
            average([])

    def test_letter_boundaries(self):
        self.assertEqual(letter_grade(100), "A")
        self.assertEqual(letter_grade(90), "A")
        self.assertEqual(letter_grade(89.99), "B")
        self.assertEqual(letter_grade(80), "B")
        self.assertEqual(letter_grade(70), "C")
        self.assertEqual(letter_grade(60), "D")
        self.assertEqual(letter_grade(59.99), "F")
        self.assertEqual(letter_grade(0), "F")

    def test_bands_cover_the_full_range(self):
        self.assertEqual(GRADE_BANDS[-1][0], 0)


class GradeBookTests(unittest.TestCase):
    def test_student_average_and_grade(self):
        student = Student("Ada Lovelace", [91, 87, 95])
        self.assertAlmostEqual(student.average, 91)
        self.assertEqual(student.grade, "A")

    def test_student_requires_a_mark(self):
        with self.assertRaises(InputError):
            Student("Ada Lovelace", [])

    def test_class_average(self):
        book = GradeBook()
        self.assertIsNone(book.class_average())
        book.add_student("Ada", [90, 90])
        book.add_student("Grace", [70, 80])
        self.assertAlmostEqual(book.class_average(), 82.5)

    def test_results_table(self):
        book = GradeBook()
        book.add_student("Ada", [90, 80])
        text = format_results(book)
        self.assertIn("Ada", text)
        self.assertIn("85.00", text)
        self.assertIn("B", text)
        self.assertIn("Class average: 85.00", text)

    def test_empty_results(self):
        self.assertIn("No students", format_results(GradeBook()))


class MenuTests(unittest.TestCase):
    def test_add_then_display_then_quit(self):
        answers = iter(
            [
                "1",
                "  Grace Hopper ",
                "70",
                "80",
                "not a mark",
                "90",
                "",
                "2",
                "9",
                "3",
            ]
        )
        with patch("sys.stdout", new_callable=StringIO) as output:
            run(prompt=lambda _label: next(answers))
        text = output.getvalue()
        self.assertIn("Mark must be a number.", text)
        self.assertIn("Added Grace Hopper — average 80.00, grade B.", text)
        self.assertIn("Class average: 80.00", text)
        self.assertIn("Choose 1, 2, or 3.", text)
        self.assertIn("Goodbye.", text)


if __name__ == "__main__":
    unittest.main()
