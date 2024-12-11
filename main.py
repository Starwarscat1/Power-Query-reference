import random

parts = {
    "Part 1: M code operators": {
        'Combination operator': '&',
        'Greater than operator': '>',
        'Greater than or equal operator': '>=',
        'Less than operator': '<',
        'Less than or equal operator': '<=',
        'Equal operator': '=',
        'Not equal operator': '<>',
        'Conditional logical operator where a single true makes the result true': 'or',
        'Conditional logical operator where a single false makes the result false': 'and',
        'Logical operator where truth value is converted to the opposite truth value': 'not',
        'Record lookup operator (Access the fields of a record by name)': '[]',
        'List indexer operator (Access an item in a list by its zero-based numeric index)': '{}'
    },
    "Part 2: Data Types": {
        'classifies the null value': 'type null',
        'classifies the values true and false': 'type logical',
        'classifies numeric values': 'type number',
        'classifies values like “4:53:12 AM”': 'type time',
        'classifies values like “1/4/2023”': 'type date',
        'classifies values like “1/4/2023 4:53:12 AM”': 'type datetime',
        'classifies values like “2 days 4 hours 3 minutes 35 seconds”': 'type duration',
        'classifies string values': 'type text',
        'classifies values like {}': 'type list',
        'classifies values like [a = 1, b = 2]': 'type record'
    },
    "Part 3: General questions": {
        'On the topic of conditionals, write out code that compares the variables num1 and num2 and outputs the greater value. In the comparison, num2 should appear first.': 'if num2 > num1 then num2 else num1',
        'On the topic of functions, write out a function that receives 3 arguments called x, y, and z of type number and outputs the sum of the arguments. The function name is “MyFunction”. The first two arguments are required. The last one is optional. The output type of the function is number. On the next line, call the function that was just defined and store the result in the variable “Result1”. The function arguments will be 1, 2, 3. Do not include the "let" keyword or the "in" block in your answer. Write your answer all on one line.': 'MyFunction = (x as number, y as number, optional z as number) as number => x + y + z, Result1 = MyFunction(1, 2, 3)',
        'Write out a “let” expression. For the first block of code, use “a = 1” followed by “b = a + 1”. For the second block of code, use “b”.': 'let a = 1, b = a + 1 in b',
        'The combination operator can combine what 3 types?': 'text, list, record',
        'What is the symbol for a single line comment?': '//',
        'What is the symbol(s) for a multi-line comment?': '/* */',
        'What symbol is used to seperate lines of code?' : ',',
        'Within a function definition, are you allowed to set an optional parameter to a value? For example, (y as number, optional z as number = 15) as number => .... Please answer yes or no.' : 'no'
    }
}

for part, questions in parts.items():
    print("\n" + part + "\n")
    items = list(questions.items())
    random.shuffle(items)

    for question, answer in items:
        user_answer = input(question + "\n")
        while user_answer.lower() != answer.lower() and user_answer.lower() != 'skip':
            print("Sorry, that's incorrect.")
            user_answer = input(question + "\n")

        if user_answer.lower() == 'skip':
            continue

        print("Correct!")
