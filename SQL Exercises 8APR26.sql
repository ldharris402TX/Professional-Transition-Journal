SELECT f.title, COUNT (r.rental_id) FROM film AS f
JOIN inventory AS i ON f.film_id = i.film_id
JOIN rental AS r ON r.inventory_id = i.inventory_id
GROUP BY f.title
HAVING COUNT(r.rental_id) > 30;

#find movies that cost 4.99 to rent and have been rented more than 10xs
SELECT f.title, f.rental_rate,COUNT(r.rental_id) FROM film AS f
JOIN inventory AS i ON f.film_id = i.film_id
JOIN rental AS r ON i.inventory_id = r.inventory_id
WHERE f.rental_rate = 4.99
GROUP BY f.title,f.rental_rate
HAVING COUNT(r.rental_id) > 10;
#find G rated movies with movie counts over 20
SELECT f.title,f.rating,COUNT(r.rental_id)
FROM film AS f
JOIN inventory AS i ON f.film_id = i.film_id
JOIN rental AS r ON r.inventory_id = i.inventory_id
WHERE f.rating = 'G'
GROUP BY f.title,f.rating
HAVING COUNT(r.rental_id) > 20;
#Movie rental totals $100 >
SELECT f.title,f.film_id, SUM(p.amount) FROM film AS f
JOIN inventory AS i ON i.film_id = f.film_id
JOIN rental AS r ON r.inventory_id = i.inventory_id
JOIN payment AS p ON p.rental_id = r.rental_id
GROUP BY f.title,f.film_id
HAVING SUM(p.amount) > 100;