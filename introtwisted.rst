.. _introtwisted:

****************************************************
-Python Packages- Part 9: Twisted Matrix
****************************************************

`Twisted-Matrix <https://twistedmatrix.com/trac/>`_, an event-driven networking engine.

Twisted-Matrix is a package with Network and Internet tools. The package supports TCP, UDP, SSL/TLS, IP Multicast, Unix
domain sockets, a large number of protocols (including HTTP, XMPP, NNTP, IMAP, SSH, IRC, FTP, and others). Even more it
is also an event handler. This means that you can define callbacks in Twisted. Callbacks are functions, which will be
called when an event arrived. This has the advantage, that your program is not blocking when it must wait for example
of a network connection. In this time your program can do different stuff, for example database tasks. In this program
is a network interface implemented which allows calls from other hosts to execute different functions on the server.
This interface is server-side defined with the XML-RPC standard.

The XML-RPC standard is a remote procedure call (RPC) protocol which uses XML to encode its calls and HTTP as a transport mechanism.

From server side the calculated values of our crankshaft are returned as a xml-file. For example the client can use this
information for further calculations. From the first blog entry, we know how to calculate the speed of a crank shaft.
In my interactive first example I use the next code example to calculate the values for the diagram. The returned values
(xml-format) from the Twisted event handler are read out by Javascript (example coming soon). Here I want you to show a
solution with a client which is also implemented in Python.

One remark: Twisted is not completely ready to use for Python 3.x at this moment (but works perfect with the 2.7 branch).

A second remark: Twisted runs absolutely perfect on Unix/Linux machines ( I'm really sorry for that...).

.. code-block:: python

    from twisted.web import xmlrpc, server
    import numpy as np

    #our known crank shaft function:
    def k(t,lam, omega,l_1,l_2):
        return l_2 * (lam*np.cos(omega *t) + np.sqrt(1-(lam*lam*np.sin(omega*t)*np.sin(omega*t))))


    class ExampleCalculator(xmlrpc.XMLRPC):

        #event handler
        def xmlrpc_crankShaft(self, l_1,l_2,omega):
            lamd = l_1 / l_2
            #round values
            l_1=np.around(l_1, decimals=2)
            l_2=np.around(l_2, decimals=2)
            omega=np.around(omega, decimals=2)
            lamd=np.around(lamd, decimals=2)

            #array, range for the X-values of the diagram, step size 0.01
            X = np.arange(-6, 6, .01)
            #array, calculate Y-values
            Y = k(X,lamd, omega,l_1,l_2)
            value = [[],[]] #2-dimensional array
            for l in range(len(X)):
                value[0].append(round(X[l],2))
                value[1].append(round(Y[l],2))

            return value


    if __name__ == '__main__':
        #import the event application of twisted
        from twisted.internet import reactor

        # assign the ExampleCalculator class as the event handler and configure Twisted for port 7080
        r = ExampleCalculator()
        reactor.listenTCP(7080, server.Site(r))

        #start the event handler
        reactor.run()



Here the client:

.. code-block:: python

    import xmlrpclib
    import matplotlib.pyplot as pp

    #connect the server
    s = xmlrpclib.Server('http://127.0.0.1:7080/')

    #call the remote server function
    values = s.crankShaft(2.2,4,8)

    #plotting as usual
    pp.plot(values[0], values[1], color='red', lw=2)
    pp.show()

What it does? It plots our crankshaft plot... But it gets the values from the server (that is really funny).