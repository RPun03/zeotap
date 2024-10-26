
class Node:
    def __init__(self, node_type, left=None, right=None, value=None):
        self.node_type = node_type  
        self.left = left  
        self.right = right  
        self.value = value 

    def __repr__(self):
        return f"Node(type={self.node_type}, value={self.value}, left={self.left}, right={self.right})"


def create_rule(rule_string):
  
    tokens = rule_string.replace('(', '').replace(')', '').split()
    return build_ast(tokens)



def build_ast(tokens):
    if len(tokens) == 1:
        
        return Node("operand", value={tokens[0]: tokens[1]})

    if 'AND' in tokens:
        idx = tokens.index('AND')
        left = build_ast(tokens[:idx])
        right = build_ast(tokens[idx + 1:])
        return Node("operator", left=left, right=right, value="AND")

    if 'OR' in tokens:
        idx = tokens.index('OR')
        left = build_ast(tokens[:idx])
        right = build_ast(tokens[idx + 1:])
        return Node("operator", left=left, right=right, value="OR")


def evaluate_rule(rule_ast, user_data):
    if rule_ast.node_type == "operand":
        key, operator = list(rule_ast.value.items())[0]
        return evaluate_condition(key, operator, user_data[key])
    elif rule_ast.node_type == "operator":
        if rule_ast.value == "AND":
            return evaluate_rule(rule_ast.left, user_data) and evaluate_rule(rule_ast.right, user_data)
        elif rule_ast.value == "OR":
            return evaluate_rule(rule_ast.left, user_data) or evaluate_rule(rule_ast.right, user_data)


def evaluate_condition(key, condition, value):
    
    operator, comp_value = condition[0], int(condition[1:])
    if operator == '>':
        return value > comp_value
    elif operator == '<':
        return value < comp_value
    return False


def combine_rules(rules):
    combined = rules[0]
    for rule in rules[1:]:
        combined = Node("operator", left=combined, right=rule, value="OR")
    return combined
