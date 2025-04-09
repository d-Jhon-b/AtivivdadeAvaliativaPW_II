create database atividade_mysql_python;

use atividade_mysql_python;

CREATE TABLE IF NOT EXISTS usuario (
	id INT AUTO_INCREMENT PRIMARY KEY,
	nome_user VARCHAR(255) NOT NULL,
	email varchar(255) not null,
	CONSTRAINT chk_nome_user_min_length CHECK (LENGTH(nome_user) >= 3)
);

insert into usuario(nome_user, email)
values('jhon', 'jhon@gmail.com');
insert into usuario(nome_user, email)
values('Lester', 'Leste@gmail.com');
insert into usuario(nome_user, email)
values('Michael', 'Michael@gmail.com');
insert into usuario(nome_user, email)
values('Zoio', 'Zoio@yahoo.com');
select *from usuario;

CREATE TABLE produto (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(255) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL,
    qtdeestoque INT UNSIGNED NOT NULL,
    CONSTRAINT chk_nome_min_length CHECK (LENGTH(nome) >= 3),
    CONSTRAINT chk_preco_positivo CHECK (preco > 0),
    CONSTRAINT chk_estoque_nao_negativo CHECK (estoque >= 0)
);
insert into produto(nome, preco, qtdeEstoque)
values('Maçã', 10.20, 5);
insert into produto(nome, preco, qtdeEstoque)
values('Calça', 100, 40);
insert into produto(nome, preco, qtdeEstoque)
values('Caldo de mocoto', 2.50, 100);
insert into produto(nome, preco, qtdeEstoque)
values('Melancia', 5, 5000);
insert into produto(nome, preco, qtdeEstoque)
values('Banana', 2.99, 1000);
insert into produto(nome, preco, qtdeEstoque)
values('Pera', 10.20, 5);

select *from produto;
/*update produto set nome='PAMONHA',preco =100, qtdeEstoque =100 where id = 1;
*/
delete from produto where id = 8;

drop table usuarios;
select * from usuario;
commit;