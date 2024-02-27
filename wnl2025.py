from random import seed, randint, choice

seed(1)

def custom_score_for_job(answer):
    score, weight = 0, 1
    if "engineer" in answer.lower():
        score, weight = randint(20, 30), 2
    elif "artist" in answer.lower():
        score, weight = randint(15, 25), 1.5
    else:
        score, weight = randint(10, 20), 1

    if "freelance" in answer.lower():
        score *= 0.9
    return score, weight

def custom_score_for_hobbies(answer):
    score, weight = 0, 1
    if "outdoor" in answer.lower():
        score, weight = randint(15, 25), 1.5
    elif "gaming" in answer.lower() or "video games" in answer.lower():
        score, weight = randint(10, 20), 1
    else:
        score, weight = randint(5, 15), 0.5

    if "reading" in answer.lower() or "chess" in answer.lower():
        score += 5
    return score, weight

def feedback_based_on_shoes(answer):
    if "sneakers" in answer.lower():
        print("Sneakers suggest a relaxed, versatile lifestyle.")
    elif "dress shoes" in answer.lower():
        print("Dress shoes hint at a preference for formality and professionalism.")

def ask_follow_up_for_tech(answer):
    score, weight = 0, 0
    if "mongodb" in answer.lower() or "congodb" in answer.lower():
        follow_up_answer = input("Do you contribute to open source? (Yes/No): ")
        if follow_up_answer.lower() in ['yes', 'y']:
            score, weight = 25, 2
    return score, weight

def stress_management_question(answer):
    if "yes" in answer.lower():
        return randint(15, 25), 2
    elif "sometimes" in answer.lower():
        return randint(5, 15), 1
    else:
        return -10, 1  

def wife_n_life_calculator():
    total_score, total_weight = 0, 0

    questions = [
        ("What's your job?: ", custom_score_for_job),
        ("What kind of shoes do you wear?: ", feedback_based_on_shoes),
        ("What do you do for fun?: ", custom_score_for_hobbies),
        ("How do you manage stress? (Yes/Sometimes/No): ", stress_management_question),
    ]

    for question, func in questions:
        answer = input(question)
        score, weight = func(answer)
        total_score += score * weight
        total_weight += weight

    final_percentage = (total_score / total_weight) * 100 if total_weight > 0 else 0
    print(f"Your Wife N Life % is: {final_percentage:.2f}% based on the provided responses.")

if __name__ == "__main__":
    wife_n_life_calculator()
