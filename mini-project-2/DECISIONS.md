1. What is an ODM and why do we use Beanie instead of writing raw MongoDB queries?
2. What is the role of the `Database` class — why wrap Beanie methods inside it instead of calling them directly in routes?
3. What happens if `initialize_database()` is not called on startup? What would break and why?
4. What is the difference between the `Event` document and the `EventUpdate` model, and why are they two separate classes?

answers

1. An ODM is Object-Document-Mapper this a library that maps NoSQL databaases like MongoDB to the project code. Beanie is an asynchronous python ODM for mongo db it is used to increase development speed, enforce data structure, and simplify asynchronous interaction with MongoDB in Python applications making it more useful than raw MongoDB queries which are time consuming for developer as manually validation and CRUD scripts must be written and might be misleading

2. For structural purposes having them wrappped means that when creating an instance of the Database class they will be inherited

3. the code will not be connected to MongoDB so we wont have a database.Application startup will fail and we will get table errors.

4. the 'Event' document reflects database schema while EventUpdate is more of what the user can do interaction capabilities
