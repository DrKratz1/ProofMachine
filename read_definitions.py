from classes import Definition, Steps

def read_in() -> list:
    all_defs = []
    current_definition = Definition("NOTHING", "NOTHING", [])
    current_step = Steps("NOTHING", "NOTHING")

    definition_list = open("definitions.txt", "r")
        
    name = False
    keyword = False
    subsidiaries = False

    # reading in definitions
    for i, line in enumerate(definition_list):
        # resetting to new definition
        if line == "\n":
            all_defs.append(current_definition)
            name = False
            keyword = False
            subsidiaries = False
            current_definition = Definition("NOTHING", "NOTHING", [])
            continue
        
        # dealing with the newline
        line = line[:len(line)-1]

        # setting values
        if not name:
            current_definition.name = line
            name = True
        elif name and not keyword:
            current_definition.keyword = line
            keyword = True
        elif name and keyword and not subsidiaries:
            line = line.split(" ? ")
            current_step.phrase = line[0]
            current_step.action = line[1]
            current_definition.subsidiaries.append(current_step)
            current_step = Steps("NOTHING", "NOTHING")
    '''
    # testing
    for defn in all_defs:
        print(f"{defn.name},{defn.keyword},{[each_step.phrase for each_step in defn.subsidiaries]}")
    '''
    # TODO: make dynamic math input for functions and sets
    definition_list.close()
    return all_defs
        

