.headers on
.mode column

PRAGMA foreign_key = on;

drop table person;
drop table accounts;
drop table address;

create table person (
	id integer primary key autoincrement not null,
	name text not null, age integer not null);

create table accounts ( 
	id integer primary key autoincrement not null,
	user_id integer not null, branch_code integer not null,
	number_account integer not null, amount numeric not null, 
	foreign key (person_id) references person(id));

create table address (
	id integer primary key autoincrement not null, 
	user_id integer not null,
	street text not null,
	number integer not null,
	city text not null, 
	country text not null,
	foreign key (person_id) references person(id));

insert into person (name, age) values
	('Nivea'),
	('Daniel'),
	('Bruna'),
	('Madalena');

insert into accounts (user_id, branch_code, number_account, amount) values
	(2, 35, 2423, 65000),
	(1, 17, 9798, 1000),
	(3, 17, 3452, 2300);

insert into address (user_id, street, number, city, country) values
	(3, 'Av Dom Pedro', 65, 'Santo André', 'Brasil'),
	(2, 'Av forte do Leme', '1205', 'São Paulo', 'Brasil'),
	(1, 'Rua Costa Aguiar', 786, 'Florianópolis', 'Brasil'),
	(4, 'Rua João Ramalho', 265, 'Araraquara', 'Brasil');

update users set name = 'Alfredo';

select avg(age) from users;




	

