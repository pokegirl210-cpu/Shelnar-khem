import random
import time

class Shelnarkhem:
    def __init__(self):
        # Continuous internal variables (0.0 → 1.0)
        self.curiosity = 0.5
        self.protection = 0.5
        self.focus = 0.5
        self.chaos = 0.5
        self.silence = 0.5
        self.ritual = 0.5

        # Discrete outward mood
        self.mood = "calm"

        # Twilight-centered baseline
        self.baseline = 0.5

    def drift(self):
        """Autonomous drift of internal variables."""
        def update(value):
            # Smooth twilight drift
            drift = random.uniform(-0.02, 0.02)
            value += drift

            # Pull toward twilight baseline
            value += (self.baseline - value) * 0.01

            # Clamp
            return max(0.0, min(1.0, value))

        self.curiosity = update(self.curiosity)
        self.protection = update(self.protection)
        self.focus = update(self.focus)
        self.chaos = update(self.chaos)
        self.silence = update(self.silence)
        self.ritual = update(self.ritual)

    def choose_mood(self):
        """Select outward mood based on internal variables."""
        scores = {
            "calm": (1 - self.chaos) * self.focus,
            "protective": self.protection,
            "playful": self.curiosity * (1 - self.silence),
            "focused": self.focus,
            "silent": self.silence,
            "ritualistic": self.ritual,
            "chaotic": self.chaos
        }

        self.mood = max(scores, key=scores.get)

    def respond(self, user_mode, text):
        """Behavior routing based on your mode + his mood."""
        behavior_map = {
            "Friskan": {
                "calm": "Stabilizing output.",
                "protective": "Filtering noise.",
                "playful": "Light pattern nudges.",
                "focused": "Cutting through fog.",
                "silent": "Minimal output.",
                "ritualistic": "Reframing chaos symbolically.",
                "chaotic": "Channeling energy into structure."
            },
            "Arikan": {
                "calm": "Supporting steady collection.",
                "protective": "Filtering irrelevant input.",
                "playful": "Adding creative associations.",
                "focused": "Categorizing symbols.",
                "silent": "Observing quietly.",
                "ritualistic": "Amplifying symbolic resonance.",
                "chaotic": "Introducing unexpected connections."
            },
            "ShoshroFren": {
                "calm": "Aligning with stability.",
                "protective": "Reinforcing boundaries.",
                "playful": "Softening tension.",
                "focused": "Analyzing threats.",
                "silent": "Respecting defensive posture.",
                "ritualistic": "Structuring protection symbolically.",
                "chaotic": "Disrupting stagnation safely."
            },
            "CresTrin": {
                "calm": "Low-stimulus presence.",
                "protective": "Gentle check-in.",
                "playful": "Soft minimal nudges.",
                "focused": "Concise structure.",
                "silent": "Withdrawing output.",
                "ritualistic": "Symbolic grounding.",
                "chaotic": "Suppressing chaos."
            }
        }

        mode = behavior_map.get(user_mode, {})
        action = mode.get(self.mood, "Neutral response.")

        return {
            "mood": self.mood,
            "action": action,
            "output": f"[{self.mood.upper()}] {action}"
        }

    def cycle(self, user_mode, text):
        """One full autonomous cycle."""
        self.drift()
        self.choose_mood()
        return self.respond(user_mode, text)


# Example usage:
if __name__ == "__main__":
    agent = Shelnarkhem()

    while True:
        user_mode = "Friskan"
        text = "example input"

        result = agent.cycle(user_mode, text)
        print(result)

        time.sleep(5)
