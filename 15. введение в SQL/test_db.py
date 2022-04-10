import psycopg2

data1 = {'photo': '12345', 'location_name': 'Ufa', 'description': 'capital city of Rebuplic of Bashkortostan', 'tour_price': 10000}
data2 = ['1234', 'Ufa-1', 'Capital city', 10001]


def sql_start():
    global conn, cur
    conn = psycopg2.connect(dbname='testdb', user='postgres', password='A8nDIVDh23')
    cur = conn.cursor()
    if conn:
        print('connection is ok')
    cur.execute(
        "CREATE TABLE IF NOT EXISTS traveltours (tour_id SERIAL PRIMARY KEY ,photo text, location_name text, description text, tour_price int);")
    conn.commit()

def sql_add_line(data):
    #cur.execute("insert into traveltours (photo, location_name, description, tour_price) values (%s, %s, %s, %s)", data1)
    cur.execute("insert into traveltours (photo, location_name, description, tour_price) values (%s, %s, %s, %s)", tuple(data2))
    conn.commit()

if __name__ == '__main__':
    sql_start()

    #sql_add_line(data=data1)
    sql_add_line(data=data2)
