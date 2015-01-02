.. _introcython:

****************************************************
-Python Packages- Part 4: Cython 
****************************************************
With `Cython <http://cython.org/>`_   you are able to write C and C++ modules for Python. It implements a superset of the Python language.
You are also able to call C-functions and realize declaration of variables and functions like in C (e.g. `float x;`or `int y;`). Here is an example:

.. code-block:: python
    :linenos:

    def primes(int kmax):
    """Calculate all prime numbers up to kmax
    (max. value: 1000) cdef variable declaration """

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


This implementation of an algorithm to find prime numbers has some additional keywords instead of the next one, which is implemented in pure Python:

.. code-block:: python


    def primes(kmax):
    """Calculate all prime numbers up to kmax
    (max. value: 1000) """

        p= range(1000)
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



The only difference between the both algorithm is this part:


.. code-block:: python

    #primes function with additional Cython code:
    def primes(int kmax):
        cdef int n, k, i
        cdef int p[1000]
        result = []


.. code-block:: python

	#primes in standard Python syntax:
    def primes(kmax):
        p= range(1000)
        result = []

What is the difference? In the upper Cython version you can see the declaration of the variable types  and the integer array like in standard C.
For example `cdef int n,k,i` in line 3.  This additional type definition (e.g. integer) allows the Cython compiler to generate
more efficient C code from the second code. While standard Python code is saved in `*.py` files,Cython code is saved in `*.pyx` files.

And what is with the speed? So lets try it!

.. code-block:: python

	import time
	#activate pyx compiler
	import pyximport
	pyximport.install()
	#primes implemented with Cython
	import primesCy
	#primes implemented with Python
	import primes

	print "Cython:"
	t1= time.time()
	print primesCy.primes(500)
	t2= time.time()
	print "Cython time: %s" %(t2-t1)
	print ""
	print "Python"
	t1= time.time()
	print primes.primes(500)
	t2= time.time()
	print "Python time: %s" %(t2-t1)


This lines are special:

.. code-block:: python

    import pyximport
    pyximport.install()


The `pyximport` module allows you to import `pyx` files (e.g., `primesCy.pyx`) with the Cython-compiled version of the `primes` function.
The `pyximport.install()` command allows the Python interpreter to start the Cython compiler directly to generate C-code,
which is automatically compiled to a `*.so` C-library. Cython is able to import this library for you in your Python-code.
Very easy and very efficient. With the `time.time()` function you are able to compare the time between this 2 different calls to find 500 prime numbers.

On a standard notebook (dualcore AMD E-450 1,6 GHz)  the measured values are:

Cython time: 0.0054 seconds

Python time: 0.0566 seconds

And here the output of an embedded `ARM beaglebone <http://beagleboard.org/Products/BeagleBone>`_  machine:

Cython time: 0.0196 seconds

Python time: 0.3302 seconds

That is a really good result...

(I contributed this article also to the famous `kennethreitz/python-guide. <http://docs.python-guide.org//>`_.)



