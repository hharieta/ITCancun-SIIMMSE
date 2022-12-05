drop table users;
create table if not exists users(
    id integer not null primary key autoincrement,
    control_number integer unique,
    names varchar,
    fathers_lastname varchar,
    mothers_lastname varchar,
    email varchar unique,
    passwor varchar not null,
    datebirth date
);

insert into users (control_number, email, passwor) values (20530228, "L20530228@cancun.tecnm.mx", "12345678")