from random import seed, randint, choice
seed(1)
print("""
                  _   _                 _                 _                          _       
                | | | |               | |               | |                        | |      
 __      ___ __ | | | |__  _   _   ___| |_ ___  __ _  __| |_ __ ___   ___ _ __   __| |_   _ 
 \ \ /\ / / '_ \| | | '_ \| | | | / __| __/ _ \/ _` |/ _` | '_ ` _ \ / _ \ '_ \ / _` | | | |
  \ V  V /| | | | | | |_) | |_| | \__ \ ||  __/ (_| | (_| | | | | | |  __/ | | | (_| | |_| |
   \_/\_/ |_| |_|_| |_.__/ \__, | |___/\__\___|\__,_|\__,_|_| |_| |_|\___|_| |_|\__,_|\__, |
                            __/ |                                                      __/ |
                           |___/                                                      |___/ 
""")
def custom_score_for_job(answer):
    if "engineer" in answer.lower():
        return randint(20, 30), 2
    elif "artist" in answer.lower():
        return randint(15, 25), 1.5
    elif "doctor" in answer.lower():
        return randint(25, 35), 2.5
    elif "teacher" in answer.lower():
        return randint(18, 28), 1.8
    else:
        return randint(10, 20), 1
def custom_score_for_hobbies(answer):
    if "outdoor" in answer.lower():
        return randint(15, 25), 1.5
    elif "video games" in answer.lower():
        return randint(10, 20), 1
    elif "reading" in answer.lower():
        return randint(18, 28), 1.8
    elif "sports" in answer.lower():
        return randint(20, 30), 2
    else:
        return randint(5, 15), 0.5
def feedback_based_on_shoes(answer):
    if "sneakers" in answer.lower():
        print("Cool choice! Sneakers can say a lot about a person.")
    elif "dress shoes" in answer.lower():
        print("Classy! You seem to mean business.")
    elif "sandals" in answer.lower():
        print("Laid-back and ready for summer!")
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
    elif "socks with sandals" in answer.lower():
        print("Bold fashion statement!")
        return -15
    return 0
def evaluate_stress(answer):
    stress_levels = {
        'high': (-20, 2),
        'medium': (-10, 1),
        'low': (0, 0),
        'none': (10, 1)
    }
    return stress_levels.get(answer.lower(), (0, 0))
def bonus_round():
    bonus_question = "Do you enjoy cooking? (Yes/No):"
    answer = input(bonus_question).lower()
    if answer in ['yes', 'y']:
        return randint(10, 20), 2
    return 0, 0
def evaluate_communication_skills(answer):
    if "excellent" in answer.lower():
        return randint(25, 35), 2.5
    elif "good" in answer.lower():
        return randint(15, 25), 1.5
    elif "average" in answer.lower():
        return randint(5, 15), 1
    else:
        return randint(0, 10), 0.5
def evaluate_financial_responsibility(answer):
    if "very responsible" in answer.lower():
        return randint(30, 40), 3
    elif "somewhat responsible" in answer.lower():
        return randint(15, 25), 2
    elif "working on it" in answer.lower():
        return randint(5, 15), 1
    else:
        return randint(-10, 0), 1
def evaluate_pet_ownership(answer):
    if "dog" in answer.lower():
        print("Dogs are great companions!")
        return randint(20, 30), 2
    elif "cat" in answer.lower():
        print("Cats add a chill vibe.")
        return randint(15, 25), 1.5
    elif "none" in answer.lower():
        return randint(0, 10), 0.5
    else:
        print("Unique pet choice!")
        return randint(10, 20), 1
def evaluate_social_life(answer):
    if "lots" in answer.lower() or "many" in answer.lower():
        return randint(20, 30), 2
    elif "few" in answer.lower():
        return randint(10, 20), 1
    elif "none" in answer.lower() or "solo" in answer.lower():
        return randint(0, 10), 0.5
    else:
        return randint(5, 15), 1
