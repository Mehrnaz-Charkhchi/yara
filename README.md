This script will post an API call and the API will insert the formated JSON in to Django database.
---
API sample:
http://yourdomain.com/api/purchase/

JSON Sample:
```json

{
	"datetime": "2015-08-06T19:37:14.000Z",
	"email": "tester@test.com",
	"address": "lilililililiiii",
	"phone": "7777",
	"purchase": "Bag",
	"purchase_id": "13",
	"name": "mehrnaz",
	"user_id": "200"
}
```

http://yourdomain.com/api/purchase/[Record_ID]

