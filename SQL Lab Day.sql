#query to display customer name address and city using JOINs
SELECT c.last_name,c.first_name,a.address,ci.city FROM customer AS c
INNER JOIN address AS a ON c.address_id = a.address_id
INNER JOIN city AS ci ON a.city_id = ci.city_id;
#query to display customer last name using WHERE
SELECT * FROM actor
WHERE last_name = 'Wahlberg';
#queries to display math aggregates
SELECT COUNT (*) FROM customer;
SELECT SUM(amount) FROM payment;
SELECT AVG(rental_rate) FROM film;
#query to display customer name
SELECT first_name,last_name FROM customer AS c
INNER JOIN payment AS p
ON c.customer_id = p.customer_id;
#query to display customer name, payment amount and date
SELECT c.first_name,c.last_name,p.amount,p.payment_date FROM customer AS c
INNER JOIN payment AS p
ON c.customer_id = p.customer_id



