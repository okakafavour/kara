from app.brain.rule_parser import RuleParser

parser = RuleParser()

tests = [
    "start work",
    "start workspace",
    "start backend development",
    "open my workspace",
    "begin work",
]

print("=" * 40)
print("Testing Workspace Parser")
print("=" * 40)

for command in tests:

    print("\nCommand:")
    print(command)

    print(parser.parse(command))