def evaluate_travel_experience(answer):
    if "often" in answer.lower():
        return randint(25, 35), 2.5
    elif "sometimes" in answer.lower():
        return randint(15, 25), 1.5
    elif "rarely" in answer.lower():
        return randint(5, 15), 1
    else:
        return randint(0, 10), 0.5
def evaluateinte_fitness_level(answer):
    if "very" in answer.lower():
        return randint(25, 35), 2
    elif "somewhat" in answer.lower():
        return randint(15, 25), 1.5
    elif "not" in answer.lower():
        return randint(0, 10), 0.5
    else:
        return randint(5, 15), 1
def evaluate_family_relationships(answer):
    if "great" in answer.lower():
        return randint(20, 30), 2
    elif "okay" in answer.lower():
        return randint(10, 20), 1
    elif "bad" in answer.lower():
        return randint(-10, 0), 1
    else:
        return randint(0, 10), 0.5
def evaluate_housing_situation(answer):
    if "own" in answer.lower():
        return randint(30, 40), 3
    elif "rent" in answer.lower():
        return randint(15, 25), 2
    elif "parents" in answer.lower() or "family" in answer.lower():
        return randint(5, 15), 1
    else:
        return randint(0, 10), 0.5
def evaluate_cooking_skills(answer):
    if "great" in answer.lower():
        return randint(20, 30), 2
    elif "decent" in answer.lower():
        return randint(10, 20), 1.5
    elif "bad" in answer.lower():
        return randint(0, 10), 0.5
    else:
        return randint(5, 15), 1
def negative_modifier_based_on_habits(answer):
    if "smoking" in answer.lower():
        print("Might want to kick that habit!")
        return -15
    elif "procrastinate" in answer.lower():
        print("Getting things done on time could help!")
        return -10
    return 0
questions = [
    ("How do you handle stress? (High/Medium/Low/None):", evaluate_stress),
    ("What's your job?:", custom_score_for_job),
    ("What kind of shoes do you wear?:", None, feedback_based_on_shoes),
    ("What do you do for fun?:", custom_score_for_hobbies),
    ("How would you rate your communication skills? (Excellent/Good/Average/Poor):", evaluate_communication_skills),
    ("How would you describe your financial responsibility? (Very responsible/Somewhat responsible/Working on it/Not great):", evaluate_financial_responsibility),
    ("Do you have any pets? (Dog/Cat/None/Other):", evaluate_pet_ownership),
    ("How many close friends do you have? (Lots/Few/None):", evaluate_social_life),
    ("How often do you travel? (Often/Sometimes/Rarely/Never):", evaluate_travel_experience),
    ("How fit are you? (Very/Somewhat/Not really):", evaluate_fitness_level),
    ("How’s your relationship with your family? (Great/Okay/Bad):", evaluate_family_relationships),
    ("What’s your housing situation? (Own/Rent/Live with parents):", evaluate_housing_situation),
    ("How good are you at cooking? (Great/Decent/Bad):", evaluate_cooking_skills),
    ("Any bad habits? (e.g., smoking, procrastinating):", negative_modifier_based_on_habits),
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
        result = scoring_function(answer)
        if isinstance(result, tuple):  
            score, weight = result
            total_score += score * weight
            total_weight += weight
        else:  
            total_score += result
tech_answer = input("Do you use MongoDB or CongoDB? ")
tech_score, tech_weight = ask_follow_up_for_tech(tech_answer)
total_score += tech_score * tech_weight
total_weight += tech_weight
negative_modifier = negative_modifier_based_on_clothing(tech_answer)
total_score += negative_modifier
if total_score / total_weight > 60:  
    bonus_score, bonus_weight = bonus_round()
    total_score += bonus_score * bonus_weight
    total_weight += bonus_weight
percentage = (total_score / total_weight) if total_weight > 0 else 0
print(f"Your Wife N Life % is: {percentage:.2f}%")
if percentage > 75:
    print("Wow, you’re living the dream!")
elif percentage > 50:
    print("Solid life! You’re doing pretty well.")
elif percentage > 25:
    print("Room to grow, but you’ve got potential!")
else:
    print("Time to level up some skills!")
