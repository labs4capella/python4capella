# Python4Capella
Python4Capella allows you to interact with you Capella model using Python. You will be able to create Python scripts to read and write from/to your Capella model.

# Installation
You can install Python4Capella in your Capella in two ways:
* update site
* dropins

Then you will need to setup Python 2.7 in your environment.

## Update site
You will need to add the following update site to your Capella installation:

TODO add the update site URL

Then select the following feature:

TODO image

Then click the next button and complet the installation by clicking the finish button.

## Dropins
To install using dropins, you need to download the folloging zip file:

TODO add droping zip URL

## Python 2.7 installation

If you are running Windows, you can download the following zip file and unzip it in your Capella installation directory:

TODO add the Python 2.7 zip file URL

If you are running Linux or MacOS X, please check your distribution documentation to install Python 2.7on your system.

# Python4Capella configuration
TODO add a wizard to import the CapellaScripting project
TODO add the documentation to import the CapellaScripting project

Now you need to refence your Python 2.7 interpreter:

Select the Window > preferences menu
  - select the PyDev / Interpreters / Python Interpreter node
    - select the python executable from your system
  - select the Scripting / Python Scripting (using Py4J) (/!\ not Scripting PyDev)
    - select the python executable from your system
  - select the Scripting / Scripting Locations
    - add /CapellaScripting/enduser

You can refere to the plugin documentation for usage reference.
