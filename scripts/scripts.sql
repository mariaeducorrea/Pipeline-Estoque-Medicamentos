--criacao das taçbelas
CREATE TABLE grupos (
	id_grupo SERIAL PRIMARY KEY,
	nm_grupo VARCHAR(100)
);


CREATE TABLE unidades (
	id_unidade SERIAL PRIMARY KEY,
	nm_unidade VARCHAR(100)
);


CREATE TABLE produtos (
	id_produto SERIAL PRIMARY KEY,
	nm_produto VARCHAR(100),
	cod_grupo INT REFERENCES grupos(id_grupo),
	cod_unidade INT REFERENCES unidades(id_unidade)
);

CREATE TABLE estoques (
	id_estoque SERIAL PRIMARY KEY,
	nm_estoque VARCHAR(100) 
);


CREATE TABLE produto_estoque (
	id_produto_estoque SERIAL PRIMARY KEY,
	cod_estoque INT REFERENCES estoques(id_estoque),
	cod_produto INT REFERENCES produtos(id_produto),
	qtd INT
);

--limpar registros adicionados ao testar codigo 

--desabilita restrições temporariamente (evita erro de dependência de FK)
ALTER TABLE produto_estoque DISABLE TRIGGER ALL;
ALTER TABLE produtos DISABLE TRIGGER ALL;

--apaga dados (ordem importa por causa das chaves estrangeiras)
TRUNCATE TABLE produto_estoque RESTART IDENTITY CASCADE;
TRUNCATE TABLE produtos RESTART IDENTITY CASCADE;
TRUNCATE TABLE grupos RESTART IDENTITY CASCADE;
TRUNCATE TABLE unidades RESTART IDENTITY CASCADE;
TRUNCATE TABLE estoques RESTART IDENTITY CASCADE;

--reabilita as restrições
ALTER TABLE produto_estoque ENABLE TRIGGER ALL;
ALTER TABLE produtos ENABLE TRIGGER ALL;

--alterando tabelas apra não repetir registros

--alterando tabela grupos
ALTER TABLE grupos
ALTER COLUMN nm_grupo SET NOT NULL,
ADD CONSTRAINT grupos_nm_grupo_unique UNIQUE (nm_grupo);

--alterar tabela unidades
ALTER TABLE unidades
ALTER COLUMN nm_unidade SET NOT NULL,
ADD CONSTRAINT unidades_nm_unidade_unique UNIQUE (nm_unidade);

--alterar tabela estoque
ALTER TABLE estoques 
ALTER COLUMN nm_estoque SET NOT NULL,
ADD CONSTRAINT estoques_nm_estoque_unique UNIQUE (nm_estoque);

--alterar tabela produtos
ALTER TABLE produtos
ALTER COLUMN nm_produto SET NOT NULL,
ADD CONSTRAINT produto_unique UNIQUE (nm_produto, cod_grupo, cod_unidade);

--alterar tabela produto_estoque
ALTER TABLE produto_estoque
ADD CONSTRAINT produto_estoque_unique UNIQUE (cod_produto, cod_estoque);


--visualizar tabelas
SELECT * FROM grupos
SELECT * FROM unidades
SELECT * FROM produtos
SELECT * FROM estoques
SELECT * FROM produto_estoque