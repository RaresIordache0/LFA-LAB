# pda deterministic 
def pda(data,input_string):
    alphabet=set(data["alphabet"])
    transitions=data["transitions"]
    initial_state=data["initial_state"]
    final_states=set(data["final_states"])
    stack_alphabet=set(data["stack_alphabet"])
    stack=[data["initial_stack"]]
    state=initial_state
    i=0
    while True:
        stack_top=stack[-1] if stack else "e"
        # tranzitii epsilon
        key=(state,"e",stack_top)

        if key in data["transitions"]:
            next_state,action=data["transitions"][key]

            state=next_state

            if stack:
                stack.pop()

            if action!="e":
                for x in reversed(action):
                    stack.append(x)

            continue

        if i>=len(input_string):
            break
        symbol=input_string[i]
        key=(state,symbol,stack_top)
        if key not in data["transitions"]:
            return False

        next_state,action=data["transitions"][key]
        state=next_state
        if stack:
            stack.pop()
        if action!="e":
            for x in reversed(action):
                stack.append(x)
        i+=1
    return state in data["final_states"]