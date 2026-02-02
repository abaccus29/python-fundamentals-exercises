
# ---------- CLASSES & OBJECTS ----------

# 1. Create a class called User with attributes name and email.
# 2. Create two objects from the User class and print their details.
# 3. Add a method greet() to the User class that prints a welcome message.
# 4. Create a class called Car with attributes brand and year.
# 5. Instantiate a Car object and print its brand.

# ---------- CONSTRUCTORS (__init__) ----------

# 6. Create a class Person that takes name and age in the constructor.
# 7. Create an object of Person and print the age.
# 8. Modify the Person class to include a method introduce().
# 9. Create a class Book with title and author passed to __init__.
# 10. Print book details using a method.

# ---------- INSTANCE METHODS ----------

# 11. Create a class Calculator with add() and subtract() methods.
# 12. Create an object and call both methods.
# 13. Create a class Student with a method that checks if the student passed.
# 14. Create a class Circle with a method to calculate area.
# 15. Call the area method using an object.

# ---------- ATTRIBUTES ----------

# 16. Create a class Account with balance attribute.
# 17. Update the balance using a deposit method.
# 18. Prevent withdrawing more than the balance.
# 19. Print the updated balance.
# 20. Create multiple Account objects with different balances.

# ---------- ENCAPSULATION ----------

# 21. Make the balance attribute private.
# 22. Create a getter method to access balance.
# 23. Create a setter method to update balance safely.
# 24. Try accessing the private variable directly (observe behavior).
# 25. Explain why encapsulation is important (comment).

# ---------- CLASS VARIABLES ----------

# 26. Create a class Employee with a company name as class variable.
# 27. Access the class variable using an object.
# 28. Change the class variable and observe effect.
# 29. Count how many Employee objects are created.
# 30. Print total employee count.

# ---------- INHERITANCE ----------

# 31. Create a base class Animal with a speak() method.
# 32. Create Dog and Cat classes that inherit from Animal.
# 33. Override the speak() method in Dog.
# 34. Call speak() on different animal objects.
# 35. Add a new method only to Dog.

# ---------- POLYMORPHISM ----------

# 36. Create multiple classes with the same method name.
# 37. Loop through objects and call the same method.
# 38. Observe different outputs.
# 39. Explain polymorphism in your own words (comment).
# 40. Demonstrate polymorphism using inheritance.

# ---------- REAL-WORLD PRACTICE ----------

# 41. Create a BankAccount class with deposit and withdraw.
# 42. Prevent invalid withdrawals.
# 43. Create a SavingsAccount that inherits BankAccount.
# 44. Add interest calculation to SavingsAccount.
# 45. Test both account types.

# ---------- ADVANCED BASICS ----------

# 46. Use __str__ to print object details nicely.
# 47. Compare two objects using their attributes.
# 48. Store multiple objects in a list.
# 49. Loop through the list and call a method.
# 50. Refactor one previous exercise to improve design.



# ================= MINI PROJECT 1 =================
# PROJECT: USER MANAGEMENT SYSTEM
# 1. Create a User class with id, name, and email.
# 2. Add login() and logout() methods.
# 3. Create an Admin class that inherits User.
# 4. Allow Admin to deactivate users.
# 5. Store multiple users in a list.
# 6. Add a method to find a user by email.
# 7. Prevent duplicate users.
# 8. Use encapsulation to protect user data.
# 9. Print all active users.
# 10. Add __str__ method to display user info.

# ================= MINI PROJECT 2 =================
# PROJECT: BANKING SYSTEM
# 1. Create a BankAccount class with account_number and balance.
# 2. Add deposit() and withdraw() methods.
# 3. Prevent negative deposits.
# 4. Prevent overdraft withdrawals.
# 5. Create a SavingsAccount class with interest rate.
# 6. Override withdraw() with additional rules.
# 7. Add method to apply interest.
# 8. Store accounts in a list.
# 9. Search for account by account number.
# 10. Print account summary using __str__.