## 📘 Python OOP (Object-Oriented Programming)

### 🧠 What is OOP?

OOP (Object-Oriented Programming) is a **programming paradigm** that organizes code around **objects** — data and behavior bundled together.

It helps you model real-world entities (like Car, Student, Employee) as objects in your code.

---

### 🔹 4 Pillars of OOP

1. **Encapsulation** – Hiding internal details and exposing only what’s necessary.
2. **Abstraction** – Showing only essential features; hiding complex logic.
3. **Inheritance** – Child classes inherit properties/methods from parent classes.
4. **Polymorphism** – Same method name but different behavior based on the object.

---

### 🧩 1. Class and Object

**Class** → Blueprint
**Object** → Real instance of that blueprint

```python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start(self):
        print(f"{self.brand} {self.model} started.")

# Creating Object
car1 = Car("Tesla", "Model S")
car1.start()
```

**Output:**

```
Tesla Model S started.
```

---

### 🧱 2. Encapsulation

Encapsulation = wrapping data and code together.
We can make variables **private** using `_` or `__` to restrict direct access.

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # private variable

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(5000)
account.deposit(2000)
print(account.get_balance())  # 7000
```

---

### 🎭 3. Inheritance

Inheritance allows one class (child) to derive from another (parent).
Helps in **code reusability**.

```python
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

dog = Dog()
dog.sound()
```

**Output:**

```
Dog barks
```

---

### 🌀 4. Polymorphism

Polymorphism means **one function behaves differently** depending on the object.

```python
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying high")

def lift_off(entity):
    entity.fly()

lift_off(Bird())
lift_off(Airplane())
```

---

### 🎨 5. Abstraction

Hide complexity using **abstract classes** (via `abc` module).

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

circle = Circle(5)
print(circle.area())  # 78.5
```

---

### 💬 Analogy

Think of **a class as a recipe**, and **an object as the dish** made from that recipe.
You can create many dishes (objects) from one recipe (class).

---

### ⚙️ Real-world Example

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        print(f"Name: {self.name}, Salary: ₹{self.salary}")

emp1 = Employee("Shani", 90000)
emp1.show_details()
```

**Output:**

```
Name: Shani, Salary: ₹90000
```

---

### 💡 Socratic Questions

1. Why is OOP considered more modular and maintainable than procedural programming?
2. What is the difference between **encapsulation** and **abstraction**?
3. Can you think of a real-world entity you’d model using a class?

---

### 🧩 Mini Exercise

Create a class `Student` that has:

* Attributes: `name`, `marks`
* Method: `grade()` that prints "Pass" if marks ≥ 50 else "Fail"

Then, create two students and call their `grade()` methods.
