# Prompt Definition
GenAI prompting is an art of constructing natural language input that LLM like ChatGPT can understand and respond back with an output. Often, this is an iterative development process to get into an optimal input for LLM.  

This repo can help you in your educational or small scale GenAI project to store the list of prompts that you developed, with its corresponding OpenAI API parameters. So, you are free from memorising all the prompts and confs that you developed!

### How To
* Create and organise your prompt configuration files in JSON format under the directory *prompts*. Refer prompts directory for sample configuration files.

* Add newly created prompt configuration file meta info in *prompt_list.json*. Refer prompt_list.json for sample prompt configuration.  

Now, 

* To find prompt configuration files with given text in the prompt, run Make command with the respective text.
```
make find <text>
```

* To get a prompt definition by ID, run Make command with the respective prompt ID.
```
make get <ID>
```

* To test a prompt definition towards ChatGPT, run Make command with the respective text.
```
make run <ID>
```

#### Prerequisites  
At present, this repository only supports ChatGPT LLM, but can easily be extended to other LLMs. To test your prompts with ChatGPT, OPEN AI API KEY has to be created and set in the env variable OPENAI_API_KEY.  

### Thoughts:  
* Why shouldn't we come up with a standard prompt specification for managing prompts for multiple LLMs?   


## Author
Vineethkumar Alil Vasudevan  


## Reference
[OpenAI Developer Platform](https://platform.openai.com/docs/overview)  
[Deeplearning.AI](https://www.deeplearning.ai/)