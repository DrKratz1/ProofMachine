from classes import Definition, Steps, Math_Set
from ai import query_ai

out_file = open("output.txt", "w", encoding='utf-8')

def print_and_log(phrase: str) -> None:
    print(phrase)
    out_file.write(phrase + '\n')
    return


def separate_if_then(statement) -> (str,str):
    # Find the index of "if" and "then"
    if_index = statement.find("if")
    then_index = statement.find("then")

    # Extract the conditions and actions
    if_condition = statement[if_index + 2:then_index].strip()
    then_action = statement[then_index + 4:].strip()

    return if_condition, then_action

def find_keyword(question: str, all_defs: list) -> str:

    # looking for keyword in the question
    keyword = "KEYWORD NOT FOUND - CHECK DEFINITION LIST"
    for concept in all_defs:
        if concept.keyword in question:
            keyword = concept.keyword
            break

    print("Keyword: " + keyword)

    if keyword == "KEYWORD NOT FOUND - CHECK DEFINITION LIST":
        return "ERROR"
    return keyword

def find_definition(keyword: str, all_defs: list) -> Definition:

    for concept in all_defs:
        if concept.keyword == keyword:
            return concept

def do_condition(condition_number: int, original_concept: Definition, all_defs: list, current_assumptions: list, has_prev_condition: bool, prev_condition: str, first_run: bool) -> None:
    # doing numbering
    if has_prev_condition:
        current_condition_number = prev_condition + "." + str(condition_number)
        print_and_log(f"\nTo show: ({current_condition_number})")
    else:
        current_condition_number = str(condition_number)
        print_and_log(f"\nTo show: ({current_condition_number})")

    # getting definition
    condition_keyword = original_concept.subsidiaries[condition_number - 1].action
    condition_question = original_concept.subsidiaries[condition_number - 1].phrase
    condition_concept = find_definition(condition_keyword, all_defs)
    print_and_log(condition_question)

    ifs, thens = separate_if_then(condition_question)
    print_and_log(f"Assume: {ifs} \nTo Show: {thens}")
    print_and_log("\nHence:")
    
    # list ai shit
    current_assumptions.append(ifs)

    if condition_keyword == "none":
        # this is the part where we get the user to prove something: we can automate this with chatgpt maybe
        # manual_proof = input("Please show the statement above\n")
        # print_and_log(manual_proof)
        print(current_assumptions)
        manual_proof = query_ai(current_assumptions, thens)
        print_and_log(manual_proof)
        print_and_log(f"Thus: {thens}")
        current_assumptions.pop(-1)
        return
    
    else:
        # means there is a minimum of second level of conditions
        num_conditions = len(condition_concept.subsidiaries)
        for ncondition in range(0,num_conditions):
            if first_run or has_prev_condition:
                print_and_log(f"{current_condition_number}.{ncondition + 1}   {condition_concept.subsidiaries[ncondition].phrase}")
            else:
                print_and_log(f"{ncondition + 1}.   {condition_concept.subsidiaries[ncondition].phrase}")
        
        for ncondition in range(0,num_conditions):
            ncondition += 1
            do_condition(ncondition, condition_concept, all_defs, current_assumptions, True, current_condition_number, False)

def do_proof(question: str, all_defs: list) -> None:
    # initial separation
    ifs, thens = separate_if_then(question)

    # finding keyword for the proof -> keyword comes after the "then" statement
    keyword = find_keyword(thens, all_defs)
    if keyword == "ERROR":
        return
    
    current_concept = find_definition(keyword, all_defs)

    # initial assumptions
    current_assumptions = [ifs,]

    print_and_log(f"Assume: {ifs} \nTo Show: {thens}")
    print_and_log("Hence:")

    num_conditions = len(current_concept.subsidiaries)
    for ncondition in range(0,num_conditions):
        print_and_log(f"{ncondition + 1}.   {current_concept.subsidiaries[ncondition].phrase}")
    
    for ncondition in range(0,num_conditions):
        ncondition += 1
        do_condition(ncondition, current_concept, all_defs, current_assumptions, False, "", True)
    
    # print_and_log("\nSo: " + )
    
    return
    