
import psycopg2
HOSTNAME = 'localhost'
USERNAME = 'postgres'
PASSWORD = 'Max1780'
DATABASE = 'MenuManager'
connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE)
cursor = connection.cursor()


class MenuItem():
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price

    def save(self):
        cursor.execute(f"insert into menuitem(item_name, price) values ('{self.item_name}', '{self.price}')")
        connection.commit()

    def delete(self):
        cursor.execute(f"delete from menuitem where item_name = '{self.item_name}'")
        connection.commit()


    def update(self, item_name, price):
        cursor.execute(f"update menuitem set item_name = '{item_name}', price = {price} where item_name = '{self.item_name}'")
        connection.commit()

    def all(self):
        cursor.execute(f"select * from menuitem")
        menu = cursor.fetchall()
        for item in menu:
            print(item)

    # Create another method called get_by_name that will return a single MenuItem object depending on it’s name,
    # if an object is not found (there is no item matching the name in the get_by_name method) return None.
    def get_by_name(self):
        cursor.execute(f"select * from menuitem where item_name ilike '%{self.item_name}%'")
        menu = cursor.fetchone()
        print(menu)
        if menu is None:
            return print("We don’t serve this menu")
        else:
            return MenuItem(menu[1], menu[2])



menu_item = MenuItem("table", 10)
# menu_item.save()
# menu_item.delete()
# menu_item.update('Strawberry', 100)
menu_item.all()
# menu_item.get_by_name()
