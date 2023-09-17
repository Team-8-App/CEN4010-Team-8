Users can rate AND comment on books they’ve purchased to help others in their
selection
REST API Actions:
Must be able to create a rating for a book by a user on a 5 star scale with a
datestamp
Logic: Create a rating for a book given by a user.o
o
o
o
HTTP Request Type: POST
Parameters Sent: Rating, User Id, Book Id
Response Data: None
Must be able to create a comment for a book by a user with a datestamp
Logic: Create a comment for a book given by a user.o
o
o
o
HTTP Request Type: POST
Parameters Sent: Comment, User Id, Book Id
Response Data: None
Must be able to retrieve a list of all comments for a particular book.
Logic: Retrieve a list of comments for the booko
o
o
o
HTTP Request Type: GET
Parameters Sent: Book Id
Response Data: JSON list of comments
Must be able to retrieve the average rating for a book
Logic: Given a book Id, calculate the average rating as a decimal.
o HTTP Request Type: GET
o Parameters Sent: Book Id
o Response Data: Computed Average rating (decimal)
