### Conceptual Exercise

Answer the following questions below:

- What is RESTful routing?
It is a naming pattern using HTTP verbs like GET, POST, PATCH, DELETE

- What is a resource?
It usually comes after the base api. Often things we created Models for.
If it similar to an object in an OOP language. A resource is an object with a type, associated data, and a relationship to other resources. The standard methods on the resource are the HTTP verbs.

- When building a JSON API why do you not include routes to render a form that when submitted creates a new user?
Because it will then allow anyone to submit the form.
When creating an API you are not returning the HTML for the form. You are simply taking in the data provided by the front end, making the user, and then sending back JSON. It is the job of the front end to do send the right data however it pleases (through a form generated on the front end, ajax, etc.).

- What does idempotent mean? Which HTTP verbs are idempotent?
It refers to the some function like an HTTP route that can be requested multiple times with 
the same result.
GET, PUT/PATCH, and DELETE are idempotent.

- What is the difference between PUT and PATCH?
PUT modifies and updates the entire resource. PATCH just applies to the data you want to update.

- What is one way encryption?
Takes some input and it maps it into some output of a fixed size. It is impossible to reverse.

- What is the purpose of a `salt` when hashing a password?
Adds random data into a hash function to make it harder to reverse or guess the password.

- What is the purpose of the Bcrypt module?
It is a password hashing function.

- What is the difference between authorization and authentication?
Authentication is being able to verify that someone is who they say they are. Authorization gives
permission.
