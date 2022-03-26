# Simple-CRUD-L1-P1_Django
Create Simple CRUD App in Django - Level 1 - Project 1


Create Simple CRUD with the below fields:
- First name
- Last name
- Email
- Password
- Confirm password

Functionalities and Conditions:
- First name, Email, Password and Confirm password fields are required.
- Email address must be unique.
- Stored password must be encrypted when stored in DB.
- When account gets created we need to send an email to created account to verify email. User will click on link given in email and account will be verified.
- When edit account detail and email changed than account status should marked as pending verification too.
- List users should be in HTML table with pagination.
- List users page should show Full Name, Email and Status ( Verified/Pending ) and edit,delete button.
- When click on delete button than that specific account should be deleted from DB.
