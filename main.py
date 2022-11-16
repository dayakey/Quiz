questions = {
    "Who created Python?: ": "A",
    "What year was Python created?: ": "B",
    "Python is tributed to which comedy group?: ": "C",
    "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
           ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]


def new_game():
    questions_num = 0
    guesses = []
    correct_answers = 0

    for key in questions:
        print(key)
        print("_________________")
        for el in options[questions_num]:
            print(el)
        print("_________________")
        while True:
            guess = input("Please enter answer (A, B, C, D)").upper()
            if guess != "A" and guess != "B" and guess != "C" and guess != "D":
                print("Enter only A, B, C, D")
                print("_______________")
            else:
                break
        guesses.append(guess)
        correct_answers += check_answer(questions.get(key), guess)
        questions_num += 1

    display_score(correct_answers, len(guesses))


def check_answer(answer, guess):
    if answer == guess:
        print("CORRECT")
        return 1
    else:
        print("WRONG")
        return 0


def display_score(correct_ans, guesses):
    total = (correct_ans / guesses) * 100
    print("Your total score is", total, "%")


def play_again():
    while True:
        response = input("Do you want to play again? (YES OR NO)").upper()
        if response != "YES" and response != "NO":
            print("Enter only YES or NO")
        else:
            break
    if response == "YES":
        return True
    elif response == "NO":
        return False


def main():
    while play_again():
        new_game()
        print("Bye")


new_game()
main()
