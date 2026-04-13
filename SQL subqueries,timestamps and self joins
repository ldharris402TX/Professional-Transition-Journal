#TO_CHAR
SELECT To_CHAR(payment_date,'DD/MM/YYYY')
FROM payment
#AGE
SELECT AGE(payment_date)
FROM payment
#EXTRACT
SELECT * EXTRACT(YEAR FROM payment_date)
FROM payment
#EXISTS with ROUNDing(using not EXISTS)
SELECT ROUND(rental_rate/replacement_cost,2)*100 AS percent_cost
FROM film
SELECT first_name, last_name FROM customer AS c
WHERE  NOT EXISTS
(SELECT * FROM payment AS p
WHERE p.customer_id = c.customer_id
AND amount > 11)
#EXISTS
SELECT first_name, last_name FROM customer AS c
WHERE EXISTS
(SELECT * FROM payment AS p
WHERE p.customer_id = c.customer_id
AND amount > 11)
#SELF JOIN-a table joined to itself
SELECT f1.title,f2.title,f1.length FROM film
AS f1
INNER JOIN film AS f2 ON
f1.film_id != f2.film_id
AND f1.length = f2.length