Usage Examples
==============

Accelerate your NumPy code
~~~~~~~~~~~~~~~~~~~~~~~~~~

A common need for speed when working with Python are scientific codes. NumPy and
the SciPy stack provides a rich environment for scientific computing, different
approaches exist to accelerate such code, with pyChapel a new means is provided.

The structure of a scientific code can often be factored into three stages::

1. Load a data-set
2. Process the data
3. Visualize results

An example of such an application is provided below:

.. literalinclude:: /examples/python.numpy.synthetic.py
   :language: python

Where the time-consuming, computational expensive and memory hungry portion of
the application is the data-processing performed in the `simulate` function.

When tasked with increasing the throughput of such appliacations the user can
either choose to port to application to another language, write a Python-extension implemented in a lower-level language such as C or call into library-functions implemented in lower-level languages.

Using pyChapel, this can be achieve with little effort such as rewritten example
below illustrates:

.. literalinclude:: /examples/chapel.numpy.synthetic.py
   :language: python

These two implementations can be executed by the commands::

  ./chapel.numpy.synthetic.py --tsteps 50 --particles 50000000
  ./python.numpy.synthetic.py --tsteps 50 --particles 50000000

The following subsection provides a couple of preliminary performance numbers.

Numbers
-------

On two systems one being a laptop another a cluster node. On each system each
implementation was executed three times and the average reported::

  # Laptop
  NumPy: wall-clock ~28.3 seconds, ~2.2GB memory consumption.
  NumPy+pyChapel: wall-clock average ~8.8 seconds, ~1.5GB memory consumption.

  # Cluster-node

Resulting in a speedup of ~ times 3.2 and a significantly lowered memory
consumption.

C-Implementation
................

.. todo:: Add OpenMP to the c-implementation to compare and illustrate how close this performance gain is to an error-prone c-implementation.

.. literalinclude:: /examples/c.numpy.synthetic.py
   :language: python
