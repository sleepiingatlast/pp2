import psycopg2
import csv

#коннектимся с базой
con = psycopg2.connect(
    #1dbname="phonebook_db",
    user="postgres",
    password="12345",
    host="localhost",
    port="5432"
)
cur = con.cursor()

#саму табличку создаем
def create_table():
    cur.execute("""
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(100),
            phone VARCHAR(20)
        );        
     """)
    con.commit()
    
#из csv грузим данные
def insert_fromcsv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader) #скипаем заголовки
        for row in reader:
            cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (row[0], row[1]))
    con.commit()
    print("data inserted from csv file")
    
    
#ввод с консоли
def console_insert():
    name = input("enter name: ")
    phone = input("enter phone number: ")
    cur.execute("INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)", (name, phone))
    print("entry was added")
    
#апдейтим запись
def update_data():
    old_name = input("enter the name to update: ")
    new_name = input("enter new name: ")
    new_phone = input("enter new phone number (press Enter to skip): ")
    
    if new_name:
        cur.execute("UPDATE PhoneBook SET name = %s WHERE name = %s", (new_name, old_name))
    if new_phone:
        cur.execute("UPDATE PhoneBook SET phone = %s WHERE phone = %s", (new_phone, new_name or old_name))
    con.commit()
    print("updated")
    
#ищем и отображаем записи
def query_data():
    keyword = input("enter name to search (press enter to show all): ")
    if keyword:
        cur.execute("SELECT * FROM PhoneBook WHERE name ILIKE %s", ('%' + keyword + '%',))
    else: 
        cur.execute("SELECT * FROM PhoneBook")
    results = cur.fetchall()
    for row in results:
        print(row)
        
#удаляем запись
def delete_data():
    value = input("enter name or phone to delete: ")
    cur.execute("DELETE FROM PhoneBook WHERE name = %s OR phone = %s", (value, value))
    con.commit()
    print("deleted")
        
#меню проги
def menu():
    create_table()
    while True:
        print("""
========= PHONEBOOK MENU =========
1. Upload from CSV file
2. Insert entry manually
3. Update existing entry
4. Search entries
5. Delete entry
6. Exit              
""")
        choice = input("Select an option (1–6): ")

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
            break
        else:
            print("invalid option, please try again")
            
    cur.close()
    con.close()
    print("program exited")
    
    
if __name__ == "__main__":
    menu()