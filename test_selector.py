from assistant.skill_selector import SkillSelector

selector = SkillSelector()

while True:

    text = input("> ")

    print(selector.choose(text))