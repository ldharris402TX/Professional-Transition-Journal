SELECT title,rental_rate FROM film
WHERE rental_rate > (SELECT AVG(rental_rate) FROM film);

SELECT title,length FROM film WHERE length >(SELECT AVG(rental_rate)FROM film)
ORDER BY length DESC
LIMIT 20;

SELECT c.first_name,c.last_name,p.amount FROM customer AS c
INNER JOIN payment AS p ON c.customer_id = p.customer_id
WHERE p.amount > (SELECT AVG(amount)FROM payment);
