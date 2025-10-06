import sqlite3

def save_token(token_data):
    conn = sqlite3.connect("aurum.db")
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tokens (access_token, refresh_token) VALUES (?, ?)", 
                   (token_data["access_token"], token_data["refresh_token"]))
    conn.commit()
    conn.close()
