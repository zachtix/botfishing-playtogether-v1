import pymysql.cursors
try:
    connection = pymysql.connect(host='wcwimj6zu5aaddlj.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                user='l9jm464uotxemvah',
                                password='ai0hxuatg2iac0vk',
                                database='lxbh8lw5gf995ay8',
                                cursorclass=pymysql.cursors.DictCursor)
    with connection:

        with connection.cursor() as cursor:
            year = '2021'
            month = '06'
            day = '22'
            hours = '10'
            # sql = ('SELECT TIMESTAMPDIFF(HOUR,'2021-06-21 20:00:00','?-?-? ?:00:00') timediff', ('2021', '06', '22', '10'))
            sql = ("SELECT TIMESTAMPDIFF(HOUR,'2021-06-21 20:00:00','?-?-? ?:00:00')", (year, month, day, hours,))
            # cursor.execute("SELECT TIMESTAMPDIFF(HOUR,'2021-06-21 20:00:00','2021-06-22 20:00:00') timediff")
            cursor.execute(sql)
            result = cursor.fetchone()
            # print(result)
            # print(type(result))
            timediff = result['timediff']
            print(timediff)

except pymysql.Error:
    print("error")

