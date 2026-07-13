from app.llm.manager import LLMManager

print("=" * 40)
print("Testing Kara LLM")
print("=" * 40)

llm = LLMManager()

response = llm.ask("Say hello in one short sentence.")

print("\nSuccess:", response.success)
print("\nResponse:")
print(response.content)

if response.error:
    print("\nError:")
    print(response.error)

print("\nLLM Test Complete")