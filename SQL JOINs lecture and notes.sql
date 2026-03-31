INNER JOINs
SELECT * FROM payment
INNER JOIN customer
ON payment.customer_id = customer.customer_id

OUTER JOIN
SELECT film.film_id,title,inventory_id,store_id
FROM film
LEFT JOIN inventory ON inventory.film_id = film.film_id

SELECT title,first_name,last_name
FROM film_actor INNER JOIN actor ON film_actor.actor_id = actor.actor_id
INNER JOIN film ON film_actor.film_id = film.film_id
WHERE first_name = 'Nick' AND last_name = 'Wahlberg'