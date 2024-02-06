class Steps:
    def __init__(self, phrase: str, action: str):
        self.phrase = phrase
        self.action = action
    
    def __str__(self):
        return str(self.phrase)

class Definition:
    def __init__(self, name: str, keyword: str, subidiaries: list):
        self.name = name
        self.keyword = keyword
        self.subsidiaries = subidiaries

    def __str__(self):
        return f'{self.name},{self.keyword},{self.subsidiaries}'

class Math_Set:
    def __init__(self, name: str, items: list, conditions: list):
        self.name = name
        self.items = items
        self.conditions = conditions
        self.count = len(items)

class Math_Function:
    def __init__(self, function_letter: str):
        self.function_letter = function_letter
        