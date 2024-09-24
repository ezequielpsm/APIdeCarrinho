create database if not exists cinema;
use cinema;
create table if not exists filmes (
	titulo varchar(50) not null,
    genero varchar(30) not null,
    ano int not null,
    primary key(titulo)
);
insert into filmes(titulo, genero, ano)
value ("Forest Gump", "Dama", 1994);