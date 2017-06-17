.read data.sql

-- Q1
create table flight_costs as
  with Nov(day, cur, prev) as (
    select 1, 20, 0 union
    select 2, 30, 20 union
    select 3, 40, 30 union
    select day + 1, (cur + prev) / 2 + 5 * ((day + 1) % 7), cur from Nov
    where day < 25 and day > 2
  )
  select day as day, cur as price from Nov;

-- Q2
create table schedule as
  with trips(path, ending, flights, cost) as (
    select departure || ", " || arrival, arrival, 1, price from flights
     where departure = "SFO" union
    select path || ", " || arrival, arrival, flights + 1, cost + price
        from trips, flights
            where ending = departure and flights < 2
  )
  select path, cost from trips where ending = "PDX" order by cost;

-- Q3
create table shopping_cart as
  with lists(items, last, budget) as (
    select item, price, 60 -price from supermarket where price <= 60 union
    select items || ", " || item, price, budget - price
        from lists, supermarket
            where price <= budget AND price >= last
  )
  select items, budget from lists order by budget, items;

-- Q4
create table number_of_options as
  select count(distinct meat) from main_course;

-- Q5
create table calories as
  select count(*) from main_course as m, pies as p
    where m.calories + p.calories < 2500;

-- Q6
create table healthiest_meats as
  select meat, min(m.calories + p.calories) as calories
    from main_course as m, pies as p 
        group by meat having max(m.calories + p.calories) < 3000;

-- Q7
create table average_prices as
  select category, avg(MSRP) from products group by category;

-- Q8
create table lowest_prices as
  select name, store, price from inventory, products where name = item
  group by name having min(price);

-- Q9
create table shopping_list as
  select l.name, store from products as p, lowest_prices as l
  where l.name = p.name
  group by category having min(MSRP/rating);

-- Q10
create table total_bandwidth as
  select sum(Mbs) from shopping_list as s, stores as t
  where s.store = t.store;
