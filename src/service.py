import util
import conf
import facade

# Load prompt dict
prompt_dict = conf.loadPromptConfig()
#print(f'Dict: {prompt_dict}')

# Find prompt
def findPrompts(query):
    prompts = {}
    for file, content in prompt_dict.items():
        for input in content['inputs']:
            prompt = input['prompt']
        
            if 'text' in prompt and prompt['text'].casefold().find(query.casefold()) != -1:
                key = f"{file}_id_{input['id']}"
                prompts[key] = input['prompt']
            elif 'context' in prompt and prompt['context'].casefold().find(query.casefold()) != -1:
                key = f"{file}_id_{input['id']}"
                prompts[key] = input['prompt']

        return  f"prompts: {prompts}"
    return None

# Get prompt
def getPrompt(id):
    for _, content in prompt_dict.items():
        for input in content['inputs']:
            if id == input['id']:
                return f"prompt: {input['prompt']}"
    return None

# Run prompt and get response from OpenAI
def runPrompt(id):
    for _, content in prompt_dict.items():
        for input in content['inputs']:
            if id == input['id']:
                promptToGPT = util.getPromptToGPT(input['prompt'])   
                print(f"promptToGPT: {promptToGPT}")
                if promptToGPT is None:
                    return "Invalid prompt. Please check the prompt definition."
                response = facade.callOpenAI(promptToGPT, input['model'])
                return f"GPT response: {response}"
    return None

#print(runPrompt('classify-1'))