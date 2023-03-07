# Receipt_Processor
I have implemented this challenge in python using Flask framework.


# Installing & Running the project

You need to have Docker installed in your system. 
Build Docker image by running below commands in the root directory of the project.

`docker build -t flask .`

`docker run -p 5000:5000 flask`

The service should now be running at http://localhost:5000/. 


# API Calls


METHOD  | API | Description   | Request Payload   | Response  | 
--------|---- | ------------  |------------|-----------|
POST  |localhost:5000/receipts/process| Create id and calculate points for receipt | {"retailer": "Target","purchaseDate": "2022-01-01","purchaseTime": "13:01","items": [{"shortDescription": "Mountain Dew 12PK","price": "6.49"}],"total": "35.35"} | { 'id' : #system generate unique id# } |
GET  |localhost:5000/receipts/<receipt_id>/points| Displays points awarded for given receipt id| null | { "points": #calculated points# }|


# Error Handling

**/receipts/process**
- All the parameters (retailer/purchaseDate/purchaseTime/items/total/short description/price) should have values & each value will be evaluated               with validation rules. 
- If the request payload is in incorrect format, end user gets a 422 RESPONSE along with error message specifying which fields are incorrect.


 **/receipts/<receipt_id>/points**
- receipt_id should not be empty.Passing an empty values results in 400 RESPONSE along with error message stating "Receipt Id cannot be empty".
- If the receipt id is not there in the in_memory database, end user gets 404 RESPONSE along with error message stating "Receipt ID Invalid".

# Testing

The API calls can be tested by sending requests to the endpoints mentioned in the specification using PostmanAPI.

I have also create unit test which can be run using the below command from the root directory of the project. Ensure that flask application is running in the background.

`python test_cases.py`


        

        
        
        
