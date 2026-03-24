- Why did you choose each Pydantic field type?
- What does each validation rule protect against?
- Which endpoint uses `async` in a meaningful way, and why?

for the enrollment model

- course name has to be a string to ensure that user only enters name or course code
- for semester it must be one of the three seasons fall,summer,or winter therefore to validate that only one of these is entered we used enum for validations and created a class and object of this class is passed to semester
- for the grade i ensured that it is only between certain values (0<=grade<=100)
  and a model validator is set to ensure that if student does not pass 50 they repeat as
- the instructor name is not important so i set to optional

the put endpoint uses 'async' in a useful way as the update of the infromation of one student will not affect other operations like adding a new course to that student or deleting another student's info or posting a new student

1. What is `@contextmanager` and why do we use it instead of a plain function here?
2. What does `check_same_thread=False` do and why is it necessary in a FastAPI application?
3. What happens to your data when the server restarts — with the old list vs. with SQLite?

1-It's a decorator from contextlib that turns a generator function into a context manager usable with "with". The generator yields exactly once: code before yield is setup, yield returns the resource, and code after yield is teardown/cleanup (runs even on exceptions).
We use it instead of a plain function when we need deterministic setup and cleanup around a resource (open/close connections, begin/commit/rollback transactions, lock acquire/release). It makes caller code concise and ensures proper cleanup on errors.

2-SQLite’s Python driver (sqlite3) by default enforces that a Connection object is only used in the same OS thread that created it. Setting check_same_thread=False disables that check so the connection can be used from different threads.
Why needed in FastAPI: FastAPIservers handle requests concurrently . If you create a single sqlite3.Connection at startup and then use it across request-handling threads, you must disable the same-thread check or else sqlite3 will raise an error.

3-Old list (in-memory Python list): lives only in process memory. When the server restarts, that list and all its contents are lost.
SQLite (file-based): persistent. If you use a file-based SQLite DB (e.g., "data.db") and commit your transactions, the data is written to disk and survives server restarts.
