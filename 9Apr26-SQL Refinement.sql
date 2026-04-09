#Identify which customers are driving revenue for the "Action" category.
#This allows a business to send targeted promotions to their highest-value fans.
SELECT c.first_name,c.last_name,SUM(p.amount) AS action_revenue
FROM customer AS c
JOIN payment AS p ON c.customer_id = p.customer_id
JOIN rental AS r ON r.rental_id = p.rental_id
JOIN inventory AS i ON i.inventory_id = r.inventory_id
JOIN film_category AS f ON f.film_id = i.film_id
JOIN category AS cat ON cat.category_id = f.category_id
WHERE cat.name = 'Action'
GROUP BY c.first_name,c.last_name
ORDER BY action_revenue DESC;
#Identify which staff member is processing the most revenue.
#In a high-stakes environment, this data helps determine resource allocation, shift scheduling,&performance bonuses.
