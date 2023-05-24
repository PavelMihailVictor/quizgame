


class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.current_question_index = 0

    def add_question(self, question):
        self.questions.append(question)

    def display_question(self):
        question = self.questions[self.current_question_index]
        print(f"Question {self.current_question_index + 1}: {question.text}")
        for index, choice in enumerate(question.choices):
            print(f"{index + 1}. {choice}")

    def get_user_choice(self):
        while True:
            try:
                user_choice = int(input("Enter your choice (1-4): "))
                if 1 <= user_choice <= 4:
                    return user_choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def play(self):
        for question in self.questions:
            self.display_question()
            user_choice = self.get_user_choice()
            if question.check_answer(user_choice):
                print("Correct answer!")
                self.score += 1
            else:
                print("Wrong answer!")
            self.current_question_index += 1
            print()

    def display_score(self):
        total_questions = len(self.questions)
        percentage = (self.score / total_questions) * 100
        print(f"Your score: {self.score}/{total_questions} ({percentage:.2f}%)")

def main():
    quiz = Quiz()

    question1 = Question("What is the capital of France?", ["London", "Paris", "Berlin", "Rome"], "2")
    question2 = Question("Who painted the Mona Lisa?", ["Leonardo da Vinci", "Pablo Picasso", "Vincent van Gogh", "Michelangelo"], "1")
    question3 = Question("Which planet is known as the Red Planet?", ["Mars", "Venus", "Jupiter", "Saturn"], "1")

    quiz.add_question(question1)
    quiz.add_question(question2)
    quiz.add_question(question3)

    quiz.play()
    quiz.display_score()

if __name__ == "__main__":
    main()
