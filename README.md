# Python4Capella
Python4Capella allows you to interact with your Capella model using Python. You will be able to create Python scripts to read and write from/to your Capella model.

# Installation
You can install Python4Capella in your Capella in two ways:
* update site
* dropins

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
