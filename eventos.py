create database site_eventos;
use site_eventos;

CREATE TABLE eventos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    data DATE,
    localizacao VARCHAR(100),
    capacidade INT
);

CREATE TABLE participantes (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100),
    idade INT
);

CREATE TABLE ingressos (
    id INT PRIMARY KEY,
    evento_id INT,
    participante_id INT,
    preco DECIMAL(10, 2),
    FOREIGN KEY (evento_id) REFERENCES eventos(id),
    FOREIGN KEY (participante_id) REFERENCES participantes(id)
);

-- Inserção de dados para exemplificação
INSERT INTO eventos (id, nome, data, localizacao, capacidade)
VALUES
    (1, 'Conferência de Tecnologia', '2024-03-15', 'Centro de Convenções A', 500),
    (2, 'Festival de Música', '2024-05-20', 'Parque da Cidade', 1000),
    (3, 'Feira de Negócios', '2024-07-10', 'Centro de Exposições B', 800);

INSERT INTO participantes (id, nome, email, idade)
VALUES
    (1, 'Ana Silva', 'ana@example.com', 30),
    (2, 'João Santos', 'joao@example.com', 25),
    (3, 'Maria Oliveira', 'maria@example.com', 35);

INSERT INTO ingressos (id, evento_id, participante_id, preco)
VALUES
    (1, 1, 1, 50.00),
    (2, 1, 2, 50.00),
    (3, 2, 1, 80.00),
    (4, 2, 3, 80.00),
    (5, 3, 2, 30.00),
    (6, 3, 3, 30.00);

SELECT e.nome AS evento, COUNT(i.id) AS ingressos_vendidos FROM eventos e LEFT JOIN ingressos i ON e.id = i.evento_id GROUP BY e.nome; 

SELECT e.nome AS evento, MIN(p.idade) AS idade_mais_jovem FROM eventos e INNER JOIN ingressos i ON e.id = i.evento_id INNER JOIN participantes p ON i.participante_id = p.id GROUP BY e.nome;

SELECT p.nome AS participante, p.email, COUNT(DISTINCT i.evento_id) AS eventos_comprados FROM participantes p INNER JOIN ingressos i ON p.id = i.participante_id GROUP BY p.id HAVING COUNT(DISTINCT i.evento_id) > 1;

SELECT AVG(p.idade) AS media_idade FROM participantes p INNER JOIN ingressos i ON p.id = i.participante_id INNER JOIN eventos e ON i.evento_id = e.id WHERE e.nome = 'Festival de Música'; 

SELECT e.nome AS evento, e.capacidade, COUNT(i.id) AS ingressos_vendidos,
(COUNT(i.id) / e.capacidade) * 100 AS percentual_vendido
FROM eventos e
LEFT JOIN ingressos i ON e.id = i.evento_id
GROUP BY e.id
HAVING (COUNT(i.id) / e.capacidade) * 100 >= 90;

