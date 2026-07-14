from app.llm.parser import LLMParser

print("=" * 40)
print("Testing Parser")
print("=" * 40)

text = """
{
    "intent":"open_application",
    "target":"firefox"
}
"""

result = LLMParser.parse(text)

print(result)

print(type(result))

print("\nParser Test Complete")