create database comercio_eletronico;
use comercio_eletronico;

CREATE TABLE clientes (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    idade INT,
    cidade VARCHAR(100)
);

CREATE TABLE produtos (
    id INT PRIMARY KEY,
    nome VARCHAR(100),
    categoria VARCHAR(100),
    preco DECIMAL(10, 2)
);

CREATE TABLE vendas (
    id INT PRIMARY KEY,
    cliente_id INT,
    produto_id INT,
    data DATE,
    quantidade INT,
    total DECIMAL(10, 2),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
);

INSERT INTO clientes (id, nome, idade, cidade)
VALUES
    (1, 'João', 30, 'São Paulo'),
    (2, 'Maria', 25, 'Rio de Janeiro'),
    (3, 'Carlos', 35, 'Belo Horizonte'),
    (4, 'Ana', 28, 'Salvador');

INSERT INTO produtos (id, nome, categoria, preco)
VALUES
    (1, 'Camiseta', 'Roupas', 29.99),
    (2, 'Tênis', 'Calçados', 99.99),
    (3, 'Celular', 'Eletrônicos', 799.99),
    (4, 'Livro', 'Livros', 19.99);

INSERT INTO vendas (id, cliente_id, produto_id, data, quantidade, total)
VALUES
    (1, 1, 1, '2024-02-01', 2, 59.98),
    (2, 2, 3, '2024-02-01', 1, 799.99),
    (3, 3, 2, '2024-02-02', 1, 99.99),
    (4, 1, 4, '2024-02-03', 3, 59.97),
    (5, 4, 1, '2024-02-03', 2, 59.98),
    (6, 2, 2, '2024-02-04', 1, 99.99),
    (7, 1, 3, '2024-02-05', 1, 799.99),
    (8, 3, 1, '2024-02-06', 2, 59.98),
    (9, 4, 4, '2024-02-07', 1, 19.99),
    (10, 1, 2, '2024-02-08', 1, 99.99),
    (11, 2, 1, '2024-02-08', 2, 59.98);
    
SELECT cliente_id, SUM(quantidade) AS totaldevendas
FROM vendas
GROUP BY cliente_id;

SELECT data, SUM(quantidade) AS total
FROM vendas
GROUP BY data
HAVING SUM(quantidade) >= 2;

SELECT data, SUM(total) AS TOTAL_VENDIDO
FROM vendas
GROUP BY data
HAVING SUM(total) > 500;

SELECT AVG(idade)
From clientes;

SELECT produto_id, SUM(quantidade) AS Total_Vendido
FROM vendas
GROUP BY produto_id
order by Total_Vendido desc
limit 1;
