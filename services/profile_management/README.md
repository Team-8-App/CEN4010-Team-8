Users can create and maintain their profiles rather than enter in
their information each time they order
REST API Actions:
Create a User with username, password and optional fields (name, email
address, home address)
Logic: Provided the user fields, create the user in the database..o
o
o
o
HTTP Request Type: POST
Parameters Sent: User Object
Response Data: None
Retrieve a User Object and its fields by their username
Logic: Given a specific username, retrieve the user details.o
o
o
o
HTTP Request Type: GET
Parameters Sent: Username
Response Data: JSON User object.
Update the user and any of their fields except for mail
Logic: Given the username as a key lookup value and any other usero
o
o
o
field, update that user field with the new param value.
HTTP Request Type: PUT / PATCH
Parameters Sent: Username
Response Data: None
Create Credit Card that belongs to a User
Logic: Given a user name and credit card details, create a credito
o
o
o
card for that user.
HTTP Request Type: POST
Parameters Sent: User name, Credit Card Object
Response Data: None
