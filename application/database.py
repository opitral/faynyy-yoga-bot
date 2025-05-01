from datetime import datetime
import sqlite3
from typing import Optional
from openpyxl import Workbook


class UserDatabase:
    def __init__(self, db_path: str = "resources/users.db"):
        self.connection = sqlite3.connect(db_path)
        self.connection.row_factory = sqlite3.Row
        self.create_table()

    def create_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS Users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_id INTEGER NOT NULL UNIQUE,
            first_name TEXT,
            last_name TEXT,
            username TEXT,
            started_practice BOOLEAN DEFAULT 0,
            wants_group BOOLEAN DEFAULT 0,
            wants_individually BOOLEAN DEFAULT 0,
            next_notification_index INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        );
        """
        self.connection.execute(query)
        self.connection.commit()

    def add_user(self, telegram_id: int,
                 first_name: Optional[str],
                 last_name: Optional[str],
                 username: Optional[str]):
        query = """INSERT INTO Users (telegram_id, first_name, last_name, username) VALUES (?, ?, ?, ?); """
        self.connection.execute(query, (telegram_id, first_name, last_name, username))
        self.connection.commit()

    def update_user_field(self, telegram_id: int, field: str, value):
        if field not in ["started_practice", "wants_group", "wants_individually", "next_notification_index"]:
            raise ValueError("Invalid field name")
        query = f"UPDATE Users SET {field} = ? WHERE telegram_id = ?"
        self.connection.execute(query, (value, telegram_id))
        self.connection.commit()

    def get_user(self, telegram_id: int) -> Optional[sqlite3.Row]:
        query = "SELECT * FROM Users WHERE telegram_id = ?"
        cursor = self.connection.execute(query, (telegram_id,))
        return cursor.fetchone()

    def get_all_users(self) -> list[sqlite3.Row]:
        query = "SELECT * FROM Users"
        cursor = self.connection.execute(query)
        return cursor.fetchall()

    def export_to_xlsx(self) -> str:
        rows = self.get_all_users()

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Users"
        headers = ["Ідентифікатор в системі", "Телеграм ID", "Ім'я", "Прізвище", "Псивдонім",
                   "Чи розпочав приактику?", "Чи хоче в міні-групу?", "Чи хоче індивідуально?", "Дата реєстрації"]
        sheet.append(headers)

        if rows:
            for row in rows:
                sheet.append([
                    row["id"],
                    row["telegram_id"],
                    row["first_name"],
                    row["last_name"],
                    row["username"],
                    "Так" if row["started_practice"] else "Ні",
                    "Так" if row["wants_group"] else "Ні",
                    "Так" if row["wants_individually"] else "Ні",
                    row["created_at"]
                ])

        file_path = "resources/exports/" + datetime.now().strftime("users_export_%Y-%m-%d_%H-%M-%S.xlsx")
        workbook.save(file_path)
        return file_path

    def get_all_users_with_notifications(self) -> list[sqlite3.Row]:
        query = "SELECT * FROM Users WHERE next_notification_index <= 19"
        cursor = self.connection.execute(query)
        return cursor.fetchall()

    def close(self):
        self.connection.close()
