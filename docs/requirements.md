# Requirements — Student Grade Management System

## Purpose

A single user enters student names and marks. The program checks those inputs, calculates each student's average and letter grade, and displays the results.

## Functional requirements

1. The user can add a student by entering a name and one or more marks.
2. The program accepts marks from 0 to 100, including decimals.
3. The program rejects an empty name, a name containing digits or symbols other than spaces, hyphens, and apostrophes, and a name longer than 40 characters.
4. The program rejects a mark that is not a number, is blank, or is outside 0 to 100, and asks again.
5. A student cannot be saved with no marks.
6. The average is the arithmetic mean of that student's marks.
7. The letter grade is A for 90–100, B for 80–89.99, C for 70–79.99, D for 60–69.99, and F below 60.
8. The results view lists every student with their marks, average (two decimal places), and letter grade.
9. The results view also shows how many students were entered and the class average of the student averages.
10. The user can leave the program from the menu.

## Out of scope

Saving data to a file, editing or deleting a student, user accounts, and weighted subjects are not part of this project. Marks exist only while the program is running.
