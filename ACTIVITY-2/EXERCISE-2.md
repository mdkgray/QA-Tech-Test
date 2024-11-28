# Swagger Petstore

## TEST PLANS

**Pet**
---
- GET
    - `/pet/{petId}`
        - Should be able to GET a pet by a valid ID
        - Should be able to GET the correct pet using the petId
        - Should be able to return a response code of 200 when a valid `petId` is used
        - Should not be able to GET the incorrect pet using the petId
        - Should not be able to GET a pet with an invalid ID
        - Should be able to return a response code of 404 when an invalid `petId` is used
        - Should not be able to GET a pet with a missing ID
        - Should be able to return a response code of 400 when the `petId` is empty or `null`    

    - `/pet/findByStatus`
        - Should be able to GET pets by valid status
        - Should be able to return a response code of 200 with the list of pets matching the status 
        - Should not be able to GET pets with an invalid status
        - Should be able to return a response code of 400 when an invalid status is used   
        - Should be able to GET pets with the status defined in the request
        - Should not be able to GET pets with a status different to the status defined in the request

- PUT
    - `/pet`
        - Should be able to update an existing pet with valid data
        - Should be able to return a response code of 200 when an existing pet has been updated 
        - Should not be able to update a pet with invalid data
        - Should be able to return a response code of 400 when invalid or malformed JSON is used
        - Should not be able to update a non-existent pet
        - Should be able to return a response code of 404 when valid JSON is used with a non-existent `id`

- POST
    - `/pet`
        - Should be able to add a new pet with valid data
        - Should be able to return a response code of 200 with the created pet details 
        - Should not be able to add a pet with invalid data
        - Should be able to return a response code of 400 when invalid or malformed JSON is used
        - Should not be able to add a pet without mandatory fields
        - Should be able to return a response code of 400 when required fields are missing (e.g. id, name)

    - `/pet/{petId}`
        - Should be able to update a pet partially using valid ID and data
        - Should be able to return a response code of 200 with the updated pet details 
        - Should not be able to update a pet with an invalid ID
        - Should be able to return a response code of 404 when when invalid pet ID and/or partial data is requested 
        - Should not be able to update a pet with invalid data
        - Should be able to return a response code of 400 when a valid pet ID is used with invalid or malformed JSON
        - Should not be able to update a pet with missing fields
        - Should be able to return a response code of 400 when a valid pet ID is used with incomplete data payload 
        - Should handle unauthorised access when updating a pet
        - Should be able to return a response of 403 when a valid pet ID and data is used with an unauthorised token 

    - `/pet/{petId}/uploadImage`
        - Should be able to upload an image for a valid pet ID
        - Should be able to return a response code of 200 with image upload confirmation
        - Should not be able to upload an image for an invalid pet ID
        - Should be able to return a response code of 404 when an image is uploaded for an invalid pet ID
        - Should not be able to upload an image without a file
        - Should be able to return a response code of 400 when a missing file is uploaded using a valid pet ID

- DELETE
    - `/pet/{petId}`
        - Should be able to delete a pet by a valid ID
        - Should be able to return a response code of 200 when a valid pet ID is used to delete a pet
        - Should not be able to delete a pet with an invalid ID
        - Should be able to return a response code of 404 when an invalid pet ID is used 
        - Should not be able to delete a pet with a missing ID
        - Should be able to return a response code of 400 when an empty or `null` pet ID is used 
        - Should not be able to delete a pet with unauthorised access
        - Should be able to return a response of 403 when a valid pet ID and data is used with an unauthorised token 

**Store**
---
- GET 
    - `/store/inventory`
        - Should be able to GET inventory successfully
        - Should be able to return a response code of 200 with inventory details 
    
    - `/store/order/{orderId}`
        - Should be able to retrieve an order by a valid ID
        - Should be able to return a response code of 200 with correct order details when a valid order ID is used 
        - Should not be able to retrieve an order with an invalid ID
        - Should be able to return a response code of 404 when an invalid order ID is used 
        - Should not be able to retrieve an order with a missing ID
        - Should be able to return a response of 400 when an empty or `null` order ID is used 

