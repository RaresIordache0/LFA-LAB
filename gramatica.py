import random
def parse_grammar(file_path):
    grammar={
        "sigma": [],
        "variables": [],
        "productions": {}
    }
    section=None
    with open(file_path,"r") as f:
        for line in f:
            line=line.strip()

            if not line or line.startswith("//"):
                continue
            
            if line.startswith("[") and line.endswith("]"):
                if line=="[Sigma]":
                    section="sigma"
                elif line=="[Var]":
                    section="variables"
                elif line=="[Sub]":
                    section="productions"

            if section=="sigma":
                grammar["sigma"]=[x.strip() for x in line.split(",")]

    
            elif section=="variables":
                grammar["variables"]=[x.strip() for x in line.split(",")]

            elif section=="productions":
                if "->" in line:
                    left,right=line.split("->")
                    left=left.strip()
                    right_parts=[r.strip().split() for r in right.split("|")]

                    if left not in grammar["productions"]:
                        grammar["productions"][left]=[]

                    grammar["productions"][left].extend(right_parts)

    return grammar

def generate(symbol,grammar):
    if symbol not in grammar["productions"]:
        return [symbol]
    production=random.choice(grammar["productions"][symbol])
    result=[]
    for sym in production:
        result.extend(generate(sym,grammar))
    return result