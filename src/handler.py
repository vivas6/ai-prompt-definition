import sys
import service


# Validate args and call service
if len(sys.argv) == 3:
    print(f'{sys.argv[1]}: {sys.argv[2]}')
    if sys.argv[1] == 'find':
        print(service.findPrompts(sys.argv[2]))
    elif sys.argv[1] == 'get':
        print(service.getPrompt(sys.argv[2]))
    elif sys.argv[1] == 'run':
        print(service.runPrompt(sys.argv[2]))

#print(service.getPrompt('classify-1'))
