import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='wcwimj6zu5aaddlj.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                user='l9jm464uotxemvah',
                                password='ai0hxuatg2iac0vk',
                                database='lxbh8lw5gf995ay8',
                                cursorclass=pymysql.cursors.DictCursor)

def insertnewusername():
    username = input('username : ')
    with connection:
        with connection.cursor() as cursor:
            sqlcheckusername = "SELECT `username` FROM `botfishing` WHERE `username`=%s"
            cursor.execute(sqlcheckusername, username)
            resultusername = cursor.fetchone()
            # print(result)
            if resultusername == None:
                print("Not Have user")
                password = input('password : ')
                hwid = input('hwid : ')
                sqlcheckhwid = "SELECT `HWID` FROM `botfishing` WHERE `HWID`=%s"
                cursor.execute(sqlcheckhwid, hwid)
                resulthwid = cursor.fetchone()
                if resulthwid == None:
                    print("Not Have hwid")
                    expyear = input('expyear : ')
                    expmonth = input('expmonth : ')
                    expday = input('expday : ')
                    exphours = input('exphours : ')
                    permission = input('permission : ')
                    exp = str({'Year':expyear, 'Month':expmonth, 'Day':expday, 'Hours':exphours})
                    sql = "INSERT INTO `botfishing` (`username`, `password`, `HWID`, `EXP`, `permission`) VALUES (%s, %s, %s, %s, %s)"
                    cursor.execute(sql, (username, password, hwid, exp, permission))
                    print('insert data sucess')
                else:
                    print("Have hwid")
            else:
                print("Have user")

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        connection.commit()


insertnewusername()