#uses plotly dash application for output, pandas for data manipulation, climb class for object class storage, and conditionalstyle to run through dash conditional formatting for each cell
from dash import Dash, html, dash_table
import dash_bootstrap_components as dbc
import pandas as pd
import climbclass
from conditionalstyle import *
from  url_index import store_urls

#initializes all the class instance objects for every location
NorB = climbclass.ClimbLocation("North Bend Exit 32/38", 47.49, -121.78)
# LaC = climbclass.ClimbLocation("Lake Cushman",47.499,-123.291)
# Van = climbclass.ClimbLocation("Vantage",47.025,-119.967)
# GdB = climbclass.ClimbLocation("Gold Bar",47.845,-121.627)
# LnW = climbclass.ClimbLocation("LeavenWorth",47.545,-120.734)
# Sqm = climbclass.ClimbLocation("Squamish",49.687,-123.136)
# SRk = climbclass.ClimbLocation("Smith Rock",44.363,-121.146)
# Maz = climbclass.ClimbLocation("Mazama", 48.608,-120.401)
# Tet = climbclass.ClimbLocation("Tieton River", 46.724,-120.809)
# MtE = climbclass.ClimbLocation("Mount Erie", 48.460, -122.625)


#Creates a dictionary with the str variable and object class

url_dict = {'NorB':[]}
#             ,'LaC':[],'Van':[],'GdB':[], 'LnW':[],
#             'Sqm':[], 'SRk':[], 'Maz':[], 'Tet':[], 'MtE':[]}
Var_Dict = {'NorB':NorB}
#             'LaC':LaC,'Van':Van,'GdB': GdB, 'LnW': LnW,
# #             'Sqm': Sqm, 'SRk': SRk, 'Maz':Maz, 'Tet':Tet, 'MtE':MtE}


#copies similar dictionary to store dataframes, column headers, data under header, and 
df_dict = Var_Dict.copy()
col_dict = Var_Dict.copy()
data_dict = Var_Dict.copy()
index_dict = Var_Dict.copy()

url_dict = store_urls(url_dict)
# function to convert pandas dataframe to formatted col headers and data so that it plots correctly in dash datatable
def df_to_dash(df):
  # create list format for the top two rows
  header=list(df.iloc[0])
  index= list(df.iloc[1])
  #combines both list into tuple pairs
  combindex =[[header[i], index[i]] for i in range(0, len(header))]
  #generates a dictionary for the columns and Id's this supports mutli header in Dash
  columns = [{'id': c, 'name': d} for (c,d) in zip(index,combindex)]
  df.columns = df.iloc[1]
  #removes header for the data section
  df1 = df[2:]
  #creates dictionary using the second row header for the unique ID
  data = df1.to_dict('records')
  return (columns,data,index)

#creates a seperate pandas dataframe for each climbing location, transposes and uses CSV to format data. (needed index column as first column)
for i, var in df_dict.items():
  df_dict[i] = pd.DataFrame(var.requestforcast()).transpose()
  df_dict[i].to_csv(f"{i}.csv")
  df_dict[i]= pd.read_csv(f"{i}.csv")
  
#creates dictionaries for the formatted columns and data for dash  
col_dict = df_dict.copy()
data_dict =df_dict.copy() 

#loops through dictionary, calls function to convert to dash format and store the return information in indexed dictionaries for easy callback
for i, var in col_dict.items():
  cols,data,index = df_to_dash(col_dict[i])
  col_dict[i] = cols
  data_dict[i] = data
  index_dict[i] = index

# #starts Dash App
app = Dash(__name__)

