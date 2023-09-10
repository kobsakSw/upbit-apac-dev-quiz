SELECT  
	depo.member_uuid, 
    depo.currency, 
    depo.amount, 
	memberinfo.first_name, 
    memberinfo.last_name, 
    memberinfo.birthday,
	memberinfo.gender,
    memberinfo.nationality, 
	memberinfo.country_of_birth, 
    memberinfo.country_location 
FROM deposits as depo
INNER JOIN memberinfopersonal as memberinfo
ON depo.member_uuid =  memberinfo.member_uuid
WHERE depo.amount >= 50000
	/*currency in depo table has a int type, So I assume it's a currency_code but I don't know which code is THB*/
	AND depo.currency = 'THB'
ORDER BY depo_amount DESC