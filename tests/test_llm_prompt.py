from app.llm.manager import LLMManager
from app.llm.parser import LLMParser

print("=" * 40)
print("Testing Kara Prompt")
print("=" * 40)

manager = LLMManager()

response = manager.ask("Could you launch Firefox?")

print("\nRaw Response:")
print(response.content)

task = LLMParser.parse(response.content)

print("\nParsed Task:")
print(task)

print("\nType:")
print(type(task))

print("\nPrompt Test Complete")