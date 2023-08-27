-- Cria o banco de dados
-- CREATE DATABASE quizdb IF NOT EXISTS;

-- Conecta-se ao banco de dados
\c quizdb;

-- Cria a tabela para armazenar as perguntas do Quiz
CREATE TABLE questions (
    id SERIAL PRIMARY KEY,
    question TEXT NOT NULL,
    options TEXT[] NOT NULL,
    answer INT NOT NULL
);

-- -- Cria o novo usuário
-- CREATE USER douglas WITH PASSWORD 'root';

-- -- Concede privilégios ao novo usuário
-- GRANT ALL PRIVILEGES ON DATABASE quizdb TO douglas;

CREATE TABLE scores(
    id SERIAL PRIMARY KEY,  
    nome VARCHAR(50) NOT NULL,
    score INT NOT NULL
);

INSERT INTO questions (question, options, answer) VALUES ('Qual é a maior montanha do mundo?', '{"Monte Everest", "Monte Kilimanjaro", "Monte McKinley", "Monte Fuji"}', 0);
INSERT INTO questions (question, options, answer) VALUES ('Qual é o maior mamífero terrestre?', '{"Elefante africano", "Baleia-azul", "Girafa", "Rinoceronte"}', 1);
INSERT INTO questions (question, options, answer) VALUES ('Qual é o elemento químico mais abundante na crosta terrestre?', '{"Oxigênio", "Silício", "Hidrogênio", "Ferro"}', 1);
-- INSERT INTO questions (question, options, answer) VALUES ('Qual é o maior planeta do sistema solar?', '{"Júpiter", "Terra", "Vênus", "Marte"}', 0);

