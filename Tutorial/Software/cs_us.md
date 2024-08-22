## Common

### What is refactoring?

Refactoring is the process of restructuring existing code without changing its external behavior. The main goal is to improve code readability, reduce complexity, and make the codebase easier to maintain and extend. Regular refactoring helps in minimizing technical debt and ensures that the software remains robust over time.

### What are design patterns?

Design patterns are proven solutions to common design problems in software development. They provide a template for how to solve these problems in a way that is reusable and adaptable to various situations. Examples include the Singleton, Factory, and Observer patterns, which help in structuring code more efficiently.

### What is the Singleton pattern?

The Singleton pattern ensures that a class has only one instance throughout the application and provides a global access point to that instance. It is commonly used for managing shared resources like configurations or logging, where multiple instances could cause inconsistencies.

### What is the Factory pattern?

The Factory pattern is a creational design pattern that defines an interface for creating objects but allows subclasses to alter the type of objects that will be created. It decouples the object creation process from the client, making it easier to introduce new types without modifying existing code.

### What is the Observer pattern?

The Observer pattern is a behavioral design pattern in which an object, known as the subject, maintains a list of dependents, called observers, and notifies them of any state changes. This pattern is commonly used in event-driven programming where changes in one object need to be propagated to others.

### What is Jenkins?

Jenkins is an open-source automation server used to automate various stages of software development, including building, testing, and deploying. It supports continuous integration and continuous delivery (CI/CD) by allowing developers to automatically trigger these processes when changes are made to the codebase.

### What is Agile?

Agile is a software development methodology that promotes iterative development, where requirements and solutions evolve through collaboration between self-organizing teams. Agile emphasizes flexibility, customer feedback, and the continuous delivery of small, functional pieces of software.

### What is the Waterfall model?

The Waterfall model is a linear and sequential software development methodology where each phase must be completed before the next begins. This model is straightforward but lacks flexibility, making it difficult to address changes in requirements once the project is underway.

### What is Scrum?

Scrum is an Agile framework used for managing and completing complex projects. It organizes work into sprints, which are short, time-boxed periods during which specific work has to be completed. Scrum emphasizes collaboration, accountability, and iterative progress towards a well-defined goal.

### What is DevOps?

DevOps is a set of practices that combines software development (Dev) and IT operations (Ops) to shorten the development lifecycle and deliver high-quality software continuously. DevOps emphasizes automation, collaboration, and integration between development and operations teams.

### What is MLOps?

MLOps is a set of practices that combine machine learning (ML) with DevOps to streamline the process of deploying, managing, and monitoring machine learning models in production. It ensures that models are reproducible, reliable, and scalable, addressing the unique challenges of ML model lifecycle management.

### What is the difference between a process and a thread?

A process is an independent execution unit with its own memory space, while a thread is a lightweight subunit of a process that shares the same memory space. Threads within the same process can communicate more efficiently but may cause issues like race conditions if not managed properly.

### What is IPC (Inter-Process Communication)?

IPC, or Inter-Process Communication, refers to the mechanisms provided by the operating system that allow processes to communicate with each other. Common IPC methods include shared memory, message passing, and pipes, which enable data exchange between processes in a controlled manner.

### What is a deadlock?

A deadlock is a situation in computer systems where two or more processes are unable to proceed because each is waiting for the other to release a resource. Deadlocks can cause programs to hang indefinitely, and preventing them requires careful management of resources and locking mechanisms.

### What is the difference between Docker and a virtual machine (VM)?

Docker is a containerization platform that allows applications to run in isolated environments called containers, which share the host OS kernel. Virtual machines (VMs), on the other hand, are fully virtualized systems that include their own OS kernel. Docker containers are more lightweight and faster to start, while VMs offer stronger isolation but with higher resource overhead.

### What is orchestration in the context of cloud computing?

Orchestration in cloud computing refers to the automated arrangement, coordination, and management of complex computer systems, middleware, and services. Tools like Kubernetes are commonly used for orchestrating containers, ensuring they run smoothly together as part of a larger application deployment.

### What is Object-Oriented Programming (OOP)?

Object-Oriented Programming (OOP) is a programming paradigm that organizes software design around data, or objects, rather than functions and logic. Objects represent instances of classes, encapsulating data and behavior together, and OOP principles include inheritance, polymorphism, encapsulation, and abstraction.

### What is the difference between overriding and overloading?

Overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass, maintaining the same method signature. Overloading, on the other hand, allows multiple methods in the same class to have the same name but different parameters, enabling methods to perform similar but distinct tasks.

## Python

### What are the pros and cons of Python?

Python is known for its simplicity and readability, making it ideal for beginners and rapid development. It has a vast ecosystem of libraries and frameworks, especially in fields like data science and web development. However, Python can be slower than compiled languages like C++ due to its interpreted nature and may not be the best choice for performance-critical applications.

### What is a variable-length argument in Python?

Python allows functions to accept a variable number of arguments using *args for positional arguments and **kwargs for keyword arguments. This feature makes it easier to create flexible functions that can handle different numbers of inputs without requiring multiple function definitions.

### What is the difference between a Python list and a tuple?

The main difference between a list and a tuple in Python is that lists are mutable, meaning they can be modified after creation, while tuples are immutable and cannot be changed. Lists are typically used for collections of items that may change, whereas tuples are used for fixed collections.

### What is list comprehension in Python?

List comprehension in Python is a concise way to create lists based on existing lists. It allows for the construction of new lists by applying an expression to each element in a sequence, optionally filtering elements with conditions, and is often more readable and faster than traditional loops.

### What is the Python Global Interpreter Lock (GIL)?

The Global Interpreter Lock (GIL) in Python is a mutex that protects access to Python objects, preventing multiple native threads from executing Python bytecodes simultaneously. This makes Python's threading less effective for CPU-bound tasks but does not affect I/O-bound tasks significantly.

### What is the difference between a Python generator and an iterator?

In Python, an iterator is an object that implements the iterator protocol, with methods __iter__() and __next__(). A generator is a special type of iterator, created with functions and the yield statement, which can produce values lazily on demand and allows for memory-efficient iteration over large data sets.

### What is a Python decorator?

A Python decorator is a function that modifies the behavior of another function or method. Decorators are often used for cross-cutting concerns like logging, authentication, and caching, allowing these functionalities to be easily added to functions in a reusable and readable manner.
