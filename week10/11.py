import psycopg2
import csv
import os

# коннектимся с базой
con = psycopg2.connect(
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)
cur = con.cursor()

# саму табличку создаем
def create_table():
    cur.execute("""
        create table if not exists phonebook (
            id serial primary key,
            name varchar(100),
            phone varchar(20)
        );
    """)
    con.commit()

# функция, возвращающая все записи по шаблону
def search_records(pattern):
    cur.execute("""
        select id, name, phone
        from phonebook
        where name ilike %s or phone ilike %s;
    """, ('%' + pattern + '%', '%' + pattern + '%'))
    return cur.fetchall()

# процедура для вставки нового пользователя или обновления телефона, если пользователь существует
def upsert_user(name, phone):
    cur.execute("""
        select 1 from phonebook where name = %s;
    """, (name,))
    if cur.fetchone():
        cur.execute("""
            update phonebook set phone = %s where name = %s;
        """, (phone, name))
    else:
        cur.execute("""
            insert into phonebook (name, phone) values (%s, %s);
        """, (name, phone))
    con.commit()
    print(f"user '{name}' inserted or updated.")

# процедура для вставки нескольких новых пользователей с проверкой корректности телефона
def insert_many_users(users):
    incorrect_data = []
    for name, phone in users:
        if phone and not phone.strip().isdigit() and not (phone.startswith('+') and phone[1:].isdigit()):
            incorrect_data.append({'name': name, 'phone': phone})
        else:
            upsert_user(name, phone)
    if incorrect_data:
        print("\nincorrect phone numbers found:")
        for data in incorrect_data:
            print(f"name: {data['name']}, phone: {data['phone']}")

# функция для запроса данных с пагинацией
def get_paged_records(limit=10, offset=0):
    cur.execute("""
        select id, name, phone
        from phonebook
        limit %s offset %s;
    """, (limit, offset))
    return cur.fetchall()

# процедура для удаления данных по имени пользователя или телефону
def delete_record(identifier):
    cur.execute("""
        delete from phonebook where name = %s or phone = %s;
    """, (identifier, identifier))
    con.commit()
    print(f"record with identifier '{identifier}' deleted.")

# из csv грузим данные
def insert_fromcsv(filename):
    if not os.path.exists(filename):
        print(f"error: file '{filename}' not found.")
        return
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # скипаем заголовки
        users_to_insert = []
        for row in reader:
            if len(row) == 2:
                users_to_insert.append((row[0], row[1]))
            else:
                print(f"warning: skipping invalid row in csv: {row}")
        insert_many_users(users_to_insert)
    print("data inserted from csv file.")

# ввод с консоли
def console_insert():
    name = input("enter name: ")
    phone = input("enter phone number: ")
    upsert_user(name, phone)

# апдейтим запись
def update_data():
    old_identifier = input("enter the name or phone to update: ")
    cur.execute("""
        select name, phone from phonebook where name = %s or phone = %s;
    """, (old_identifier, old_identifier))
    existing_record = cur.fetchone()
    if not existing_record:
        print(f"record with identifier '{old_identifier}' not found.")
        return

    new_name = input(f"enter new name (current: {existing_record[0]}, press enter to skip): ") or existing_record[0]
    new_phone = input(f"enter new phone number (current: {existing_record[1]}, press enter to skip): ")
    cur.execute("""
        update phonebook set name = %s, phone = %s where name = %s or phone = %s;
    """, (new_name, new_phone, old_identifier, old_identifier))
    con.commit()
    print("record updated.")

# ищем и отображаем записи
def query_data():
    keyword = input("enter name or phone to search (press enter to show all): ")
    results = search_records(keyword)
    if results:
        print("\nsearch results:")
        for row in results:
            print(row)
    else:
        print("no matching records found.")

# удаляем запись
def delete_data():
    value = input("enter name or phone to delete: ")
    delete_record(value)

# меню проги
def menu():
    create_table()
    while True:
        print("""
========= phonebook menu =========
1. upload from csv file
2. insert entry manually
3. update existing entry
4. search entries
5. delete entry
6. show all entries (paginated)
7. exit
""")
        choice = input("select an option (1–7): ")

        if choice == "1":
            insert_fromcsv("contacts.csv")
        elif choice == "2":
            console_insert()
        elif choice == "3":
            update_data()
        elif choice == "4":
            query_data()
        elif choice == "5":
            delete_data()
        elif choice == "6":
            limit = int(input("enter records per page: ") or 10)
            offset = int(input("enter page number (starting from 0): ") or 0) * limit
            results = get_paged_records(limit, offset)
            if results:
                print("\npaged records:")
                for row in results:
                    print(row)
            else:
                print("no records found.")
        elif choice == "7":
            break
        else:
            print("invalid option, please try again.")

    cur.close()
    con.close()
    print("program exited.")

if __name__ == "__main__":
    menu()