- POST
    - `/store/order`
        - Should be able to place a new order with valid data
        - Should be able to return a response code of 200 with created order details 
        - Should not be able to place an order with invalid data
        - Should be able to return a response code of 400 when the request contains invalid or malformed JSON
        - Should not be able to place an order without mandatory fields
        - Should be able to return a response of 400 when the request contains missing required fields

- DELETE
    - `/store/order/{orderId}`
        - Should be able to delete an order by a valid ID
        - Should be able to return a response code of 200 when a valid order ID is used to delete an order
        - Should not be able to delete an order with an invalid ID
        - Should be able to return a response code of 404 when the request contains an invalid order ID
        - Should not be able to delete an order with a missing ID
        - Should be able to return a response code of 400 when the request contains an empty or `null` order ID

**User**
---
- GET
    - `/user/{username}`
        - Should be able to retrieve a user by valid username
        - Should be able to return a response code of 200 when the request contains a valid username 
        - Should not be able to retrieve a user with an invalid username
        - Should be able to return a response code of 404 when the request contains an invalid username
        - Should not be able to retrieve a user with a missing username
        - Should be able to return a response code of 400 when the request contains an empty or `null` username

    - `/user/login`
        - Should be able to log in with valid credentials
        - Should be able to return a response code of 200 when the request contains a valid username and password as query parameters 
        - Should not be able to log in with invalid credentials
        - Should be able to return a response code of 400 when the request contains invalid username or password
        - Should not be able to log in with missing credentials
        - Should be able to return a response code of 400 when the request contains a missing username or password

    - `/user/logout`
        - Should be able to log out successfully
        - Should be able to return a response code of 200 when the user logs out

- PUT
    - `/user/{username}`
        - Should be able to update a user with valid data
        - Should be able to return a response code of 200 when the user has been updated 
        - Should not be able to update a user with invalid data
        - Should be able to return a response code of 400 when the request contains a valid username but invalid or malformed JSON
        - Should not be able to update a user with an invalid username
        - Should be able to return a response code of 404 when the request contains an invalid username 
        - Should not be able to update a user without mandatory fields
        - Should be able to return a response of 400 when the request contains missing required fields

- POST
    - `/user`
        - Should be able to create a new user with valid data
        - Should be able to return a response code of 200 with created user details 
        - Should not be able to create a user with invalid data
        - Should be able to return a response code of 400 when the request contains invalid or malformed JSON
        - Should not be able to create a user without mandatory fields
        - Should be able to return a response of 400 when the request contains missing required fields

    - `/user/createWithArray`
        - Should be able to create multiple users with valid array data
        - Should be able to return a response code of 200 when request contains a valid array of user objects 
        - Should not be able to create users with invalid array data
        - Should be able to return a response code of 400 when the request contains invalid or malformed JSON array
        - Should not be able to create users without mandatory fields in the array
        - Should be able to return a response code of 400 when the request containing the array contains missing field/s in one or more user objects in the array 

    - `/user/createWithList`
        - Should be able to create multiple users with valid list data
        - Should be able to return a response code of 200 when request contains a valid list of user objects 
        - Should not be able to create users with invalid list data
        - Should be able to return a response code of 400 when the request contains invalid or malformed JSON list
        - Should not be able to create users without mandatory fields in the list
        - Should be able to return a response code of 400 when the request containing the list contains missing field/s in one or more user objects in the list

- DELETE
    - `/user/{username}`
        - Should be able to delete a user by valid username
        - Should be able to return a response code of 200 when a valid username is used to delete a user
        - Should not be able to delete a user with an invalid username
        - Should be able to return a response code of 404 when the request contains an invalid username
        - Should not be able to delete a user with a missing username
        - Should be able to return a response code of 400 when the request contains an empty or `null` username
