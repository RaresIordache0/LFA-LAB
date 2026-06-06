from collections import defaultdict
def get_data(filename):
    data={
        "alphabet":[],
        "states":[],
        "initial_state":None,
        "final_states":[],
        "transitions":defaultdict(list),
        "stack_alphabet":[],
        "initial_stack":['$']
    }
    current_section=None
    with open(filename,"r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("//"):
                continue
            if line.startswith("[") and line.endswith("]"):
                current_section=line.lower()
                continue
            if current_section=="[alphabet]":
                data["alphabet"].extend(line.split())
            elif current_section=="[states]":
                data["states"].append(line)
            elif current_section=="[initial state]":
                data["initial_state"] = line
            elif current_section=="[final states]":
                data["final_states"].append(line)
            elif current_section=="[transitions]":
                parts = [p.strip() for p in line.split("->")]
                if len(parts)==3:    #verific daca transitiile sunt pentru un dfa/nfa sau un pda
                    source,symbol,dest=map(str.strip, line.split("->"))
                    data["transitions"][(source, symbol)].append(dest)
                elif len(parts)==5:
                    source,symbol,stack_top,action,destination=parts
                    data["transitions"][(source,symbol,stack_top)]=(destination,action)
            elif current_section=="[stack alphabet]":
                data["stack_alphabet"].extend(line.split())
            elif current_section=="[initial stack]":
                data["initial_stack"]=line.strip()    
    return data