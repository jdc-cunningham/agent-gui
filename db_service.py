import sqlite3

class Database:
    def __init__(self):
        self.con = sqlite3.connect("agent_gui.db", check_same_thread=False)
        self.init_agents_table()

    def get_con(self):
        return self.con

    def get_cursor(self):
        return self.con.cursor()

    def init_agents_table(self):
        cur = self.get_cursor()
        table_exists = False

        try:
            table_exists = cur.execute("SELECT * FROM agents")
        except Exception:
            print("Error: DB agents Exists")

        if not(table_exists):
            try:
                cur.execute("CREATE TABLE agents(name, model_name, prompt, tools, created, last_used)")
            except Exception:
                print("Failed to create agents table")

    def add_agent(
        self,
        name,
        model_name,
        prompt,
        tools, # comma-separated list of fcn names
        created,
        last_used
    ):
        con = self.get_con()
        cur = self.get_cursor()

        try:
            cur.execute(
                "INSERT INTO agents VALUES(?, ?, ?, ?, ?, ?)",
                [name, model_name, prompt, tools, created, last_used]
            )

            con.commit()
        except sqlite3.Error as e:
            print("Row insert failed for agents")
            print(e)

    def get_agents(self):
        con = self.get_con()
        cur = self.get_cursor()

        try:
            agents = cur.execute("SELECT * FROM agents")
            return agents.fetchall()
        except sqlite3.Error as e:
            print("Row insert failed for agents")
            print(e)

    def delete_agent(self, agent_name):
        con = self.get_con()
        cur = self.get_cursor()

        try:
            cur.execute(
                "DELETE FROM agents WHERE name = ?",
                [agent_name]
            )

            con.commit()
        except sqlite3.Error as e:
            print(f"Failed to delete agent {agent_name}")
            print(e)
