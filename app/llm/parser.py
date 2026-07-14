import json
import re


class LLMParser:
    """
    Converts LLM responses into Python objects.
    """

    @staticmethod
    def parse(text: str):
        """
        Parse JSON returned by the LLM.

        Returns:
            dict | list | None
        """

        if not text:
            return None

        text = text.strip()

        # Remove Markdown code fences if present
        text = re.sub(r"^```(?:json)?", "", text, flags=re.IGNORECASE).strip()
        text = re.sub(r"```$", "", text).strip()

        try:
            return json.loads(text)

        except json.JSONDecodeError:
            pass

        # Try extracting JSON object
        match = re.search(r"\{.*\}", text, re.DOTALL)

        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass

        # Try extracting JSON array
        match = re.search(r"\[.*\]", text, re.DOTALL)

        if match:
            try:
                return json.loads(match.group())
            except json.JSONDecodeError:
                pass

        return None