Users can create and have 3 different wish lists which can have books moved to
REST API Actions:
Must be able to create a wishlist of books that belongs to user and has a
unique name
Logic: Given a user Id and a wish list name, create the wishlist.o
o
o
o
HTTP Request Type: POST
Parameters Sent: Wish list name, User Id
Response Data: None
Must be able to add a book to a user’s wishlisht
Logic: Given a book Id and a wish list Id, add the book to that wisho
o
o
o
list.
HTTP Request Type: POST
Parameters Sent: Book Id, Wishlist Id
Response Data: None
Must be able to remove a book from a user’s wishlist into the user’s
shopping cart
Logic: : Given a book Id and a wish list Id, remove the book to thato
o
o
o
wish list.
HTTP Request Type: DELETE
Parameters Sent: Book Id, Wishlist Id
Response Data: None
Must be able to list the book’s in a user’s wishlist
Logic: Given a wishlist Id, return a list of the books in that wishlist.o
o
o
o
HTTP Request Type: GET
Parameters Sent: Wishlist Id
Response Data: JSON LIST of books in the user’s wishlist.
