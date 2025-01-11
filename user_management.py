import mysql.connector
from mysql.connector import Error

# 数据库配置
config = {
    'user': 'huang1057',
    'password': '1057233',
    'host': 'localhost',
    'database': 'eebbkboomusers'
}

# 连接到数据库
def connect_to_db(config):
    connection = None
    try:
        connection = mysql.connector.connect(**config)
        print("Database connection was successful")
    except Error as e:
        print(f"Error: {e}")
    return connection

# 创建新用户
def create_user(connection, user):
    cursor = connection.cursor()
    query = "INSERT INTO users (qq_number, serial_number) VALUES (%s, %s)"
    cursor.execute(query, (user['qq_number'], user['serial_number']))
    connection.commit()
    print("User created successfully")

# 列出所有用户
def list_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    for user in users:
        print(user)

# 更新用户信息
def update_user(connection, user_id, new_data):
    cursor = connection.cursor()
    query = "UPDATE users SET qq_number=%s, serial_number=%s WHERE id=%s"
    cursor.execute(query, (new_data['qq_number'], new_data['serial_number'], user_id))
    connection.commit()
    print("User updated successfully")

# 删除用户
def delete_user(connection, user_id):
    cursor = connection.cursor()
    query = "DELETE FROM users WHERE id=%s"
    cursor.execute(query, (user_id,))
    connection.commit()
    print("User deleted successfully")

# 主程序
def main():
    connection = connect_to_db(config)
    
    if connection:
        while True:
            print("\n1. Create User")
            print("2. List Users")
            print("3. Update User")
            print("4. Delete User")
            print("5. Exit")
            choice = input("Enter choice: ")

            if choice == '1':
                qq_number = input("Enter QQ number: ")
                serial_number = input("Enter serial number: ")
                create_user(connection, {'qq_number': qq_number, 'serial_number': serial_number})
            elif choice == '2':
                list_users(connection)
            elif choice == '3':
                user_id = int(input("Enter user ID to update: "))
                qq_number = input("Enter new QQ number: ")
                serial_number = input("Enter new serial number: ")
                update_user(connection, user_id, {'qq_number': qq_number, 'serial_number': serial_number})
            elif choice == '4':
                user_id = int(input("Enter user ID to delete: "))
                delete_user(connection, user_id)
            elif choice == '5':
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please try again.")

        connection.close()

if __name__ == "__main__":
    main()
