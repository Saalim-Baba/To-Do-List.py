import mysql.connector


def sql_add_entry(mycursor, mydb):
    mycursor.execute(f"""INSERT INTO tasks (task, done) VALUES ('{input("Ihre Aufgabe?")}', false)""")

    mydb.commit()

    mydb.close()
    main()


def show_tables(mycursor):
    mycursor.execute("""SELECT * FROM tasks""")
    list = mycursor.fetchall()
    if len(list) == 0:
        print("No tasks")
    for i in list:
        print(i)


def done_task(mycursor, mydb):
    id = int(input("Which ID?"))
    mycursor.execute(f"""UPDATE tasks SET done = true WHERE id={id}""")
    mydb.commit()
    main()


def delete_task(mycursor, mydb):
    id = int(input("Which ID?"))
    try:
        mycursor.execute(f"""DELETE FROM tasks WHERE id = {id}""")
    except NotImplemented:
        print("No ID found")
    mydb.commit()
    main()



def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="123456",
        database="To_Do_List"
    )


    mycursor = mydb.cursor()
    show_tables(mycursor)
    try:
        choice = int(input(f"\nCreate new task?(1)\nFinished a task(2)\nDelete task(3)\nClear all tasks(4)\nExit("
                           f"5)\nEingabe:"))

        if choice == 1:
            sql_add_entry(mycursor, mydb)
        elif choice == 2:
            done_task(mycursor, mydb)
        elif choice == 3:
            delete_task(mycursor, mydb)
        elif choice == 4:
            mycursor.execute("""DELETE FROM tasks""")
            mydb.commit()
            main()
        elif choice == 5:
            print("Bye bye!")
        else:
            print("Please select available options")
            main()
    except ValueError:
        print("No valid input")


if __name__ == "__main__":
    main()
