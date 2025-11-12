'''
This script allows to extract a table with:
 - the list of NodePC
 - the summary of the NodePC
 - for each NodePC its PhysicalPorts
 - for each PhysicalPort its direction (defined as the direction of the ComponentPort allocated to the PhysicalPort)
 - the physical link(s) connected to the PhysicalPort
 
 It will create a folder result in the selected Capella project with the resulting xlsx file.
'''
# To run it:
#  - enable Developer capabilities if not already done (see documentation in the help menu)
#  - you can run this script by launching the contextual menu "Run As / EASE Script..." 
#    on this script. 
#    - By default, the model selected is IFE sample (aird path of the model written below)

#  - you can also run this script according to a configuration (script selected, arguments) 
#    and modify the configuration by launching the contextual menu "Run As / Run configurations..." 
#    on this script. 
#    - create a new "EASE Script" configuration
#    - define the name of the configuration: "Export_table_for_Node_PC_with_summary_PP_and_PL_to_xlsx.py" (for instance)
#    - define the Script Source path: "workspace://Python4Capella/sample_scripts/Export_table_for_Node_PC_with_summary_PP_and_PL_to_xlsx.py"
#


# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *
    
# include needed for utilities
include('workspace://Python4Capella/utilities/CapellaPlatform.py')
if False:
    from utilities.CapellaPlatform import *

# include needed to read/write xlsx files
from openpyxl import *

# change this path to execute the script on your model (here is the IFE sample). 
# comment it if you want to use the "Run configuration" instead
aird_path = '/In-Flight Entertainment System/In-Flight Entertainment System.aird'

'''
#Here is the "Run Configuration" part to uncomment if you want to use this functionality :

#check parameter numbers
if len(argv) != 1:
    # use IFE default values
    aird_path = "/In-Flight Entertainment System/In-Flight Entertainment System.aird"
else:
    # Load the Capella model from the first argument of the script
    aird_path = argv[0]
'''

model = CapellaModel()
model.open(aird_path)

# gets the SystemEngineering and print its name
se = model.get_system_engineering()
print('starting export of model ' + se.get_name())

# preparing excel file export
project_name = aird_path[0:(aird_path.index("/", 1) + 1)]
project = CapellaPlatform.getProject(project_name)
folder = CapellaPlatform.getFolder(project, 'results')
CapellaPlatform.getAbsolutePath(folder)
xlsx_file_name = CapellaPlatform.getAbsolutePath(folder) + '/' + 'Export_table_for_Node_PC_with_summary_PP_and_PL_to_xlsx.xlsx'
# create a workbook
workbook = Workbook()


# writing excel file header
worksheet = workbook.active
worksheet.title = 'PA export'
worksheet["A1"] = 'NodePC name'
worksheet["B1"] = 'NodePC summary'
worksheet["C1"] = 'ComponentPort name'
worksheet["D1"] = 'direction'
worksheet["E1"] = 'PhysicalLink name'

i=2

# retrieving elements from the model
for npc in se.get_all_contents_by_type(NodePC):
    #: :type npc: NodePC
    for pp in npc.get_contained_physical_ports():
        #: :type pp: PhysicalPort
        # for this script, we consider only the first component port allocated to the physical port
        cp = None
        if len(pp.get_allocated_component_ports()) > 0:
            cp = pp.get_allocated_component_ports()[0]
        for pl in pp.get_physical_links():
            #: :type pl: PhysicalLink
            worksheet["A" + str(i)] = npc.get_name()
            worksheet["B" + str(i)] = npc.get_summary()
            worksheet["C" + str(i)] = pp.get_name()
            if cp is not None:
                worksheet["D" + str(i)] = cp.get_orientation()
            worksheet["E" + str(i)] = pl.get_name()
            i = i + 1
        

# Save the xlsx file
workbook.save(xlsx_file_name)

print('saving excel file')

# refresh 
CapellaPlatform.refresh(folder)
