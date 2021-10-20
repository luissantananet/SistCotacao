create database cotacao;
use cotacao;

create table tarifa(
	id int not null auto_increment,
    tarifa_base decimal,
    ad_valoren decimal,
    gris decimal,
    taxa decimal,
    icms decimal,
    f_cif decimal,
    f_fob decimal,
    flitoral decimal,
    primary key(id)
);
create table tarifa_20(
	id int not null auto_increment,
    tarifa_base decimal,
    gris decimal,
    ffinal decimal,
    ad_valoren decimal,
    ftotal decimal,
    flitoral decimal,
    primary key(id)
);
create table tarifa_50(
	id int not null auto_increment,
    tarifa_base decimal,
    gris decimal,
    ffinal decimal,
    ad_valoren decimal,
    ftotal decimal,
    flitoral decimal,
    primary key(id)
);
create table tarifa_100(
	id int not null auto_increment,
    tarifa_base decimal,
    gris decimal,
    ffinal decimal,
    ad_valoren decimal,
    ftotal decimal,
    flitoral decimal,
    primary key(id)
);
create table tarifa_150(
	id int not null auto_increment,
    tarifa_base decimal,
    gris decimal,
    ffinal decimal,
    ad_valoren decimal,
    ftotal decimal,
    flitoral decimal,
    primary key(id)
);
create table tarifa_200(
	id int not null auto_increment,
    tarifa_base decimal,
    gris decimal,
    ffinal decimal,
    ad_valoren decimal,
    ftotal decimal,
    flitoral decimal,
    primary key(id)
);
create table tarifa_250(
	id int not null auto_increment,
    tarifa_base decimal,
    gris decimal,
    ffinal decimal,
    ad_valoren decimal,
    ftotal decimal,
    flitoral decimal,
    primary key(id)
);
create table tarifa_300(
	id int not null auto_increment,
    tarifa_base decimal,
    gris decimal,
    ffinal decimal,
    ad_valoren decimal,
    ftotal decimal,
    flitoral decimal,
    primary key(id)
);

create table cotacao(
	id int not null auto_increment,
    origem varchar(100),
    destino varchar(100),
    cidade_origem varchar(100),
    estado_origem varchar(100),
    cidade_destino varchar(100),
    estado_destino varchar(100),    
    tipo varchar(3),
    valor_merc decimal,
    peso decimal,
    volume int,
    tipo_merc varchar(100),
    peso_cubo_total decimal,
    m3_total decimal,
    primary key(id)
);
create table cubagem(
	id int not null auto_increment,
    dim1 decimal,
    dim2 decimal,
    dim3 decimal,
    volume int,
    m3 decimal,
    primary key(id)
);