import math
import random
import datetime


def generate_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)

    op = random.choice(["+", "*", "-", "**"])
    # op = random.randint(1,4)

    if op == "+":
        question = f"{num1} + {num2} ="
        answer = num1 + num2
    elif op == "-":
        question = f"{num1} - {num2} ="
        answer = num1 - num2
    elif op == "*":
        question = f"{num1} * {num2} ="
        answer = num1 * num2
    elif op == "**":
        question = f"{num1} ** {num2} ="
        answer = int(math.pow(num1,num2))
    return question , answer

def quiz():
    print("Welcome to math quiz game")
    num_questions = 5
    score = 0
    start_time = datetime.datetime.now()
    for i in range(1,num_questions+1):
        questin, answer= generate_question()
        print(f"\nQuestion {i}: {questin}") 
        
        user_answer = int(input("Your answer:"))
        if user_answer == answer:
            print("Correct!!")
            score+=1
        else:
            print(f"!!Wrong! The correct answer is {answer}")
    end_time = datetime.datetime.now()
    time_taken = end_time - start_time
    print("\n---------Quiz Completed--------")
    print(f"Your Score: {score}/{num_questions}")
    print(f"Time taken: {time_taken.seconds}sec")
    print("Hope you enjoyed. Thanks for playing!!")


quiz()
    