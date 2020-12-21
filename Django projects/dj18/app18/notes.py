#
# Function-Based Views
# Pros
# Simple to implement
# Easy to read
# Explicit code flow
# Straightforward usage of decorators
# Cons
# Hard to extend and reuse the code
# Handling of HTTP methods via conditional branching
# Class-Based Views
# Pros
# Can be easily extended, reuse code
# Can use O.O techniques such as mixins (multiple inheritance)
# Handling of HTTP methods by separate class methods
# Built-in generic class-based views
# Cons
# Harder to read
# Implicit code flow
# Hidden code in parent classes
# Use of view decorators require extra import, or method override