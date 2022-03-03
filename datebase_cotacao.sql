create database cotacao;
use cotacao;

create table tarifas(
	id int not null auto_increment,
    descricao varchar(50),
    frete_peso decimal(7,2),
    ad_valoren decimal(7,4),
    gris decimal(7,4),
    taxa decimal(7,2),
    icms decimal(7,2),
    primary key(id)
);
create table tarifas_minimas(
	id int not null auto_increment,
    descricao varchar(50),
    tarifa_base decimal(7,2),
    tarifa_litoral decimal(7,2),
	ad_Gris decimal(7,4),
    pedagio decimal(7,2),
    pedlitoral decimal(7,2),
    primary key(id)
);

create table cotacao(
	id int not null auto_increment,
    emit_cnpj varchar(14),
    emit_nome varchar(100),
    dest_cnpj varchar(14),
    dest_nome  varchar(100),
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
    dim1 decimal(5,2),
    dim2 decimal(5,2),
    dim3 decimal(5,2),
    volume int,
    m3 decimal(6,3),
    primary key(id)
);
CREATE Table cidades(
    id int not null AUTO_INCREMENT,
    cidade VARCHAR(100) NOT NULL,
    uf VARCHAR(100) not null,
    PRIMARY KEY(id)
);

INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 01 até 20Kg',00.00,00.00,00.00,00.00,00.00);
INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 21 até 50Kg',00.00,00.00,00.00,00.00,00.00);
INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 51 até 100Kg',00.00,00.00,00.00,00.00,00.00);
INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 101 até 150Kg',00.00,00.00,00.00,00.00,00.00);
INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 151 até 200Kg',00.00,00.00,00.00,00.00,00.00);
INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 201 até 250Kg',00.00,00.00,00.00,00.00,00.00);
INSERT INTO tarifas_minimas(descricao,tarifa_base,tarifa_litoral,ad_Gris,pedagio,pedlitoral) VALUES('De 251 até 300Kg',00.00,00.00,00.00,00.00,00.00);
INSERT INTO tarifas(frete_peso,ad_valoren,gris,taxa,icms) VALUES(00.00,00.00,00.00,00.00,00.00);
INSERT INTO tarifas(frete_peso,ad_valoren,gris,taxa,icms) VALUES(00.00,00.00,00.00,00.00,00.00);

select * from tarifas_minimas;
select * from tarifas;
