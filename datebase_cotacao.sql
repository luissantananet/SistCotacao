create database cotacao;
use cotacao;

create table tarifa(
	id int not null auto_increment,
    frete_peso decimal(7,2),
    pedagio decimal(7,2),
    ad_valoren decimal(7,2),
    gris decimal(7,2),
    taxa decimal(7,2),
    icms decimal(7,2),
    f_cif decimal(7,2),
    f_fob decimal(7,2),
    flitoral decimal(7,2),
    primary key(id)
);
create table tarifas_minimas(
	id int not null auto_increment,
    descricao varchar(50),
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
    valor_merc decimal(10,2),
    peso decimal(10,3),
    volume int,
    tipo_merc varchar(100),
    peso_cubo_total decimal(10,3),
    m3_total decimal(10,3),
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