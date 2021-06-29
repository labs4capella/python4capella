# Python4Capella

Python4Capella allows you to interact with your Capella model using Python. You will be able to create Python scripts to read and write from/to your Capella model.

# Introduction to the need

One basic need of most Capella users is to be able to extract information from Capella models.

In addition to that, the need to be able to import information in a Capella model is also important (to initialize a model, update it...).

However, those needs are currently poorly supported by the tool and existing add-ons.

The idea of this initiative is to provide Python API so that users will be able to develop scripts for Capella.

Scripts will be able to support export / import of data in excel in a generic way, but also at the end could support many more use cases.

# Python4Capella solution

The proposed solution is an add-on for Capella allowing to develop and execute scripts in Capella.

(Technically, it encapsulates Eclipse EASE to allow execution of scripts, PyDev for the edition of Python Scripts, and a Python interpreter.)

Here is a preview of the solution:
![Python4Capella Solution](./README/python4capella_solution.png)

The solution is based on a 3 levels architecture:

Level | Content | Defined | Used By
----- | ------- | ------- | -------
1     | Java API to bridge Python with Java. It is defined in the most generic way to support extraction / import of any kind of information <br/> **Provided by default with the add-on** | Java developers | Advanced Users to develop technical Python Libraries
2     | Python technical libraries. Provides to basic users a set of simplified operations to be used to define high level scripts <br/>**Some libraries are provided by default, including a simplified definition of Capella metamodel and libraries for most common add-ons (Requirements, PVMT)** | Advanced Capella Users <br/>(if default libraries need to be extended) | Basic Users to build high level scripts | Basic Users to build high level scripts
3     | High-level user scripts. Used to define the actions to perform (information to be exported / imported) <br/>**Some examples are provided by default to illustrate the capabilities of the add-on** | Basic Users | Basic Users to execute the scripts

![Python4Capella Levels](./README/python4capella_levels.png)

Legend:

- Circled in red: the scope of the solution
- Blue: what is created by users

More in details, the solution supports:

- **the use of a common scripting language**, not dedicated to Capella: **Python**
- **easy to share**: scripts are defined in the workspace, can be exported in a zip file and imported by another user
- **easy to use**: scripts can be executed from
  - contribution to contextual menu (right click on a model element)
  - right click on the script, execute
  - command line (for automatic extraction for example)
- **high customization capabilities** as all of the scripts are accessible by users to be modified / extended if necessary
- **extensibility of Capella metamodel by add-ons** (any information from the model can be accessed, even information from add-ons)
- **separation between technical stuff** (in level 2) **and high level scripting** (in level 3) to hide complexity to end users
- default libraries including:
  - a **simplified metamodel for Capella**, which can be extended if the simplified version does not covers specific needs
  - **libraries for common add-ons** (Requirement, PVMT)
  - **utilities** to support excel import / exports and possibly others
  - **examples** of high level scripts
- **wide compatibility with Capella versions** (the goal is to support at least Capella 1.3.x to Capella 5.x)
- **support of Capella and Team for Capella**

# Capella simplified metamodel for Python4Capella

Python4Capella relies on a simplified metamodel in order to ease the definition of scripts by end-users.

This simplified metamodel is defined in a Capella model (**using Capella 5.0.0**).

Please have a look in the documentation tab of the model to know more about its content.

This model can be retrieved here:  https://github.com/labs4capella/python4capella/tree/master/specification/Capella%20Light%20Metamodel

Moreover, a documentation is generated from this model using M2Doc.
This documentation can be retrieved here:  https://github.com/labs4capella/python4capella/blob/master/specification/M2Doc%20generation/Python4Capella%20Simplified%20Metamodel.docx

PS: the Capella model can be retrieved by cloning the git repository, or by downloading a zip file of the last version of the repository.
For this last option, you need to go this the main page (https://github.com/labs4capella/python4capella) and select Code / Download ZIP

![Python4Capella Download](./README/python4capella_download.jpg)

# Installation

You can install Python4Capella in your Capella in two ways:

- update site
- dropins

Then you will need to setup Python 2.7 in your environment.

## Update site

You will need to add the following update site to your Capella installation:

TODO add the update site URL

If you don't know how to install from an update site you can have a look at our [video](https://www.youtube.com/watch?v=qYTrO7THer0).

Then select the Python4Capella feature:

![Select the Python4Capella feature](https://raw.githubusercontent.com/labs4capella/python4capella/master/README/Install.png)

Click the next button and complet the installation by clicking the finish button.

## Dropins

To install using dropins, you need to download the following zip file:

TODO add droping zip URL

Then unzip it in the dropins folder in the same folder as your Capella executable.

## Python 2.7 installation

If you are running Windows, you can download the following zip file and unzip it in your Capella installation directory, or any other location:

TODO add the Python 2.7 zip file URL

If you are running Linux or MacOS X, please check your distribution documentation to install Python 2.7 on your system.

# Python4Capella configuration

You need to import the Python4Capella project that contains the Python API needed to interact with Capella and store your own Python scripts.

Right click in the project explorer and select New > Other menu:

![Right click in the project explorer and select New > Other](https://raw.githubusercontent.com/labs4capella/python4capella/master/README/import-Python4Capella-01.png)

In the New dialog, select the Python4Capella project under the Python4Capella category:

![Select the Python4Capella project](https://raw.githubusercontent.com/labs4capella/python4capella/master/README/import-Python4Capella-02.png)

You can click the next then finish buttons to complet the wizard.

At this point you will be prompted to configure your python environment, you can ignore the dialog for the moment and follow the next steps to setup your environment.

![Python4Capella project content](https://raw.githubusercontent.com/labs4capella/python4capella/master/README/import-Python4Capella-03.png)

You now have the following Python4Capella project in your workspace:

![Python4Capella project content](https://raw.githubusercontent.com/labs4capella/python4capella/master/README/import-Python4Capella-04.png)

Now you need to refence your Python 2.7 interpreter:

Select the Window > preferences menu
- select the PyDev / Interpreters / Python Interpreter
  - select the python executable from the [Python 2.7 installation section](#python-27-installation) by clicking the New button
- select the Scripting / Python Scripting (using Py4J) (/!\ not Scripting PyDev)
  - select the python executable from the [Python 2.7 installation section](#python-27-installation) by clicking the Browse button
- select the Scripting / Scripting Locations
  - add /Python4Capella/enduser by clicking the Add Workspace button

You can click the Apply and close button to finish your setup.

When you will open your fist Python file, you will be prompted by PyDev to define its default configuration:

![Default Eclipse preferences for PyDev](https://raw.githubusercontent.com/labs4capella/python4capella/master/README/PyDev_preferences.png)

You can validate the dialog by clicking the OK button.

You can refere to the plugin documentation for usage reference. The documentation is accessible by using the Help > Help contents menu from capella, then on the right tree, you can select Python4Capella.
