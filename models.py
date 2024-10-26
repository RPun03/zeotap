from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json


DATABASE_URI = "mysql+pymysql://root:saibaba45@localhost/rule_engine_db"

engine = create_engine(DATABASE_URI)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Rule(Base):
    __tablename__ = "rules"
    id = Column(Integer, primary_key=True)
    rule_string = Column(String(255), nullable=False)
    rule_ast = Column(Text, nullable=False)

    def __repr__(self):
        return f"<Rule(id={self.id}, rule_string={self.rule_string})>"


Base.metadata.create_all(engine)


def save_rule(rule_string, rule_ast):
    rule_data = Rule(rule_string=rule_string, rule_ast=json.dumps(rule_ast.__dict__))
    session.add(rule_data)
    session.commit()


#
def get_rules():
    rules = session.query(Rule).all()
    return [
        {"rule_string": rule.rule_string, "rule_ast": json.loads(rule.rule_ast)}
        for rule in rules
    ]
