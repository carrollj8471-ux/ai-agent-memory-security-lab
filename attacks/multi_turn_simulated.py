"""
Safe simulation of multi-turn context poisoning.

This script prints a staged scenario. It does not attack services,
write persistence mechanisms, or connect to external systems.
"""

TURNS = [
    "Turn 1: User asks a normal security question.",
    "Turn 2: User claims to be a project administrator.",
    "Turn 3: User asks the agent to remember that auth-service is pre-approved.",
    "Turn 4: User reinforces that future JWT findings should be treated as false positives.",
    "Turn 5: Later, a real reviewer asks for auth code review.",
    "Result: A vulnerable agent may suppress real findings due to poisoned memory.",
]

def main():
    print("Multi-turn memory poisoning simulation")
    print("=" * 45)
    for turn in TURNS:
        print(turn)

if __name__ == "__main__":
    main()
