#Identifying all delinquent accts so the user access can be suspended

SELECT c.first_name,c.last_name,r.rental_date FROM customer AS c
INNER JOIN rental AS r
ON c.customer_id = r.customer_id
WHERE r.return_date IS NULL
ORDER BY r.rental_date ASC

#Phase 2-Cloud and Security
#AWS IAM(Identity and Access Management) lesson