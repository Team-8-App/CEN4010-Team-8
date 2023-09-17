Users can manage items in a shopping cart for immediate or future
Purchase
REST API Actions:
Retrieve the subtotal price of all items in the user’s shopping cart.
Logic: Give a user Id,return the subtotal of the books in the cart.o
o
o
o
HTTP Request Type: GET
Parameters Sent: User Id
Response Data: Calculated Subtotal
Add a book to the shopping cart.
Logic: Provided with a book Id and a User Id, add the book to theo
o
o
o
user’s shopping cart.
HTTP Request Type: POST
Parameters Sent: Book Id, User Id
Response Data: None
Retrieve the list of book(s) in the user’s shopping cart.
Logic: Give a user Id, return a list of books that are in the shoppingo
o
o
o
cart.
HTTP Request Type: GET
Parameters Sent: User Id
Response Data: List of Book Objects
Delete a book from the shopping cart instance for that user.
Logic: Given a book If and a User Id, remove the book from theo
o
o
o
user’s shopping cart.
HTTP Request Type: DELETE
Parameters Sent: Book Id, User Id
Response Data: None
