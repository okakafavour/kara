from app.brain.rule_parser import RuleParser

parser = RuleParser()

commands = [
    "what's my battery percentage",
    "battery level",
    "cpu usage",
    "how much ram am i using",
    "disk space",
]

print("=" * 40)
print("Testing System Parser")
print("=" * 40)

for command in commands:

    print("\nCommand:")
    print(command)

    print(parser.parse(command))