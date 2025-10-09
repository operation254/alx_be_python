# class_static_methods_demo.py

class Calculator:
    """Demonstrate static vs class methods."""
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Return the sum of two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Print the class calculation type, then return the product."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
