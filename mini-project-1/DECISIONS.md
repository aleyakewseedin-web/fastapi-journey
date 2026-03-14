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
