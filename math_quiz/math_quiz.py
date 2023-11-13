import random


def get_int(min, max):
    # get a random integer within bounds.
    return random.randint(min, max)


def get_operator():
    # get either '+', '-' or '*' operator
    return random.choice(['+', '-', '*'])


def calc_problem(n1, n2, operator):
    text = f"{n1} {operator} {n2}"
    if operator == '+':
        product = n1 + n2
    elif operator == '-': 
        product = n1 - n2
    elif operator == '*': 
        product = n1 * n2
    else:
        raise ValueError('Wrong operator.')
    return text, product

def math_quiz():
    s = 0
    rounds = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for round in range(rounds):
        n1 = get_int(1, 10)
        n2 = get_int(1, 5)
        operator= get_operator()

        PROBLEM, ANSWER = calc_problem(n1, n2, operator)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")
        try:
            useranswer = int(useranswer)
        except:
            raise ValueError('Your input must be an integer.')

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            s += 1
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {s}/{rounds}")

if __name__ == "__main__":
    math_quiz()
