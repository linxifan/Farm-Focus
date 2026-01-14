import random

def get_mood():
    return random.choice(["happy", "neutral", "sad"])

def mood_reward(mood):
    if mood == "happy":
        return "flower"
    return None