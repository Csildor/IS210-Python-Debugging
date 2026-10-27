Python Debugging with pdb
=========================

About this project
------------------

This example introduces ``pdb``, Python's built-in debugger. Debugging lets
us pause a program, inspect variables, and follow execution one line at a
time. I chose it because we will cover debugging later in IS 210, and I wanted
to get familiar with a useful tool before that lesson.

Requirements and installation
-----------------------------

You need Python 3. The ``pdb`` module is included in the Python standard
library, so no extra installation is required.

Run the example normally
------------------------

Open a terminal in this folder and run::

    python debugging_demo.py

On some systems use ``python3`` instead. Expected output::

    Scores: [80, 90, 100]
    Average: 90.00

Run it in the debugger
----------------------

Start the same program with ``pdb``::

    python -m pdb debugging_demo.py

At the ``(Pdb)`` prompt, try these commands:

* ``l`` : list nearby source code.
* ``b 10`` : set a breakpoint at line 10 (the loop in ``calculate_average``).
* ``c`` : continue until the breakpoint.
* ``p total`` : display the current value of ``total``.
* ``p score`` : display the current value of ``score``.
* ``n`` : execute the next line without stepping into called functions.
* ``s`` : step into a function call.
* ``q`` : quit the debugger.

For a beginner-friendly walkthrough, try this sequence instead:

1. At the first ``(Pdb)`` prompt, type ``b calculate_average`` and press Enter.
2. Type ``c`` to continue to that function.
3. Type ``p scores`` to inspect the input list.
4. Type ``n`` a few times, and use ``p total`` to see how the total changes.
5. Type ``c`` to finish the program, then ``q`` if the debugger prompts again.

If you want to investigate a bug, change one of the scores or temporarily
change the math in the function and use the debugger to see what happened.

Why it matters
--------------

Unlike ``try`` / ``except``, which handles errors during normal program
execution, a debugger helps you understand what the program is doing. It can
also reveal logic errors that do not raise exceptions.
