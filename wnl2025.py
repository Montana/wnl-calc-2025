from random import seed, randint, choice

seed(1) 

def custom_score_for_job(answer):
    if "engineer" in answer.lower():
        return randint(20, 30), 2  
    elif "artist" in answer.lower():
        return randint(15, 25), 1.5  
    else:
        return randint(10, 20), 1  

def custom_score_for_hobbies(answer):
    if "outdoor" in answer.lower():
        return randint(15, 25), 1.5  
    elif "video games" in answer.lower():
        return randint(10, 20), 1  
    else:
        return randint(5, 15), 0.5  

def feedback_based_on_shoes(answer):
    if "sneakers" in answer.lower():
        print("Cool choice! Sneakers can say a lot about a person.")
    elif "dress shoes" in answer.lower():
        print("Classy! You seem to mean business.")

def ask_follow_up_for_tech(answer):
    if "mongodb" in answer.lower() or "congodb" in answer.lower():
        follow_up_answer = input("Do you contribute to open source? (Yes/No): ")
        if follow_up_answer.lower() in ['yes', 'y']:
            return 25, 2  
    return 0, 0

def negative_modifier_based_on_clothing(answer):
    if "cargo shorts" in answer.lower():
        print("Interesting choice... that's brave!")
        return -10  
    return 0

def evaluate_stress(answer):
    stress_levels = {
        'high': (-20, 2),
        'medium': (-10, 1),
        'low': (0, 0)
    }
    return stress_levels.get(answer.lower(), (0, 0))

def bonus_round():
    bonus_question = "Do you enjoy cooking? (Yes/No):"
    answer = input(bonus_question).lower()
    if answer in ['yes', 'y']:
        return randint(10, 20), 2  
    return 0, 0

questions = [

    ("How do you handle stress? (High/Medium/Low):", evaluate_stress),
    ("What's your job?:", custom_score_for_job),
    ("What kind of shoes do you wear?:", None, feedback_based_on_shoes),
    ("What do you do for fun?:", custom_score_for_hobbies),
]

total_score = 0
total_weight = 0

for question, scoring_function, *optional in questions:
    answer = input(question)
    if optional:
        feedback_function = optional[0]
        if feedback_function:
            feedback_function(answer)
    if scoring_function:
        score, weight = scoring_function(answer)
        total_score += score * weight
        total_weight += weight

tech_answer = input("Do you use MongoDB? CongoDB?")
tech_score, tech_weight = ask_follow_up_for_tech(tech_answer)
total_score += tech_score * tech_weight
total_weight += tech_weight

negative_modifier = negative_modifier_based_on_clothing(tech_answer)
total_score += negative_modifier

if total_score / total_weight > 50:  
    bonus_score, bonus_weight = bonus_round()
    total_score += bonus_score * bonus_weight
    total_weight += bonus_weight

percentage = (total_score / total_weight) if total_weight > 0 else 0

print(f"Your Wife N Life % is: {percentage:.2f}%")
