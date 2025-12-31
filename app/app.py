from flask import Flask, request, redirect
import mysql.connector
import os
import time

app = Flask(__name__)

# Database config (from Docker env)
db_config = {
    "host": os.environ.get("DB_HOST", "db"),
    "user": os.environ.get("DB_USER", "root"),
    "password": os.environ.get("DB_PASSWORD", "root"),
    "database": os.environ.get("DB_NAME", "testdb")
}

# Retry DB connection
def get_db_connection():
    for _ in range(10):
        try:
            return mysql.connector.connect(**db_config)
        except:
            time.sleep(2)
    return None


@app.route("/", methods=["GET", "POST"])
def home():
    conn = get_db_connection()
    if not conn:
        return "<h2>Database connection failed</h2>"

    cursor = conn.cursor()

    # Handle form submission
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        role = request.form.get("role")

        if name and email and role:
            cursor.execute(
                "INSERT INTO users (name, email, role) VALUES (%s, %s, %s)",
                (name, email, role)
            )
            conn.commit()

        return redirect("/")

    # Fetch users
    cursor.execute("SELECT name, email, role FROM users;")
    users = cursor.fetchall()

    cursor.close()
    conn.close()

    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Two-Tier DevOps Web App</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background: #f4f6f8;
                margin: 0;
            }
            header {
                background: #1f2937;
                color: white;
                padding: 25px;
                text-align: center;
            }
            section {
                max-width: 900px;
                margin: 30px auto;
                background: white;
                padding: 25px;
                border-radius: 8px;
                box-shadow: 0 4px 10px rgba(0,0,0,0.1);
            }
            h2 {
                color: #1f2937;
            }
            input, button {
                width: 100%;
                padding: 10px;
                margin: 8px 0;
                border-radius: 5px;
                border: 1px solid #ccc;
            }
            button {
                background: #2563eb;
                color: white;
                border: none;
                cursor: pointer;
            }
            button:hover {
                background: #1e40af;
            }
            table {
                width: 100%;
                border-collapse: collapse;
                margin-top: 20px;
            }
            th, td {
                padding: 10px;
                border-bottom: 1px solid #ddd;
                text-align: left;
            }
            th {
                background: #e5e7eb;
            }
            footer {
                text-align: center;
                padding: 15px;
                background: #e5e7eb;
                margin-top: 40px;
            }
        </style>
    </head>
    <body>

        <header>
            <h1>Two-Tier DevOps Web Application</h1>
            <p>Flask • MySQL • Docker • Jenkins</p>
        </header>

        <section>
            <h2>📌 Project Overview</h2>
            <p>
                This application demonstrates a <b>Two-Tier Architecture</b>
                where the frontend and backend are built using Flask and data
                is persisted in a MySQL database running in a separate container.
            </p>
        </section>

        <section>
            <h2>➕ Add New User</h2>
            <form method="POST">
                <input type="text" name="name" placeholder="Full Name" required />
                <input type="email" name="email" placeholder="Email Address" required />
                <input type="text" name="role" placeholder="Role / Designation" required />
                <button type="submit">Add User</button>
            </form>
        </section>

        <section>
            <h2>👥 Users in Database</h2>
            <table>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Role</th>
                </tr>
    """

    for user in users:
        html += f"""
        <tr>
            <td>{user[0]}</td>
            <td>{user[1]}</td>
            <td>{user[2]}</td>
        </tr>
        """

    html += """
            </table>
        </section>

        <footer>
            <p>Built by Sai Ganesh | DevOps Project</p>
        </footer>

    </body>
    </html>
    """

    return html


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
