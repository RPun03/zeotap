# app/api.py
from flask import Flask, request, jsonify
from app.rule_engine import create_rule, evaluate_rule, combine_rules
from database.models import save_rule, get_rules

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    rule_string = request.json['rule']
    rule_ast = create_rule(rule_string)
    save_rule(rule_string, rule_ast)  
    return jsonify({"rule_ast": repr(rule_ast)})


@app.route('/combine_rules', methods=['POST'])
def combine_rules_endpoint():
    rules = get_rules()  
    combined_rule = combine_rules([rule['rule_ast'] for rule in rules])
    return jsonify({"combined_rule": repr(combined_rule)})


@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    rule_ast = request.json['rule_ast']
    user_data = request.json['user_data']
    result = evaluate_rule(rule_ast, user_data)
    return jsonify({"result": result})


if __name__ == '__main__':
    app.run(debug=True)
