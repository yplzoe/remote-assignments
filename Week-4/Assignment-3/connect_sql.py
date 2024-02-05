import pymysql.cursors

# for database


def add_to_db(email, pwd):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='password',
                         database='assignment',)
    with db:
        with db.cursor() as cursor:
            sql = "INSERT INTO `user` (`email`, `password`) VALUES (%s, %s)"
            cursor.execute(sql, (email, pwd))
        db.commit()


def check_db(email, pwd):
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='password',
                         database='assignment',)
    all_correct = False
    exist_email = False
    with db:
        with db.cursor() as cursor:
            sql = "SELECT * FROM `user` WHERE `email`=%s"
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            print(result)
            print(type(result))
            if result != None:
                exist_email = True
                if result[2] == pwd:
                    all_correct = True

    return all_correct, exist_email, result


def delete_all():
    db = pymysql.connect(host='localhost',
                         user='root',
                         password='password',
                         database='assignment',)
    with db:
        with db.cursor() as cursor:
            sql = "DELETE FROM `user`"
            cursor.execute(sql)
        db.commit()
