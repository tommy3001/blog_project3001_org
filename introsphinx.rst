.. _introsphinx:

****************************************************
-Python Packages- Part 6: Sphinx
****************************************************


This blog entry is a try to show you some hot tips to improve your work flow with the document generator   `sphinx <http://sphinx-doc.org>`_.

The sphinx document generator is very scalable. You are able to improve it with further extensions.

What I want to show you here:

* Generate formulas with the popular latex syntax (png or rendered with mathjax)
* Include line numbers and highlighted lines in your code
* Autodoc, get your documentation directly from the code
* Doctest, integrate your test code in the documentation
* Generate and integrate your plots directly in sphinx by executing your code examples
* A small overview of some syntax examples


Generate Formulas
==================


Formulas are generated with the latex syntax for formulas. In the `wikibooks <http://en.wikibooks.org/wiki/LaTeX/Mathematics>`_ about latex you can find an introduction about this topic.
In sphinx you can include inline math (e.g. the result of `:math:`x\\leftarrow y\\ x\\forall y\ x-y``  is
:math:`x\leftarrow y\ x\forall y\ x-y` or display mode.
Here an example::

    .. math::

        M = \begin{bmatrix}
           \frac{5}{6} & \frac{1}{6} & 0           \\[0.3em]
           \frac{5}{6} & 0           & \frac{1}{6} \\[0.3em]
           0           & \frac{5}{6} & \frac{1}{6}
         \end{bmatrix}

The result is:


.. math::

    M = \begin{bmatrix}
       \frac{5}{6} & \frac{1}{6} & 0           \\[0.3em]
       \frac{5}{6} & 0           & \frac{1}{6} \\[0.3em]
       0           & \frac{5}{6} & \frac{1}{6}
     \end{bmatrix}

There are two ways to integrate your formulas in your sphinx documentation:

The first possibility is the javascript library `Mathjax <http://www.mathjax.org/>`_ :

To do this, you must include the following extension in your `conf.py` in your root folder of the documentation:

.. code-block:: python

    extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',  #Here it is
    'sphinx.ext.viewcode',

    ]


Mathjax will be included automatically in your html output (`make html` command in the root directory of your document) by implementing the javascript library.


The second way is by including `sphinx.ext.pngmath` instead  in your `extensions` variable in the `conf.py` file.. One dependence is dvipng. With this extension the formulas are rendered to png.


Extended code view
===================

To highlight code lines, you should use :emphasize-lines: , e.g.::

        .. code-block:: python
            :linenos:
            :emphasize-lines: 3,3-5

            def primes( kmax):
                p= range(1000)
                result = []


The result is:

.. code-block:: python
    :linenos:
    :emphasize-lines: 1,3-5

    def primes( kmax):
            p= range(1000)
            result = []
            if kmax > 1000:
                kmax = 1000


To show only the line numbers, you can set `:linenos:` without `:emphasize-lines:`.

.. code-block:: python
   :linenos:

        def primes( kmax):
                p= range(1000)
                result = []

Autodoc
=======

With the `autodoc <http://sphinx-doc.org/ext/autodoc.html>`_ extension you are able to extract documentation directly from your Python code.
For example, if you want to include the `doc string` in your sphinx generated documentation  of the following  module,

.. literalinclude:: autodoc_example/autodocExample.py
   :language: python

you can use the following instruction::


    .. autoclass:: autodocExample.Foo
        :members:



The module class must be included in your `conf.py` file (e.g. with `sys.path.insert(0, os.path.abspath('autodoc_example'))`).
In this case the folder `autodoc_example' is included in your root folder of your documentation (normally the code and
the documentation are placed in  different folders in the application root folder).


Here the generated class description:

.. autoclass:: autodocExample.Foo
        :members:

Doctest
========
`Doctest <http://docs.python.org/3.3/library/doctest.html>`_  is another big reason why I love Python. It is a standard library of Python.
With doctest you can document and test your code in the same way with your in the code included `docstrings`.

Here our example function:


.. literalinclude:: doctest_example/doctestExample.py
   :language: python


One remark: To include complete files in your sphinx document, you can use::

    .. literalinclude:: doctest_example/doctestExample.py
   :language: python



When you run it with Python doctestExample.py, you will get an error message in case of a difference between the described output and the real output.
For more information, even in the case of no failures, you should use `python -v doctestExample.py`

Doctest compares the function call (starts with `>>>`) with the output of the command, which is placed in the docstring directly under the function call description.

If you include it with `docstring` in this document with::

    .. autoclass:: doctestExample.factorial()
        :members:

It looks like:


.. autoclass:: doctestExample.factorial()
    :members:




Integration of plots
====================


To plot the example from the first blog article and include it automatically in this document , you can write::

    .. plot::

        import matplotlib.pyplot as pp
        import numpy as np

        def k(t,lam, omega,l_1,l_2):
                return l_2*(lam*np.cos(omega*t)+np.sqrt(1-(lam*lam*np.sin(omega*t)*np.sin(omega*t))))

        l_1=1.0
        l_2=5.0
        omega = 4.0
        lam = l_1 / l_2
        t = np.arange(-6, 6, 0.1)
        S = k(t,lam, omega,l_1,l_2)
        pp.plot(t, S, color='red', lw=2)
        pp.show()


The magic is here `.. plot::`. I love Python...

The output is the following:

.. plot::

    import matplotlib.pyplot as pp
    import numpy as np

    def k(t,lam, omega,l_1,l_2):
            return l_2*(lam*np.cos(omega*t)+np.sqrt(1-(lam*lam*np.sin(omega*t)*np.sin(omega*t))))

    l_1=1.0
    l_2=5.0
    omega = 4.0
    lam = l_1 / l_2
    t = np.arange(-6, 6, 0.1)
    S = k(t,lam, omega,l_1,l_2)
    pp.plot(t, S, color='red', lw=2)
    pp.show()


The extension `'matplotlib.sphinxext.plot_directive',` must be added to the `extensions` array in the conf.py configuration file.


Overview of the sphinx syntax
=============================

This chapter is not ready yet.

Sphinx has a very good tutorial  `Try it out <http://sphinx-doc.org/tutorial.html>`_ .