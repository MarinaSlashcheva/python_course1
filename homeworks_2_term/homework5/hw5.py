import sqlite3 as sq
with sq.connect('data.sqlite') as con:
    cur = con.cursor()

#1 Всю информацию о всех пользователях (все колонки в любом порядке)
    for row in cur.execute(
            'select * from Orders '
            'inner join Users on user_id = Users.id '
            'inner join GoodsInOrders on Orders.id = GoodsInOrders.order_id '
            'limit 10'):
        print(row)

#2 Количество всех пользователей (число)
    for row in cur.execute(
            'select count(id) from Users'):
        print(row[0])

#3 Количество пользователей 40 лет или старше (число). Чтобы сравнить столбец таблицы с конкретной датой можно
# использовать функцию date – where birth_date <= date(”2000-12-20”) с да-той в формате ”YYYY-MM-DD”.
    for row in cur.execute(
            'select count(*) from Users '
            'where birth_date <= date("1976-05-13")'):
        print(row[0])

#4 Страна + количество пользователей из данной страны (страна|количество)
    for row in cur.execute(
            'select country, count(*) from Users '
            'group by Users.country'):
        print(row[0], '|', row[1])

#5 Придумайте, как проверить, есть ли люди с одинаковым именем (в любом удобном формате)
    same_name = 0
    for row in cur.execute(
            'select count(*) from Users '
            'group by name'
            ):
        if row[0] != 1:
            same_name += 1
    print('yes, ', same_name, ' names not unique')


#6 Количество заказов в 2016 году (число)
    for row in cur.execute(
            'select count(*) from Orders '
            'where created like "%2016%"'):
        print(row[0])

#7 День, когда совершили наибольшее число заказов (день|число заказов)
    for row in cur.execute(
            'select strftime("%Y-%m-%d", created) as query_date, count(*) from Orders '
            'group by query_date '
            'order by count(*) desc limit 4'):
        print(row[0], '|', row[1])

#8 Процент неоплаченных заказов (число)
    for row in cur.execute(
            'select (count(id) - sum(paid)*1.0) / count(id)*100 from Orders '):
        print(row[0], ' % of orders is unpaid')

#9 Всю информацию о хлебе среди товаров. Используйте конструкцию where name like ”%bread%”
    for row in cur.execute(
            'select * from Goods '
            'where name like "%bread%"'):
        print(row)

#10 Самые 10 популярных товаров (встречаемость в GoodsInOrders) (id|name|количество)
    for row in cur.execute(
            'select good_id, Goods.name, count(good_id) from GoodsInOrders '
            'inner join Goods on good_id = Goods.id '
            'group by good_id '
            'order by count(*) desc limit 10'):
        print(row)

#11 Чистая выручка в 2016 году. Нужно учитывать только оплаченные заказы (число)
    for row in cur.execute(
            'select sum(Goods.price) from GoodsInOrders '
            'inner join Orders on order_id = Orders.id '
            'inner join Goods on good_id = Goods.id '
            'where Orders.created like "%2016%" and Orders.paid = "1"'):
        print(row[0])

#12 Самые 10 популярных товаров среди женщин (id|название)
    for row in cur.execute(
            'select good_id, Goods.name from GoodsInOrders '
            'inner join Goods on good_id = Goods.id '
            'inner join Orders on order_id = Orders.id '
            'inner join Users on Orders.user_id = Users.id '
            'where Users.gender = "F" '
            'group by good_id '
            'order by count(*) desc limit 10'
            ):
        print(row[0], '|', row[1])

#13 Пользователь, который купил больше всего килограмм (id|имя)
    for row in cur.execute(
            'select Users.id, Users.name from GoodsInOrders '
            'inner join Goods on good_id = Goods.id '
            'inner join Orders on order_id = Orders.id '
            'inner join Users on Orders.user_id = Users.id '
            'where Goods.units = "KG" and Orders.paid = "1"'
            'group by Orders.user_id '
            'order by sum(Goods.quantity) desc limit 1'
            ):
        print(row)