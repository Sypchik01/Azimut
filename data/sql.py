def get_sql(sql_name, sql_mod=''):
    sql_text = ''
    if sql_name == 'histori_roll':
        sql_text = 'select histori_text  from v_histori_roll'

    elif sql_name == 'histori_roll_in_injuries':
        sql_text = 'begin pk_histori_roll.histori_roll_in_injuries(\''+sql_mod+'\') ; end;'

    return sql_text
