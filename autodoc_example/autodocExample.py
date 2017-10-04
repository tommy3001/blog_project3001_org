class Foo:
    """Docstring for class Foo.

    * This is a test
    * This also

    This is a short explanation of the class. This is a short
    explanation of the class. This is a short explanation of the class.
    """
    #: Doc comment for class attribute Foo.bar.
    #: It can have multiple lines.
    bar = 1
    flox = 1.5   #: Doc comment for Foo.flox. One line only.
    gbaz = 2
    """Docstring for class attribute Foo.baz."""
    def __init__(self):
        #: Doc comment for instance attribute qux.
        self.qux = 3
        self.spam = 4
        """Docstring for instance attribute spam."""
    def freakyFunction(self):
        """Docstring of Foo.freakyFunction"""
        pass

