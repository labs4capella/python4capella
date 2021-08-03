# Content
In this folder, you will find:
 - **/Capella Light Metamodel**: the Capella model which defines the simplified metamodel for Python4Capella
 - **/M2Doc generation**: a M2Doc project to generate documentation of the simplified metamodel from the previous Capella model
 - **/User Scripts Need definition**: the definition of user needs regarding import / export of data (used to define sample scripts)
 - **/org.eclipse.python4capella.implementation.status.update**: a plugin to allow import and update of implementation status in the Capella model
 - **/org.eclipse.python4capella.m2doc.service**: a plugin required for the M2Doc generation

# How-To generate simplified metamodel
To generate the documentation of the simplified metamodel, you need a Capella 5.0.0 with M2Doc installed (M2Doc 3.1.1 for Capella 5.0.x).

You then need to execute a runtime with the plugin org.eclipse.python4capella.m2doc.service, or you need to build and deploy this plugin.

Finally, you need to import the project "Capella Light Metamodel" with the Capella model, and the project "M2Doc generation" with the M2Doc template and configuration. In this project, execute the documentation generation using right click on the genconf file, Generate Documentation.

# How-To update implementation status
The Capella model defining the simplified metamodel also contains information about the implementation status.
This information is automatically updated based on the result of execution of the automated tests on the Python API.

To update the implementation status in the Capella model you need to have Capella 5.0.0 and execute a runtime with the plugin org.eclipse.python4capella.implementation.status.update, or you need to build and deploy this plugin.

With this plugin, you will then have a new menu when using a right click on the element SystemEngineering of the Capella model (of the simplified metamodel).
The new menu is called Python4Capella / Update Implementation Statuses.

Using this command, the tool will ask you to select a xml file. You need to select the xml file with the export of the tests results.
The tool will analyze the xml file and show the result of the update of implementation status with a diff / merge window. To validate the update of the status, you need to transfer the modifications in the Capella model