# #starts the code for the app layout this plots to a plotly dash app, it wil create a title, then headers and a conditionally plotted table with forcast and last 48 hours
app.layout = html.Div( children =[
    #main title
    html.H1(children="Climbing Weather Forcasts for PNW Locations", style = {'text-align':'center' ,'fontWeight': 'bold'}),

  #for each table give an H1 title, lat and lon info, 48 rainfall, Links to weather forcasts, pulls the col and data dictionary info, and pulls conditional formatting data for each cell.
    html.H1(children=f"{NorB.name} "),
    html.Div(children= f"Lat: {NorB.lat} and Lon:{NorB.lon}",style = {'fontWeight':'bold','display': 'inline-block'}), 
    # html.Div(children= f"Rain last 48 Hr's: {NorB.accumrain} in", style = {'fontWeight':'bold','display': 'inline-block',"margin-left": "100px", 'fontSize': '20px'}),
    html.A("Weather.gov NWS 7-day Forecast", href=f"{url_dict['NorB'][0][0]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
    html.A("Weather.com 10-day Forecast", href=f"{url_dict['NorB'][0][1]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  html.A("Accuweather Multi index Forecast", href=f"{url_dict['NorB'][0][2]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
    dash_table.DataTable(
               style_header = { 'textAlign': 'center' ,'fontWeight': 'bold','overflow':'auto'},  
               data=data_dict['NorB'],     
               columns=col_dict["NorB"],
               merge_duplicate_headers=True,
               style_data_conditional=(style_all(index_dict['NorB']))),
#   # Lake Cushman table
#     html.H1(children=f"{LaC.name} "),
#     html.Div(children= f"Lat: {LaC.lat} and Lon:{LaC.lon} Rain last 48 Hr's:   {LaC.accumrain} in", style = {'fontWeight':'bold'}),
#     html.A("Weather.gov NWS 7-day Forecast", href=f"{url_dict['LaC'][0][0]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
#     html.A("Weather.com 10-day Forecast", href=f"{url_dict['LaC'][0][1]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
#      html.A("Accuweather Multi index Forecast", href=f"{url_dict['LaC'][0][2]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
# #     dash_table.DataTable(
#                style_header = { 'textAlign': 'center' ,'fontWeight': 'bold' },
#                data=data_dict['LaC'],     
#                columns=col_dict["LaC"],
#                merge_duplicate_headers=True,
#                style_data_conditional=(style_all(index_dict['LaC']))),
#    # Vantage table
#     html.H1(children=f"{Van.name} "),
#     html.Div(children= f"Lat: {NorB.lat} and Lon:{Van.lon}  Rain last 48 Hr's:   {Van.accumrain} in", style = {'fontWeight':'bold'}),
  #     html.A("Weather.gov NWS 7-day Forecast", href=f"{url_dict['Van'][0][0]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  #   html.A("Weather.com 10-day Forecast", href=f"{url_dict['Van'][0][1]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  # html.A("Accuweather Multi index Forecast", href=f"{url_dict['Van'][0][2]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
#     dash_table.DataTable(
#               style_header = { 'textAlign': 'center' ,'fontWeight': 'bold' },
#                data=data_dict['Van'],     
#                columns=col_dict["Van"],
#                merge_duplicate_headers=True,
#                style_data_conditional=(style_all(index_dict['Van']))),
    
#     html.H1(children=f"{GdB.name} "),
#     html.Div(children= f"Lat: {GdB.lat} and Lon:{GdB.lon} Rain last 48 Hr's:   {GdB.accumrain} in", style = {'fontWeight':'bold'}),
      # html.A("Weather.gov NWS 7-day Forecast", href=f"{url_dict['GdB'][0][0]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  #   html.A("Weather.com 10-day Forecast", href=f"{url_dict['GdB'][0][1]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  # html.A("Accuweather Multi index Forecast", href=f"{url_dict['GdB'][0][2]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
#     dash_table.DataTable(
#               style_header = { 'textAlign': 'center' ,'fontWeight': 'bold' },
#                data=data_dict['GdB'],     
#                columns=col_dict["GdB"],
#                merge_duplicate_headers=True,
#                style_data_conditional=(style_all(index_dict['GdB']))),
#   # Leavenworth table
#     html.H1(children=f"{LnW.name} "),
#     html.Div(children= f"Lat: {LnW.lat} and Lon:{LnW.lon} Rain last 48 Hr's:   {LnW.accumrain} in", style = {'fontWeight':'bold'}),
  # html.A("Weather.gov NWS 7-day Forecast", href=f"{url_dict['LnW'][0][0]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  #   html.A("Weather.com 10-day Forecast", href=f"{url_dict['LnW'][0][1]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  # html.A("Accuweather Multi index Forecast", href=f"{url_dict['LnW'][0][2]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
#     dash_table.DataTable(
#               style_header = { 'textAlign': 'center' ,'fontWeight': 'bold' },
#                data=data_dict['LnW'],     
#                columns=col_dict["LnW"],
#                merge_duplicate_headers=True,
#                style_data_conditional=(style_all(index_dict['LnW']))),
  
#   # Squamish table
#     html.H1(children=f"{Sqm.name} "),
#     html.Div(children= f"Lat: {Sqm.lat} and Lon:{Sqm.lon} Rain last 48 Hr's:   {Sqm.accumrain} in", style = {'fontWeight':'bold'}),
  # html.A("Weather.gov NWS 7-day Forecast", href=f"{url_dict['Sqm'][0][0]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  #   html.A("Weather.com 10-day Forecast", href=f"{url_dict['Sqm'][0][1]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  # html.A("Accuweather Multi index Forecast", href=f"{url_dict['Sqm'][0][2]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
#     dash_table.DataTable(
#                style_header = { 'textAlign': 'center' ,'fontWeight': 'bold' },
#                data=data_dict['Sqm'],     
#                columns=col_dict["Sqm"],
#                merge_duplicate_headers=True,
#                style_data_conditional=(style_all(index_dict['Sqm']))),
#   #Smith Rock table
#     html.H1(children=f"{SRk.name} "),
#     html.Div(children= f"Lat: {SRk.lat} and Lon:{SRk.lon} Rain last 48 Hr's:   {SRk.accumrain} in", style = {'fontWeight':'bold'}),
  # html.A("Weather.gov NWS 7-day Forecast", href=f"{url_dict['SRk'][0][0]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  #   html.A("Weather.com 10-day Forecast", href=f"{url_dict['SRk'][0][1]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  # html.A("Accuweather Multi index Forecast", href=f"{url_dict['SRk'][0][2]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
#     dash_table.DataTable(
#                style_header = { 'textAlign': 'center' ,'fontWeight': 'bold' },
#                data=data_dict['SRk'],     
#                columns=col_dict["SRk"],
#                merge_duplicate_headers=True,
#                style_data_conditional=(style_all(index_dict['SRk']))),
#   # Mazama table
#     html.H1(children=f"{Maz.name} "),
#     html.Div(children= f"Lat: {Maz.lat} and Lon:{Maz.lon} ain last 48 Hr's:   {Maz.accumrain} in", style = {'fontWeight':'bold'}),
  # html.A("Weather.gov NWS 7-day Forecast", href=f"{url_dict['Maz'][0][0]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  #   html.A("Weather.com 10-day Forecast", href=f"{url_dict['Maz'][0][1]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  # html.A("Accuweather Multi index Forecast", href=f"{url_dict['Maz'][0][2]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
#     dash_table.DataTable(
#                style_header = { 'textAlign': 'center' ,'fontWeight': 'bold' },
#                data=data_dict['Maz'],     
#                columns=col_dict["Maz"],
#                merge_duplicate_headers=True,
#                style_data_conditional=(style_all(index_dict['Maz']))),
  
#     html.H1(children=f"{Tet.name} "),
#     html.Div(children= f"Lat: {Tet.lat} and Lon:{Tet.lon} Rain last 48 Hr's:   {Tet.accumrain} in", style = {'fontWeight':'bold'}),
  # html.A("Weather.gov NWS 7-day Forecast", href=f"{url_dict['Tet'][0][0]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  #   html.A("Weather.com 10-day Forecast", href=f"{url_dict['Tet'][0][1]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  # html.A("Accuweather Multi index Forecast", href=f"{url_dict['Tet'][0][2]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
#     dash_table.DataTable(
#                style_header = { 'textAlign': 'center' ,'fontWeight': 'bold' },
#                data=data_dict['Tet'],     
#                columns=col_dict["Tet"],
#                merge_duplicate_headers=True,
#                style_data_conditional=(style_all(index_dict['Tet']))),
  
#   #Mount Erie table
#     html.H1(children=f"{MtE.name} "),
#     html.Div(children= f"Lat: {MtE.lat} and Lon:{MtE.lon} Rain last 48 Hr's:   {MtE.accumrain} in", style = {'fontWeight':'bold'}),
  # html.A("Weather.gov NWS 7-day Forecast", href=f"{url_dict['MtE'][0][0]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  #   html.A("Weather.com 10-day Forecast", href=f"{url_dict['Mte'][0][1]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
  # html.A("Accuweather Multi index Forecast", href=f"{url_dict['Mte'][0][2]}", target="_blank", style = {'display': 'inline-block',"margin-left": "50px"}),
#     dash_table.DataTable(
#                style_header = { 'textAlign': 'center' ,'fontWeight': 'bold' },
#                data=data_dict['MtE'],     
#                columns=col_dict["MtE"],
#                merge_duplicate_headers=True,
#                style_data_conditional=(style_all(index_dict['MtE']))),
])
    
#calls and initiates server               
if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
