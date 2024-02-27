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
        score *= 0.8  # Freelancers get a slight reduction due to perceived instability
    return score, weight

def calculate_base_score(answers):
    base_score = sum([randint(5, 15) for _ in answers])  # Simple base score from initial answers
    compatibility_score = randint(10, 30)  # Simulate compatibility calculation
    life_goals_alignment = randint(5, 20)  # Simulate alignment with life goals
    social_skills_evaluation = randint(-5, 15)  # Simulate social skills evaluation
    stress_management = randint(-10, 10)  # Simulate stress management capability
    return base_score + compatibility_score + life_goals_alignment + social_skills_evaluation + stress_management

def simulate_random_events():
    events = [
        ("Found a $50 bill on the sidewalk!", 25),
        ("Got a flat tire on the way to an important meeting.", -20),
        ("Received a surprise promotion at work!", 30),
        ("Misunderstanding with a close friend led to an argument.", -15)
    ]
    event_choice = choice(events)
    print(f"Random event: {event_choice[0]}")
    return event_choice[1]

def consider_external_factors():
    factors = randint(-10, 20)  
    return factors

def ask_questions():
    questions = [
        "What's your favorite way to spend a weekend?",
        "What traits do you value most in a partner?",
        "How important is career success to you?",
        "How do you handle disagreements or conflicts?"
    ]
    answers = [input(f"{q}\n") for q in questions]
    return answers

def calculate_wife_n_life_percentage():
    answers = ask_questions()
    base_score = calculate_base_score(answers)
    random_event_impact = simulate_random_events()
    external_factors_impact = consider_external_factors()
    total_score = base_score + random_event_impact + external_factors_impact
    # Normalize score to a percentage
    normalized_score = (total_score / (100 + 50 + 30 + 20)) * 100  
    return max(0, min(normalized_score, 100))  


def custom_score_for_hobbies(answer):
    score, weight = 0, 1
    if "outdoor" in answer.lower():
        score, weight = randint(15, 25), 1.5
    elif "video games" in answer.lower():
        score, weight = randint(10, 20), 1
    else:
        score, weight = randint(5, 15), 0.5
    if "reading" in answer.lower():
        score += 5  
    return score, weight

def dynamic_question_path(answer):
    if "yes" in answer.lower() or "y" in answer.lower():
        follow_up_question = "How often do you plan dates or outings? (Often/Sometimes/Rarely/Never):"
        follow_up_answer = input(follow_up_question).lower()
        if follow_up_answer in ["often", "sometimes"]:
            return 20, 2 
        else:
            return -10, 1 
    return 0, 0

def random_event():
    events = [("Found a $20 bill on the ground!", 20), ("Missed the bus and got late.", -10)]
    event_choice = choice(events)
    print(f"Random event: {event_choice[0]}")
    return event_choice[1], 1

questions = [
    ("What's your job?:", custom_score_for_job),
    ("What kind of shoes do you wear?:", None, feedback_based_on_shoes),
    ("What do you do for fun?:", custom_score_for_hobbies),
    ("Are you open to trying new things with your partner? (Yes/No):", dynamic_question_path),
]

total_score, total_weight = 0, 0

for question, scoring_function in questions:
    answer = input(question)
    score, weight = scoring_function(answer) if scoring_function else (0, 0)
    total_score += score * weight
    total_weight += weight

event_score, event_weight = random_event()
total_score += event_score * event_weight
total_weight += event_weight

percentage = (total_score / total_weight) * 100 if total_weight > 0 else 0

print(f"Your Wife N Life % is: {percentage:.2f}%")
