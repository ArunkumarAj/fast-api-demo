<h3>Set up routes, manage errors, utilize request and path parameters, validate data using Pydantic models, structure responses, and explore the interactive API documentation.</h3>

To Run the application, 
   `uvicorn main:app --reload`

old >> curl -X POST -H "Content-Type: application/json" 'http://127.0.0.1:8000/items?item=apple'

* POST Method ::  

   `curl -X POST -H "Content-Type: application/json" -d "{\"text\":\"apple\"}" "http://127.0.0.1:8000/items"`

* GET Method BY ID :: 

   `curl -X GET http://127.0.0.1:8000/items/3`

* GET Method BY RANGE :: 

   `curl -X GET http://127.0.0.1:8000/items?limit=4`
 
* GET Method TO GET ALL :: 

   `curl -X GET http://127.0.0.1:8000/items`

* if feel `curl` hard, go for Intractive documentaion (Swagger) :

   `http://127.0.0.1:8000/docs#` or `redoc`
