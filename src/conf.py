import json
import os

current_directory = os.path.dirname(__file__)

PROMPT_LIST_FILE = '../prompt_list.json'
PROMPT_LIST_ABSOLUTE_PATH = os.path.join(current_directory, PROMPT_LIST_FILE)

PROMPS_CONF_DIR='../prompts/'
PROMPT_ABSOLUTE_PATH = os.path.join(current_directory, PROMPS_CONF_DIR)


def loadPromptConfig():
    prompt_dict = {}
    # Read prompt list file
    with open(PROMPT_LIST_ABSOLUTE_PATH) as f:
        pList = json.load(f)

    # Iterate the prompt list
    for config in pList.get('prompts'):
        file = config.get('ref')
        #print(f'File: {file}')

        # Iterate the prompt configuration
        with open(PROMPT_ABSOLUTE_PATH+file) as f:
            content = json.load(f)
            pName = content.get('name')
            #print(f'Prompt name: {pName}')
            
            prompt_dict[file] = content
        
    return prompt_dict


