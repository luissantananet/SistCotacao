DELIMITER //
# salvar dados na tabelas cotacao / tarifa / cubagem 
create procedure salvar_cotacao(
	frete_pesos decimal(7,2), pedagios decimal(7,2),ad_valorens decimal(7,2),griss decimal(7,2),taxas decimal(7,2),icmss decimal(7,2),f_cifs decimal(7,2),f_fobs decimal(7,2),flitorals decimal(7,2),
    dim1s decimal(5,2),dim2s decimal(5,2),dim3s decimal(5,2),volumes int,m3s decimal(6,3),
    emit_cnpjs varchar(14),emit_nomes varchar(100),dest_cnpjs varchar(14),dest_nomes varchar(100),cidade_origems varchar(100),estado_origems varchar(100),cidade_destinos varchar(100),estado_destinos varchar(100),tipos varchar(3),valor_mercs decimal(10,2),pesos decimal(10,3),volumess int,tipo_mercs varchar(100),peso_cubo_totals decimal(10,3),m3_totals decimal(10,3))
begin
	start transaction;
        insert into tarifa(frete_peso,pedagio,ad_valoren,gris,taxa,icms,f_cif,f_fob,flitoral) 
        values(frete_pesos,pedagios,ad_valorens,griss,taxas,icmss,f_cifs,f_fobs,flitorals);
        SELECT LAST_INSERT_ID() INTO @id;
        insert into cubagem(dim1,dim2,dim3,volume,m3) 
        values(dim1s,dim2s,dim3s,volumes,m3s);
        SELECT LAST_INSERT_ID() INTO @id;
        insert into cotacao(emit_cnpj,emit_nome,dest_cnpj,dest_nome,cidade_origem,estado_origem,cidade_destino,estado_destino,tipo,valor_merc,peso,volume,tipo_merc,peso_cubo_total,m3_total) 
        values(emit_cnpjs,emit_nomes,dest_cnpjs,dest_nomes,cidade_origems,estado_origems,cidade_destinos,estado_destinos,tipos,valor_mercs,pesos,volumess,tipo_mercs,peso_cubo_totals,m3_totals);
	commit;
end //
Delimiter ;