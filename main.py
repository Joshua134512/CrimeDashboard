from extraction.functions import download_files
from config import settings
from execution.execute import execute_functions, list_commands
import sys

def main():
    input = sys.argv[1]
    if input == 'help':
        print('Commands can be found in --- execution > commands.yml --- \n alternatively, type "python main.py list" for a list of commands \n execute a command with "python main.py <command_name>" in the terminal')
    elif input == 'list':
        list_commands()
    else:
        execute_functions(input)
    return

if __name__ == '__main__':
    main()