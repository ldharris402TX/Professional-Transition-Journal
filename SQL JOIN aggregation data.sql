Statement 1 (The Gap Audit):

-- Step 6: Finding films with zero rentals
SELECT f.title, r.rental_id
FROM film AS f
LEFT JOIN inventory AS i ON f.film_id = i.film_id
LEFT JOIN rental AS r ON i.inventory_id = r.inventory_id
WHERE r.rental_id IS NULL;

Statement 2 (The Volume Audit):

-- Step 7: Counting total rentals per movie
SELECT f.title, COUNT(r.rental_id)
FROM film AS f
LEFT JOIN inventory AS i ON f.film_id = i.film_id
LEFT JOIN rental AS r ON i.inventory_id = r.inventory_id
GROUP BY f.title;