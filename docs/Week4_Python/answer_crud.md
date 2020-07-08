## CRUD practice answers
- What routes would you need to implement to provide your workout class model with this CRUD functionality and what are their corresponding HTTP verbs?

    - Create
    - **Route:** POST/classes
    - **Effect on Database:** Adds the class provided in the request body to the database
    - **Response Body:** `{"class": The Newly-Created Class}`
    - **Success Response Code:** 201
   
- What effect would each route have on the database?

    - Read (All Classes)
    - **Route:** GET/classes
    - **Effect on Database:** None
    - **Response Body:** `{"classes": [Array of All Saved Classes]}`
    - **Success Response Code:** 200
    
- What response body would each route return?
    
    - Read(One Class)
    - **Route:** GET/classes/:id
    - **Effect on Database:** None
    - **Response Body:** `{"class": The class with the specified ID}`
    - **Success Response Code:** 200
    
- What response code would each route return?

    - Update
    - **Route:** PUT/classes/:id
    - **Effect on Database:** Updates class with specified ID to have class information provided in the request body
    - **Response Body:** `{"class": The updated class is now saved in the database}`
    - **Success Response Code:** 200
    
    