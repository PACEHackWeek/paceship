# README

Welcome to our 🛰️**PACESHIP**, a demonstration and practice repository for the PACE Data Hackweek.

- **DEMONSTRATION**:
  The stages below offer an opinionated process for authoring an open science project that uses Python.
  Click on the version "[tag]" noted in the subsections below to peek into the history of this repository at that stage.
- **PRACTICE**:
  The repository is for real! Not only can you trace the stages of development,
  you can use the repository to practice sharing your code with fellow hackweek participants.

[tag]: https://git-scm.com/book/en/v2/Git-Basics-Tagging

## DEMONSTRATION

You can explore the state of this repository at any stage described below on GitHub (i.e. without needing a local clone)
simply by following the `v0.x` links.
Navigate back to the `main` branch to see the current state of the repository.
Note that you should not clone this repository as a way of starting your own project, nor is it a [template repository].
Instead, try following these stages from scratch for your own project!

[template repository]: https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template

### Stage 1 ([v0.1](../../tree/v0.1))

Create a code repository on GitHub[^1] and start composing a README in your browser.

1. open https://github.com/new (sign in if prompted)
1. enter your project's "code name" :shipit: in "**Repository name**"
1. select the option to "**Add a README file**"
1. click the "**Create repository**" button

A README is a special document to all writers of code&mdash;it is the first place to look for information and is the "landing page" for any repository on GitHub.
Use your README to welcome readers and introduce the project.
You can edit this [GitHub Flavored Markdown][GFM] file and create a commit right on the GitHub platform.

[GFM]: https://docs.github.com/en/get-started/writing-on-github
[^1]: Or use whatever website works for you and your collaborators! It may be another cloud platform (e.g. https://bitbucket.org/) or a platform hosted by your workplace (e.g. https://git.smce.nasa.gov).

### Stage 2 ([v0.2](../../tree/v0.2))

Start authoring a Jupyter Notebook on the CryoCloud.

1. clone your repository
1. create a `notebooks` folder with a new notebook
1. add a `.gitignore` to prevent "data" from ending up in your code repository

Nearly all projects will have notebooks, and some projects may only have notebooks!
Keeping your notebooks in a subfolder makes your project ready for future complexification, and provides a dedicated area for "data" that are not a good fit for code repositories.

### Stage 3 ([v0.3](../../tree/v0.3))

Change some of your code into functions or classes to allow re-use and improve modularity.
Learn more about "[Defining Your Own Python Function]" Python functions in the Real Python lesson.
Open science projects often don't need classes, unless your project evolves into a package that needs "[The Power of Object-Oriented Programming]".

1. choose part of your notebook that can be "modularized"
1. sort "inputs" into an argument list, providing default values for optional arguments
1. define the function in your "Setup" section, and use it!

[Defining Your Own Python Function]: https://realpython.com/defining-your-own-python-function/
[The Power of Object-Oriented Programming]: https://realpython.com/python-classes/

### Stage 4 ([v0.4](../../tree/v0.4))

While Jupyter Notebooks are text-based (they are JSON files), they can have large binary outputs encoded as text and have other drawbacks when it comes to collaboration with git.
Jupyter Notebooks also make it possible to execute workflows "out of order", leading to problems with reproducibility.
For both of these reasons, you may want to work with Shell or Python scripts for part of your project.

TODO:
- scripts/png-to-s3 move figure to s3 temporary storage

### Stage 5 ([v0.5](../../tree/v0.5))

So now you want to use a function or class in multiple notebooks?
The most robust way forward&mdash;this seems like **a big deal** but is not&mdash;is to migrate your functions and classes to a Python package in the same project.
A package is something you can `import` in your notebooks, once it is made visible to the Python interpreter (i.e. "installed").

1. use the `uv` command line tool for initializing the package
    ```shell
    uv init --package
    ```
1. tell git to ignore the ".python-version" file
1. move your functions and classes to ".py" files inside the `src` tree
1. add your dependencies to your "pyproject.toml" file
    ```shell
    uv add numpy pillow
    ```
1. use `pip` to perform an "editable" install into your Python interpreter
    ```shell
    pip install -e .
    ```

### Stage 6 ([v0.6](../../tree/v0.6))

Prepare for users and contributors!

TODO:
- CONTRIBUTING.md
- LICENSE
- citation.cff
- zenodo github integration

## PRACTICE

You **should** fork this repository for practice contributing to an open science project.
Consider adding a notebook or a script by dropping it into the 🛰️**PACESHIP** repository through a pull request.
You could also add functions to the `src/paceship` folder containing the Python package .
Like many projects, we include a CONTRIBUTING.md guide to support first-time contributors, so take a look and ask a hackweek mentor for friendly supervision if desired!

## Acknowledgements

We would like to thank the US-OCB office for sponsoring the PACE Data Hackweek, and to acknowledge all hackweek
participants who improve this repository through feedback or contributions.
