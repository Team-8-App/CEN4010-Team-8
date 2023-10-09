Users can see informative and enticing details about a book

**REST API Actions:**

- An administrator must be able to create a book with the book ISBN, book name, book description, price, author, genre, publisher , year published and copies sold.

  - Logic: Given a Book’s info, add it to the system.o
  - HTTP Request Type: POST
  - Parameters Sent: Book Object
  - Response Data: None

- Must be able retrieve a book’s details by the ISBN :check:

  - Logic: Given a book id, retrieve the book informationo
  - HTTP Request Type: GET
  - Parameters Sent: Book Id
  - Response Data: Book object JSON

- An administrator must be able to create an author with first name, last name, biography and publisher

  - Logic: Given an Author’s Info, add it to the system.o
  - HTTP Request Type: POST
  - Parameters Sent: Author Object
  - Response Data: None

- Must be able to retrieve a list of books associated with an author :check:
  - Logic: Given an Author’s Id, return the list of books for that author.o
  - HTTP Request Type: GET
  - Parameters Sent: Author Id
  - Response Data: JSON list of Book Objects
