# PROJECT REPORT

## Online Quiz Game

### 1. Introduction

The Online Quiz Game is a command-line based application developed using Python.
The project allows users to answer multiple-choice questions and calculates their
score and percentage at the end of the quiz.

### 2. Objectives

The main objectives of this project are:

- To develop a simple quiz application using Python.
- To practice Python functions and loops.
- To use lists and dictionaries for storing questions.
- To implement user input and validation.
- To calculate the final score and percentage.
- To create a program that can be executed from the command line.

### 3. Technologies Used

- Programming Language: Python
- IDE: Visual Studio Code
- Interface: Command Line / Terminal

### 4. Features

- Main menu
- Start Quiz option
- Instructions option
- Exit option
- 10 multiple-choice questions
- Input validation
- Instant feedback
- Score calculation
- Percentage calculation
- Play again option

### 5. Working of the Project

The program first displays the main menu.

The user can select:

1. Start Quiz
2. Instructions
3. Exit

When the user starts the quiz, questions are displayed one by one.
Each question has four options: A, B, C and D.

The user's answer is compared with the correct answer stored in the
program. If the answer is correct, one mark is added to the score.

After all questions are completed, the program calculates the percentage
using the score and total number of questions.

### 6. Python Concepts Used

The following Python concepts are used:

- Functions
- Lists
- Dictionaries
- For loops
- While loops
- Conditional statements
- User input
- String methods
- Arithmetic operations

### 7. Algorithm

1. Start the program.
2. Display the main menu.
3. Ask the user to select an option.
4. If Start Quiz is selected, display the questions.
5. Take the user's answer.
6. Validate the input.
7. Compare the answer with the correct answer.
8. Increase the score if the answer is correct.
9. Repeat until all questions are completed.
10. Calculate the percentage.
11. Display the final result.
12. Ask whether the user wants to play again.
13. Exit the program.

### 8. Testing

The program was tested through the command line.

Test cases included:

- Starting the quiz.
- Selecting the instructions.
- Selecting the exit option.
- Entering correct answers.
- Entering incorrect answers.
- Entering invalid answers.
- Calculating the final score.
- Calculating the percentage.
- Playing the quiz again.

### 9. Sample Output

```text
===== ONLINE QUIZ GAME =====

1. Start Quiz
2. Instructions
3. Exit

Enter your choice: 1

Question 1:
Which language is commonly used for Artificial Intelligence?

A. Python
B. HTML
C. CSS
D. SQL

Your answer: A
Correct!

===== QUIZ RESULT =====

Score: 8/10
Percentage: 80.0%
Excellent performance!