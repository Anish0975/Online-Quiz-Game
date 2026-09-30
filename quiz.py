def show_instructions():
    print("\n===== INSTRUCTIONS =====")
    print("1. The quiz contains 10 questions.")
    print("2. Each question has four options: A, B, C, and D.")
    print("3. Enter only A, B, C, or D.")
    print("4. Each correct answer gives 1 mark.")
    print("5. There is no negative marking.")


def start_quiz():
    questions = [
        {
            "question": "Which language is commonly used for Artificial Intelligence?",
            "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
            "answer": "A"
        },
        {
            "question": "What is the correct extension of a Python file?",
            "options": [ "A. .java", "B. .py", "C. .cpp", "D. .html"],
            "answer": "B"
        },
        {
            "question": "Which keyword is used to define a function in Python?",
            "options": ["A. function", "B. define", "C. def", "D. fun"],
            "answer": "C"
        },
        {
            "question": "Which data type stores True or False?",
            "options": ["A. int", "B. str", "C. float", "D. bool"],
            "answer": "D"
        },
        {
            "question": "Which symbol is used to start a comment in Python?",
            "options": ["A. //", "B. #", "C. /*", "D. --"],
            "answer": "B"
        },
        {
            "question": "Which function is used to display output in Python?",
            "options": ["A. input()", "B. display()", "C. print()", "D. output()"],
            "answer": "C"
        },
        {
            "question": "What is the symbol of addition in Python?",
            "options": ["A. +", "B. -", "C. *", "D. /"],
            "answer": "A"
        },
        {
            "question": "Which keyword is used for a loop over a sequence?",
            "options": ["A. repeat", "B. for", "C. loop", "D. iterate"],
            "answer": "B"
        },
        {
            "question": "Which data type stores multiple values in an ordered collection?",
            "options": ["A. list", "B. int", "C. bool", "D. float"],
            "answer": "A"
        },
        {
            "question": "Which operator is used for exponentiation in Python?",
            "options": ["A. ^", "B. //", "C. **", "D. %%"],
            "answer": "C"
        }
    ]

    score = 0

    print("\n===== ONLINE QUIZ GAME =====")

    for number, question in enumerate(questions, 1):
        print(f"\nQuestion {number}: {question['question']}")

        for option in question["options"]:
            print(option)

        while True:
            user_answer = input("Your answer: ").upper()

            if user_answer in ["A", "B", "C", "D"]:
                break

            print("Invalid input! Please enter A, B, C, or D.")

        if user_answer == question["answer"]:
            print("Correct! ✓")
            score += 1
        else:
            print("Wrong!")
            print("Correct answer:", question["answer"])

    percentage = (score / len(questions)) * 100

    print("\n===== QUIZ RESULT =====")
    print(f"Score: {score}/{len(questions)}")
    print(f"Percentage: {percentage:.1f}%")

    if percentage >= 80:
        print("Excellent performance!")
    elif percentage >= 50:
        print("Good job!")
    else:
        print("Keep practicing!")


def main():
    while True:
        print("\n==============================")
        print("       ONLINE QUIZ GAME")
        print("==============================")
        print("1. Start Quiz")
        print("2. Instructions")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_quiz()

            again = input("\nDo you want to play again? (Y/N): ").upper()

            if again != "Y":
                print("Thank you for playing!")
                break

        elif choice == "2":
            show_instructions()

        elif choice == "3":
            print("Thank you for playing!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


main()