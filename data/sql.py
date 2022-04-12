def get_sql(sql_name, sql_mod_name='', sql_mod_value=0):
    sql_text = ''
    # ЗАПРОС ИЗ histori_roll
    if sql_name == 'histori_roll':
        sql_text = 'select histori_text  from v_histori_roll'

    # ВЫЗОВ ПРОЦЕДУРЫ histori_injuries
    elif sql_name == 'histori_injuries':
        sql_text = 'begin pk_histori_roll.histori_roll_injuries(\''+sql_mod_name+'\'); end;'

    # ВЫЗОВ ПРОЦЕДУРЫ histori_jumping
    elif sql_name == 'histori_jumping':
        sql_mod_value = str(sql_mod_value)
        sql_text = 'begin pk_histori_roll.histori_roll_jumping(\''+sql_mod_name+'\',\''+sql_mod_value+'\'); end;'

    return sql_text
