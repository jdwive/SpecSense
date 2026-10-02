from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from utils import load_file

# Directory containing prompt templates
PROMPTS_DIR = Path(__file__).parent / "prompts"


def load_prompt(filename: str) -> str:
    """
    Load a prompt template from the prompts directory.

    Args:
        filename: Name of the prompt template file.

    Returns:
        The prompt template as a string.
    """
    return load_file(PROMPTS_DIR / filename)


# Select the prompt template to use
PROMPT = load_prompt("react.md")  # Change filename to switch strategies

print(PROMPT)


def generate_prompt(user_input: str) -> str:
    """
    Generate a prompt for SpecSense AI.

    Available strategies:
        - REACT_PROMPT:
          Step-by-step reasoning to understand user intent,
          extract product constraints, match products,
          and explain recommendations.

        - FEWSHOT_PROMPT:
          Learn from example product queries and recommendations
          to produce consistent outputs.

        - STRICT_JSON_PROMPT:
          Return only valid JSON containing user intent,
          constraints, recommendations, trade-offs,
          and confidence.

        - SIMPLIFIED_PROMPT:
          Quickly identify user intent and recommend the
          best matching product(s) with minimal reasoning.

    Args:
        user_input: Natural language product query.

    Returns:
        A formatted prompt string ready for LLM execution.
    """
    return f"{PROMPT}\n\nUser Query:\n{user_input.strip()}"