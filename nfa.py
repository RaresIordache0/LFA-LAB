def nfa(data,input_string):
    alphabet=set(data["alphabet"])
    final_states=set(data["final_states"])
    transitions=data["transitions"]
    current_states={data["initial_state"]}
    for symbol in input_string:
        if symbol not in alphabet:
            print(f"{symbol} : invalid input")
            return False
        next_states=set()
        for state in current_states:
            next_states.update( transitions.get((state,symbol),[]) )
        current_states=next_states
    return bool(current_states & final_states)