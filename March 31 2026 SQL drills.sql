---Ask the librarian to count every row in the film table
SELECT COUNT (*) FROM film;
---Find the biggest payment and the smallest payment
SELECT MAX(amount), MIN(amount) FROM payment;
---1. Count the payments AND find the total money spent
---2. Only for Customer #1
SELECT COUNT(amount), SUM(amount)
FROM payment
WHERE customer_id = 1;
---Ask for the average (middle) price of all rentals
SELECT AVG(amount) FROM payment;