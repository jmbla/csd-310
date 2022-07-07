import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "Joefarm123!",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    cursor = db.cursor()

    cursor.execute("INSERT INTO player (player_id, first_name, last_name, team_id) VALUES(21, 'Smeagol', 'Shire Folk', 1);")

    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name  = 'Smeagol';")

    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum';")

    cursor.execute("SELECT player_id, first_name, last_name, team.team_name FROM team INNER JOIN player ON team.team_id = player.team_id;")

    players = cursor.fetchall()

    print("-- DISPLAYING PLAYERS AFTER DELETE --")
    for player in players:
        print("Player ID: {} \nFirst Name: {} \nLast Name: {} \nTeam Name: {}".format(player[0], player[1], player[2], player[3]))
        print()

    input("\n\n Press any key to continue...\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("    The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")
        
    else:
        print(err)

finally:
    db.close()



