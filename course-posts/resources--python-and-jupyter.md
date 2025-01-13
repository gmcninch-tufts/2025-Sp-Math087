---
author: George McNinch
title: |
  Resources: python & jupyter
date: 2024-01-01
---

# Overview

Our course will use the `python` programming language to perform
some machine computations needed to carry out mathematical modeling
tasks.

And parts of the notes of the course lectures will be made available
as `jupyter notebooks`.

There are a few ways that you should learn to interact with `python`
and `jupyter` for our class:

#. via [Google's colab]
#. by executing ``python`` code in a ``python`` interpreter on your computer
#. (optionally) using [jupyter notebooks](http://www.jupyter.org)  on your computer.

Here is a bit of what you need to know to enable these interactions:

- [Overview of `jupyter` notebooks](#notebooks)
- [Interacting with `jupyter` notebooks via colab](#colab)
- [installing the tools on your computer](#venv)
- [using the `jupyter notebook` viewer on your computer](#jupyter)


Before diving into the details, let me try to answer a few question
that you may have:

**Q** - do I need to install `juptyer` on my computer, or I just use `colab`?

: **A** - It is probably possible to just use `colab`. `colab`
  provides a reasonable environment for reading the course material,
  though for code execution it may (?) be a tad slow.
  
  **But**: using `python` exclusively through `colab` is a somewhat
  imperfect environment for producing code, and at least in the long
  run you'll be better served by learning to work with these tools on
  your own computer.

# An overview of `jupyter` notebooks {#notebooks}

[`Jupyter` notebooks] provide a way to package written material -- with
possible mathematical markup -- together with an interactive
environment for executing computer code.

The material for this course will mostly be presented in the form of
these `notebooks`. You can recognize `notebook` files by their
filename extension -- their file name has the form `*.ipynb`.
 
On the course site, notebooks will be posted with *two links* -- one
to `colab`, and one to an `*.ipynb` file.

- The simplest way to interact with `jupyter notebooks` is to use
  [Google's colab]. Clicking one of the links will open the notebook
  *in the cloud* via the site
  [colab.research.google.com](https://colab.research.google.com/).

- The other one link permits you to download the `notebook` file to
  your computer. In order to use this file, you will need to have a
  working installation of `python` and `jupyter`. See below for some
  discussion of how to [set up the required tools](#venv) and how to
  [use `jupyter`](#jupyter).

[`Jupyter` notebooks]: https://jupyter.org/
[Google's colab]: https://colab.research.google.com/

# Interacting with `jupyter` notebooks via Google's CoLab {#colab}

As [mentioned above](#notebooks), the course material will be
presented in the form of `jupyter` notebooks, and for each notebook
there will be a link to a copy of this notebook available via
`colab`.

`Colab` is a web-based free-to-use Jupyter notebook environment that
runs in *the cloud* and stores its notebooks on Google Drive.  When
you view a notebook in `colab` containing code, that code can be
executed. The code execution occurs *in the cloud*, which basically
means *on some google computer*. Thus, google's computer has `python`
and the relevant libraries installed and available.

You can choose to interact with the course notebooks on `colab`, abd
create your own notebooks there.

A good starting point to learn how to use colab (and jupyter notebooks
in general) is the document [Overview of Colaboratory
Features](https://colab.research.google.com/notebooks/basic_features_overview.ipynb).

# Installing the tools on your computer {#venv}

Here I hope to answer the questions: "What do I need to do to be able
to view and execute `jupyter` notebooks on my computer?"

You first need to have [`python`](http://www.python.org) installed. In
many cases, this is already true.

We are going to install `jupyter` and some python libraries in a
*virtual environment*; you can read about [virtual environments
here](https://docs.python.org/3/library/venv.html).

To begin, create a directory named `jupyter` somewhere on your
computer (you can actually call it whatever you like...)

Open a `terminal` on your computer, and change to the directory you
just created. To do so, use a command something like:

> ```
> george@valhalla:~$ cd jupyter
> george@valhalla:~/jupyter$ 
> ```

(You should only type the `cd jupyter` bit. And you may need to type a
more complicated string if the directory you created is nested below
your home directory).

Now create a `virtual environment` as follows:

> ```
> $ python -m venv .venv
> ```

You may need to instead type

> ```
> $ python3 -m venv .venv
> ```

Among other things, this should create a directory named `.venv`
beneath your `jupyter` directory.

You now need to *activate* the virtual environment in your terminal.
In linux or on a mac, you do this as follows:

> ```
> $ source .venv/bin/activate
> ```

Looking at the docs
https://docs.python.org/3/library/venv.html
is appears that in `windows` you proceed as follows

> ```
> # in cmd.exe
> C:\jupyter\> .venv/Scripts\activate.bat
> 
> #or
> # in powershell
> C:\jupyter\> .venv\Scripts\Activate.ps1
> ```

After activation, the terminal "prompt" should appear differently. For
example, you might see something like this:

> ```
> (.venv) george@valhalla:~/jupyter$ 
> ```

You can no *exit* the virtual environment by typing `deactivate`, like this:

> ```
> (.venv) george@valhalla:~/jupyter$ deactivate
> george@valhalla:~/jupyter$
> ```

Now, with the virtual environment active, you can install the following
packages using a command called `pip`:

> ```
> (.venv) george@valhalla~/jupyter$ pip install jupyter numpy sympy scipy pandas pydot matplotlib
> ```

`pip` will install all these packages *in your `jupyter/.venv`
directory*. In this case, packages occupying ~750M of disk space are
installed and can be removed simply by deleting your `jupyter`
directory.

# Interacting with `jupyter` on your computer {#jupyter}


You can always view and interact with `jupyter notebooks` on
`colab`. But if you carried out the above instructions for installing
`conda`, you can now use `jupyter` notebooks on your own computer.

Start `jupyter` from the command-line. I actually find that I prefer
the `jupyter lab` interface to the the plain `jupyter notebook`
interface (and honestly I'm not sure I understand why there are two
different interfaces) but you should experiment for yourself.

So, with you virtual envirnoment activated type:


> ```
> (.venv) george@valhalla:~$ jupyter-lab
> ```

There will be some output to the terminal that you can mostly
ignore. The significant effect of running this program is that *a page
should open in your web browser*.

The page that opens will have a `URL` that looks something like:

> ```
> http://localhost:8888/lab
> ```

This `URL` tells you that there is now a `server` running on your
local machine, and that your web browser is communicating with that
server.

In the web page at this location, you should see in particular an
interface where you can interact with `jupyter notebooks`. You can
create a new notebook from the `File` menu: `New -> Notebook`. If you
are asked to `Select Kernel`, you should select `Python 3`.

You are now editing a file name `Untitled.ipynb`. 

If you save a `jupyter notebook` (i.e. a `ipynb` file) in your directory tree, you can open it using
the `File` menu: `Open from path`

You can end the `jupyter` notebook session by typing `C-c` (twice)
in the terminal where you started the command, or by menu-driven
commands in the web-interface.


# Some learning resources for python and scientific computing


(Honestly, I just borrowed this list from a previous instructor, but
the links look useful).

* [DataCamp's interactive Intro to Python tutorial](https://www.learnpython.org/)
* [Python for Everybody (University of Michigan MOOC)](https://www.py4e.com/lessons)
* [A short Python and NumPy tutorial (Stanford CS231)](http://cs231n.github.io/python-numpy-tutorial/)
* [Official Python tutorial](https://docs.python.org/3/tutorial/index.html)
* Numpy
  * [Introduction to
    NumPy](https://jakevdp.github.io/PythonDataScienceHandbook/02.00-introduction-to-numpy.html)
  * [NumPy reference
    guide](https://docs.scipy.org/doc/numpy/reference/) (chapter 2 of
    VanderPlas' *Python Data Science Handbook*)
* Matplotlib
  * [Official Pyplot tutorial
    (short)](https://matplotlib.org/tutorials/introductory/pyplot.html)
  * [Visualization with Matplotlib (chapter 4 of VanderPlas' *Python
    Data Science
    Handbook*)](https://jakevdp.github.io/PythonDataScienceHandbook/04.00-introduction-to-matplotlib.html)
  * [Gallery of Matplotlib
    examples](https://matplotlib.org/gallery/index.html)
