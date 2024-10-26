CREATE DATABASE rule_engine_db;
USE rule_engine_db;

CREATE TABLE rules (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rule_string VARCHAR(255) NOT NULL,
    rule_ast TEXT NOT NULL
);
