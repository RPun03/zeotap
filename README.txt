Rule Engine with Abstract Syntax Tree (AST)
Overview
This project is a 3-tier rule engine application designed to determine user eligibility based on attributes such as age, department, salary, experience, etc. The system uses an Abstract Syntax Tree (AST) to represent conditional rules, allowing dynamic creation, combination, and modification of these rules.


Features
Create Rules:

A rule string is parsed to generate an AST, which is used to represent the conditional logic.
Combine Rules:

Multiple rules can be combined into a single AST to evaluate complex conditions efficiently.
Evaluate Rules:

Given user attributes in a JSON format, the rule engine evaluates the AST to determine whether the user qualifies based on the rule conditions.

Modify Rules:
The system allows modifications to existing rules (e.g., changing operators, adding/removing conditions) to accommodate changing business requirements.
System Design
1. Data Structure
The rule engine uses a Node-based data structure to represent rules as an AST. Each node can either be an operator (AND, OR) or an operand (a condition like age > 30).
Node Types:
Operator Node: Represents logical operators like AND or OR. It has two children (left and right).
Operand Node: Represents a condition such as age > 30. It contains a value (e.g., 30 for comparison).
2. Data Storage
Database Choice:
We use MySQL  to store rules and related metadata. The schema includes a table for storing rules as strings and their AST representation.

API Endpoints
1. create_rule(rule_string)
This API accepts a string representing a rule and returns a Node object representing the AST.

Input: A rule string (e.g., "((age > 30 AND department = 'Sales') OR (age < 25 AND department = 'Marketing')) AND (salary > 50000 OR experience > 5)")
Output: A serialized AST in JSON format.
2. combine_rules(rules)
This API combines multiple rule strings into a single AST. The system optimizes the combination to avoid redundant conditions.

Input: A list of rule strings.
Output: A combined AST representing all rules.
3. evaluate_rule(ast, data)
This API evaluates the given AST against a dictionary of user attributes to determine if the user meets the conditions in the rule.

Input:
ast: The AST to be evaluated (in JSON format).
data: A dictionary containing user attributes (e.g., {"age": 35, "department": "Sales", "salary": 60000, "experience": 3}).
Output: True or False, depending on whether the user qualifies based on the rule.

Test Cases
1. Creating Individual Rules
Test the create_rule function to ensure the AST accurately represents the rule string.

Test: Create AST for rule strings like "age > 30 AND department = 'Sales'".
Expected Output: Correct AST structure.
2. Combining Rules
Test the combine_rules function to verify that the rules are properly merged into a single AST.

Test: Combine two rule strings and check the combined AST.
Expected Output: AST reflecting the logical combination of the rules.
3. Evaluating Rules
Test the evaluate_rule function to ensure it correctly evaluates different JSON user data against the AST.

Test: Evaluate a user’s attributes against different rules.
Expected Output: Return True if the user qualifies, False otherwise.
4. Error Handling
Test error handling for invalid rule strings, unsupported operators, or missing data attributes.

Test: Provide invalid inputs and observe system behavior.
Expected Output: Proper error messages for invalid rule syntax or missing attributes.
