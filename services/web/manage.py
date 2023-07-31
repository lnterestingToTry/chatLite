from flask.cli import FlaskGroup

from project import app, db, models

from datetime import datetime

import re
from sqlalchemy import text

import threading
import time


cli = FlaskGroup(app)


dump_root = "db_dumps"


@cli.command("dump_db")
def dump_db():
    # try:
    #     with open(f'{dump_root}/db_dump.sql', 'r') as prev:
    #         prev_dump = prev.read()
        
    #     with open(f'{dump_root}/db_dump.sql', 'w') as copy:
    #         copy.write(prev_dump)

    # except Exception as error:
    #     print(error)
    current_datetime = datetime.now()
    formatted_datetime = current_datetime.strftime('%Y-%m-%d %H:%M:%S')

    try:
        with open(f'{dump_root}/db_dump_{formatted_datetime}.sql', "w") as dump_file:
            tables = db.metadata.sorted_tables
            #tables_meta = db.metadata.sorted_tables
            #print(tables)
            for table, model in zip(tables, models):
                rows = model.query.all()
                columns = [column.name for column in table.columns]
                dump_file.write(f"-- Table: {table.name}\n")
                for row in rows:
                    column_names = ', '.join(columns)

                    row_values_list = []

                    for column in table.columns:

                        value = getattr(row, column.name)

                        value_str = f"'{value}'"

                        row_values_list.append(value_str)

                        if column.primary_key: 
                            if column.autoincrement:
                                curent_id = int(row_values_list[0].strip("'"))
                                dump_file.write(f"SELECT setval(pg_get_serial_sequence('{table.name}', 'id'), {curent_id}, true)\n")
                        
                    row_values = ', '.join(row_values_list)
                    
                    dump_file.write(f"INSERT INTO {table.name}({column_names}) VALUES ({row_values});\n")
    except Exception as error:
        print(error)


#docker-compose exec web python manage.py insert_dump_db
@cli.command("insert_dump_db")
def insert_dump_db(file_name):
    #file_path = "db_dump.sql"
    file_path = file_name
    
    try:
        with open(file_path, 'r') as dump_file:
            lines = dump_file.readlines()
            
            current_table = None
            
            for line in lines:
                if line.startswith('-- Table: '):
                    current_table = re.search(r"-- Table: (.*)\n", line).group(1)
                elif current_table and line.strip():
                    sql_expr = text(line)
                    db.session.execute(sql_expr)
                
            db.session.commit()
                
    except Exception as error:
        print(error)


@cli.command("rebuild_db")
def rebuild_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

@cli.command("delete_db")
def delete_db():
    db.drop_all()
    db.session.commit()


def set_interval(func, interval):
    stopped = threading.Event()

    def loop():
        while not stopped.wait(interval):
            func()

    t = threading.Thread(target=loop)
    t.daemon = True
    t.start()
    return stopped


if __name__ == "__main__":
    cli()
    
    stop_signal = set_interval(dump_db, 10)