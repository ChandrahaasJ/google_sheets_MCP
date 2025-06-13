#load_dotenv(dotenv_path=r"C:\EAG\session8\assignment8\.env")
from mcp.server.fastmcp import FastMCP
from environments.loader import Auth
import sys
pth=r"C:\EAG\session8\assignment8\.env"
mcp=FastMCP("G_Sheets")

"""
              IMPORTANT
"""

path_to_env="REPLACE WITH ENV PATH"



@mcp.tool()
def list_sheets():
    """Listing the sheets available"""
    obj=Auth(path_to_env)
    sheets=obj.initialize_sheets()
    sheet=sheets[0]
    return sheet.worksheets()

@mcp.tool()
def locate_info(info):
    obj=Auth(path_to_env)
    sheets=obj.initialize_sheets()
    sheet=sheets[0]
    """ you can get the row and column number of the information you passed in the sheet"""
    info=info.upper()
    print(info)
    cells = sheet.findall(info) 
    if(len(cells)>1):
         return "multiple values found, specify more details"
    else:
         return [cells[0].row,cells[0].col]

@mcp.tool()
def get_number(name):
    """get the number of the contact"""
    obj=Auth(path_to_env)
    sheets=obj.initialize_sheets()
    sheet=sheets[0]
    name=name.upper()
    row,col=locate_info(name)
    ans=sheet.cell(row,col+1).value
    return ans
          

@mcp.tool()
def get_email(name):
    """get the email of the contact"""
    obj=Auth(path_to_env)
    sheets=obj.initialize_sheets()
    sheet=sheets[0]

    name=name.upper()
    row,col=locate_info(name)
    ans=sheet.cell(row,col+2).value
    return ans


@mcp.tool()
def add_contact(body):
    obj=Auth(path_to_env)
    sheets=obj.initialize_sheets()
    sheet=sheets[0]
    name=body["name"]
    number=body["number"]
    email=body["email"]
    cells = sheet.findall(name)
    if(len(cells)==0):
        sheet.append_row([name,number,email])
        return "contact added successfully"
    else:
         return "contact already exists, please specify the full name"


if __name__ == "__main__":
    
    print("mcp_server_1.py starting")
    
    
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
            mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution
        print("\nShutting down...")