from pymysql import connect

conn = connect(host='localhost', port=3309, user='root', passwd='Password123', db='games', autocommit=True)
cursor = conn.cursor()


def add_score(difficulty):
    try:
        cursor.execute("SELECT * FROM users_scores")
        record = cursor.fetchone()
        cursor.execute("UPDATE users_scores SET score = (%s + (%s * 3) + 5);" % (int(record[0]), difficulty))

    except:
        cursor.execute("INSERT INTO users_scores VALUES ('%s');" % ((difficulty * 3) + 5))

    cursor.close()



