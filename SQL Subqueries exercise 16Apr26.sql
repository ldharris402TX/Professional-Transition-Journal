SELECT c.first_name,c.last_name,SUM(p.amount) FROM customer AS c
INNER JOIN payment as p
ON c.customer_id = p.customer_id
GROUP BY c.first_name,c.last_name
HAVING SUM(p.amount) > 150
ORDER BY SUM(p.amount) DESC;

SELECT c.first_name,c.last_name,SUM(p.amount) FROM customer AS c
INNER JOIN payment as p
ON c.customer_id = p.customer_id
WHERE p.amount > (SELECT AVG(amount) FROM payment)
GROUP BY c.first_name,c.last_name
ORDER BY SUM(p.amount) DESC;