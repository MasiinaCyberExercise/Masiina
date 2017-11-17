@	IN	SOA	ns1.masiina.com.	root.masiina.com. (

				3	;
				604800	;
				86400	;
				2419200	;
				604800	);

;name-servers
	IN	NS	ns1.masiina.com.

ns1.masiina.com.	IN	A	62.106.7.2
@			IN 	A 	62.106.4.2
www			IN 	A	62.106.4.2
support			IN 	A	62.106.7.3
mattermost		IN	A	62.106.8.5
