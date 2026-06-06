from config import *
from collections import defaultdict
def dfa(data,input_string):
    alphabet=set(data["alphabet"])
    final_states=set(data["final_states"])
    transitions=data["transitions"]
    current_state=data["initial_state"]
    for symbol in input_string:
        if symbol not in alphabet:
            print(f"{symbol} : invalid input")
            return False
        if (current_state,symbol) not in transitions:
            current_state=current_state
        else:
            current_state=transitions[(current_state,symbol)][0]    
    return current_state in final_states
