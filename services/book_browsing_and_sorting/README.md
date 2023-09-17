Users will have a simple and enjoyable way to discover new books and
Authors and sort results.

**REST API Actions:**

- **Retrieve List of Books by Genre**

  - Logic: Given a specific genre, return a list of books for that genre.o
  - HTTP Request Type: GET
  - Parameters Sent: Genre
  - Response Data: JSON List of book objects

- **Retrieve List of Top Sellers (Top 10 books that have sold the most copied)**

  - Logic: Return the top 10 books that have sold the most copies ino
  - descending order (most copies sold would be #1)
  - HTTP Request Type: GET
  - Parameters Sent: None
  - Response Data : JSON List of book objects

- **Retrieve List of Books for a particular rating and higher**

  - Logic: Filter by rating higher or equal to the passed rating value.o
  - HTTP Request Type: GET
  - Parameters Sent: Rating
  - Response Data: JSON List of book objects

- **Discount books by publisher.**
  - Logic: Update the price of all books under a publisher by a discount percent.
  - HTTP Request Type: PUT or PATCH
  - Parameters Sent: Discount percent, Publisher
  - Response Data: None
