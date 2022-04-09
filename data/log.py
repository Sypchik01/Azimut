def record_log(record_name_id, record_input):
    with open(r".\directory_log\log_"+record_name_id+".txt", "w", encoding="utf-8") as file:
        file.write(record_input + '\n')