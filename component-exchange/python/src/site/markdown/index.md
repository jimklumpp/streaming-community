# Performing calculus operations in Python

The purpose of this module is to call a process external to StreamBase to 
handle certain calculations. 

The Python library numpy is an excellent programming tool for scientific and 
mathematical computing. In this simple example, we call a Python script from 
StreamBase that imports the numpy library in order to perform either 
integration or differentiation on a polynomial.

**Input Stream:**

* Integrate    - A boolean variable where "true" represents integrate and "false" represents differentiate.
* Coefficients - A list of polynomial coefficients that start at the term with the highest power and end with the constant term.

The tuple is then sent to the the Python module where the desired Calculus 
operation is performed. Notice that there are two output streams. The 
StreamBase output stream returns a timestamp (representing the time before 
processing) and a summary of what was input. The Python output stream returns 
the output from the Python function, the time of completion and the approximate 
time it took to run the external process.

If everything runs smoothly, a list representing the Calculus operation 
performed is in the Output field of the output tuple. If an error occurs while 
running the external process operator, an error message is placed in the Error 
field of the output tuple.

This example depends on numpy, which you must obtain and build independently. 
Download the numpy package from http://numpy.scipy.org/, and follow the 
instructions in the INSTALL.txt and README.txt files at the top level of 
the distribution archive. Building and installing numpy requires a supported 
C compiler. Make sure numpy is installed as a Python library on your system and 
that it is locatable by the Python "import numpy" line. For Windows, StreamBase 
supports Python 2.6 from ActiveState or Python.org, as described in the API Guide 
in the StreamBase documentation.

In the EventFlow application, there is an External Process operator named 
CallPython. One of the command arguments for this operator is the path to 
the external Python file to execute, <span>Calculus</span>.py. As installed from the 
StreamBase Component Exchange, this file is placed in the Extras directory of 
the Studio workspace for the SB_Python project. Thus if you installed this 
project from the StreamBase Component Exchange, change the second argument in 
the Command Arguments tab of the CallPython operator to the following, with double 
quotes:
    "Extras\\<span>Calculus</span>.py"

Since the current working directory of the PythonProcess.sbapp application is 
the project workspace, the Extras directory is found with a relative path.
If one wishes to run a python script from a different directory, then one must 
instead provide the full path to this file.

Version History
	1.1 - Updated paths and deleted variables in parameters tab