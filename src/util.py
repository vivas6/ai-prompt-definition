
# Validates the prompt. If it is valid, returns the prompt to be sent to OpenAI 
def getPromptToGPT(prompt):
    if 'text' in prompt and 'context' in prompt and 'custom' in prompt:
        return f"{prompt['context']}\n{prompt['text']}\n{prompt['custom']}"
    elif 'text' in prompt and 'context' in prompt:
        return f"{prompt['text']}\n{prompt['context']}"
    elif 'text' in prompt:
        return prompt['text']
    return None


# Test prompt
prompt = f"""
Classify the text into positive, neutral or negative:
Text: The Design of Everyday Things.
Classification:
"""