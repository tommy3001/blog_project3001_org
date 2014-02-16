****************************************************
-Python Packages- Blog overview
****************************************************



:ref:`Part 1: Numpy and Matplotlib <intronumpy>`
==================================================================

Python is a fantastic programming tool. It has a simple syntax, a lot of additional libraries and this scripts are running out of the box. 
All you need is an installed Python interpreter and the used libraries. It is running under MS Windows, Mac, Linux and other. The scripting language 
is like the glue between different components and other programming languages. For example you can call C/C++ functions with Cython inside Python scripts. 

Python claims to combine "remarkable power with very clear syntax" [Python-docs]

In this blog I want to show you some important tools and libraries. This is the first part of this topic. Here is is a introduction by example in the 2 packages.

*  Numpy
*  Matplotlib

Calculation examples with visualization you can find in the project part ( project 1 and 2) .  

:ref:`Read more ...<intronumpy>`



:ref:`Part 2: Scipy <introscipy>`
===================================================

In this part I want to write something about SciPy. It is an extension for Numpy.

SciPy contains modules for optimization, linear algebra, integration, interpolation, special functions, FFT, signal and image processing, ODE solvers and others.

Here I want to show you an example with B-splines. It is a subfield of numerical analysis. It has a wide range of applications like in the computer science subfields computer-aided design and computer graphics. It is also used for motion planning of robots and other mechanic structures. 

B-splines were investigated in the beginning of the last century by Nikolai Lobachevsky.  In the mathematics a spline is a smooth polynomial function that is piecewise-defined, and possesses a high degree of smoothness at the places where the polynomial pieces connect (which are known as knots).

B-splines can be evaluated in a numerically stable way by the de Boor algorithm.  I don't want to treat you here with this stuff of mathematical derivations. If you are more interested in this, you can read detailed information about computed geometry here. The details are also  for me not of interest.

In SciPy is a function implemented to solve this stuff for you.   
:ref:`Read more ...<introscipy>`


:ref:`Part 3: Sympy <introsympy>`
===================================================


SymPy is a library for symbolic computation for (you are right...) Python.

It includes features like basic symbolic arithmetic, calculus, algebra and discrete mathematics.To show you a small example, 
I used a classical linear system of an one-dimensional movement of a mass  described with the Newton’s laws of motion which is 
moving vertical between 2 walls, a spring and a damper. :ref:`Read more ... <introsympy>`



:ref:`Part 4: Cython <introcython>`
=====================================================


With Cython you are able to write C and C++ modules for Python. It implements a superset of the Python language. 
With Cython you are also able to call C-functions and realize strong typing of variables and functions like float 
(floating point numbers) or int (integer) definition of variables. Here is an example of strong typing with Cython:

.. code-block:: python

	def primes(int kmax):
    		cdef int n, k, i
    		cdef int p[1000]
    		result = []
    		if kmax > 1000:
			kmax = 1000
   		k = 0
   		n = 2
    		while k < kmax:
        		i = 0
        		while i < k and n % p[i] != 0:
           			 i = i + 1
        		if i == k:
            			p[k] = n
           			 k = k + 1
            			result.append(n)
        		n = n + 1
  		 return result
 
This implementation of an algorithm to find prime numbers has some additional commands instead of the next one, which is implemented in pure Python:
:ref:`Read more ... <introcython>`




:ref:`Part 5: Psutil <intropsutil>`
===================================================
I wrote a small Python script to be ready for the next Mars invasion. It is running all the time on my server. It checks only some system values like CPU and net usage and the availability of project3001.org. If there is an overload or the address is not available, the program sends an email. This can be a protection against  `DDoS atacks <http://en.wikipedia.org/wiki/Denial-of-service_attack>`_. (Please not me, I'm one of the good guys!!)

  `Psutil <https://code.google.com/p/psutil/>`_  is a small package with very useful system functions.
  :ref:`Read more ... <intropsutil>`




:ref:`Part 6: Sphinx <introsphinx>`
====================================


This blog entry is a try to show you some hot tips to improve your work flow with the document generator   `sphinx <http://sphinx-doc.org>`_.

The sphinx document generator is very scalable. You are able to improve it with further extensions.

What I want to show you here:

* Generate formulas with the popular latex syntax (png or rendered with mathjax)
* Include line numbers and highlighted lines in your code
* Autodoc, get your documentation directly from the code
* Doctest, integrate your test code in the documentation
* Generate and integrate your plots directly in sphinx by executing your code examples

  :ref:`Read more ... <introsphinx>`


:ref:`Part 7: Data storage with HDF5 <introhdf>`
================================================


What the hell is HDF? "The Hierarchical Data Format HDF (HDF4, HDF5) is the name of a set of file formats and libraries designed to store and organize large amounts of numerical data.  Originally developed at the National Center for Supercomputing Applications, it is currently supported by the non-profit HDF Group, whose mission is to ensure continued development of HDF5 technologies, and the continued accessibility of data currently stored in HDF" It is for example widely used by scientist of the NASA space agency. They are using it to save the different measured values of a telescope or a satellite. A really great database of these files is freely available on different NASA project websites. The here used HDF5 format is a little bit newer version. 3 Python packages are used for this example:

* guidata
* h5py
* numpy

The aim of this example is to handle this kind of files with a graphical interface in a really easy (Python) way. On the end we will have a program which can open hdf5 files, can show the different hierarchical entries and can present the numerical values in matrices or vectors.

This program needs only 35 lines of code.

Guidata is a Python library generating graphical user interfaces for easy dataset editing and display.

The h5py package is a Pythonic interface to the HDF5 binary data format.

It lets you store huge amounts of numerical data, and easily manipulate that data from NumPy. For example, you can slice into multi-terabyte datasets stored on disk, as if they were real NumPy arrays. Thousands of datasets can be stored in a single file, categorized and tagged however you want.

:ref:`Read more ... <introhdf>`




:ref:`Part 8: Website with jinja2 and tornado <introjinja>`
============================================================

This article was stolen from the famous  `kennethreitz/python-guide. <http://docs.python-guide.org//>`_ The introduction to jinja2 and tornado with its
code examples was a contribution from me.
... so I stole my own code back to complete a little bit my blog ...


The introductions to template engines and frameworks are from the python-guide and its authors.


Templating (with Jinja2)

Most WSGI applications are responding to HTTP requests to serve
content in HTML or other markup languages. Instead of generating directly
textual content from Python, the concept of separation of concerns
advises us to use templates. A template engine manages a suite of
template files, with a system of hierarchy and inclusion to ...

:ref:`Read more ... <introjinja>`


:ref:`Part 9: Twisted Matrix <introtwisted>`
============================================================
Twisted-Matrix, an event-driven networking engine.

Twisted-Matrix is a package with Network and Internet tools. The package supports TCP, UDP, SSL/TLS, IP Multicast, Unix
domain sockets, a large number of protocols (including HTTP, XMPP, NNTP, IMAP, SSH, IRC, FTP, and others). Even more it
is also an event handler. This means that you can define callbacks in Twisted. Callbacks are functions, which will be
called when an event arrived. This has the advantage, that your program is not blocking when it must wait for example
of a network connection. In this time your program can do different stuff, for example database tasks. In this program
is a network interface implemented which allows calls from other hosts to execute different functions on the server.
This interface is server-side defined with the XML-RPC standard.

The XML-RPC standard is a remote procedure call (RPC) protocol which uses XML to encode its calls and HTTP as a transport mechanism.

:ref:`Read more ... <introtwisted>`