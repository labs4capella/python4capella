'''
This script extracts the Description fields (HTML) from all Capella model elements 

And format it as nicely as possible in Excel cells

@author: slacrampe
'''
# To run it:
#  - MAKE SURE xlsxwriter is installed (if not, open a cmd window and type 'pip install XlsxWriter')
#  - enable Developer capabilities if not already done (see documentation in the help menu)
#  - you can run this script by launching the contextual menu "Run As / EASE Script..." 
#    on this script. 
#    - By default, the model selected is IFE sample (aird path of the model written below)

#  - you can also run this script according to a configuration (script selected, arguments) 
#    and modify the configuration by launching the contextual menu "Run As / Run configurations..." 
#    on this script. 
#    - create a new "EASE Script" configuration
#    - define the name of the configuration: "Export_list_of_functional_exchanges_to_xlsx.py" (for instance)
#    - define the Script Source path: "workspace://Python4Capella/sample_scripts/Export_list_of_functional_exchanges_to_xlsx.py"
#
#

# include needed for the Capella modeller API
include('workspace://Python4Capella/simplified_api/capella.py')
if False:
    from simplified_api.capella import *

# include needed for converting HTML to Excel cells
include('workspace://Python4Capella/utilities/HTML_RichText_Converter.py')
if False:
    from utilities.HTML_RichText_Converter import *

# include needed for this script and the HTML_RichText_Converter one
import xlsxwriter

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

############################################################
# Initializing the excel file
############################################################
project_name = aird_path[0:(aird_path.index("/", 1) + 1)]
project = CapellaPlatform.getProject(project_name)
folder = CapellaPlatform.getFolder(project, 'results')
xlsx_file_name = CapellaPlatform.getAbsolutePath(folder) + '/' + 'Export_description.xlsx'
workbook = xlsxwriter.Workbook(xlsx_file_name)  
#Creating the worksheet
worksheet = workbook.add_worksheet('Elements Description')
#Creating the default format (text will be wrapped)
cell_format = workbook.add_format()
cell_format.set_text_wrap()
# writing excel file header
worksheet.set_column('A:A', 50)
worksheet.set_column('B:C', 100)
worksheet.write("A1",'Element Name') 
worksheet.write("B1", 'HTML Description')
worksheet.write("C1", 'Rich Text Description')
############################################################

i=2
# retrieving all Capella model elements from the model
for elem in se.get_all_contents_by_type(CapellaElement):
    if elem.get_description() != None and len(elem.get_description())>0 and len(elem.get_description().strip())>0 :
        print("processing: "+ elem.get_name())
        worksheet.write("A" + str(i),elem.get_name(), cell_format)
        worksheet.write("B" + str(i), elem.get_description(), cell_format)
        #This is where the HTML gets converted to Excel cell
        HTML_RichText_Converter.write_cell(elem.get_description(), "C" + str(i), workbook, worksheet, cell_format)                              
        i = i+1

workbook.close()
print('saving excel file: '+ xlsx_file_name)
CapellaPlatform.refresh(folder)