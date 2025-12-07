def get_quest_status(progress):
    return progress["quests"]["bridge_run"]["status"]


# example usage:
from typing import TypedDict

class CharacterProgress(TypedDict):
    character_name: str
    quests: dict[str, dict[str, str]]


TestCase = tuple[CharacterProgress, str]

run_cases: list[TestCase] = [
    (
        {
            "character_name": "Sir Galahad",
            "quests": {
                "bridge_run": {
                    "status": "In Progress",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        },
        "In Progress",
    ),
    (
        {
            "character_name": "Lady Gwen",
            "quests": {
                "bridge_run": {
                    "status": "Completed",
                },
                "talk_to_syl": {
                    "status": "In Progress",
                },
            },
        },
        "Completed",
    ),
]

submit_cases: list[TestCase] = run_cases + [
    (
        {
            "character_name": "Archer Finn",
            "quests": {
                "bridge_run": {
                    "status": "Not Started",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        },
        "Not Started",
    ),
    (
        {
            "character_name": "Mage Elara",
            "quests": {
                "bridge_run": {
                    "status": "Failed",
                },
                "talk_to_syl": {
                    "status": "Completed",
                },
            },
        },
        "Failed",
    ),
    (
        {
            "character_name": "Rogue Talon",
            "quests": {
                "bridge_run": {
                    "status": "Completed",
                },
                "talk_to_syl": {
                    "status": "Not Started",
                },
            },
        },
        "Completed",
    ),
]


def test(progress: CharacterProgress, expected: str) -> bool:
    print("---------------------------------")
    print("Inputs:")
    print(f" * Progress Dictionary: {progress}")
    print(f"Expected: {expected}")
    result = get_quest_status(progress)
    print(f"Actual:   {result}")
    if result == expected:
        print("Pass")
        return True
    print("Fail")
    return False


def main() -> None:
    passed = 0
    failed = 0
    skipped = len(submit_cases) - len(test_cases)
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    if skipped > 0:
        print(f"{passed} passed, {failed} failed, {skipped} skipped")
    else:
        print(f"{passed} passed, {failed} failed")


test_cases: list[TestCase] = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()