#dash datatable is callable by column but not by row. Because dataframe was transposed I have to look through each each collumn and row index and create a conditional statment. This will color code the cell based on the value of the cell. Colors are CSS color format. Column ID = filter query. needed to only color indidivdual cell and not entire row.
def style_all(index):
  styleall = []
  n= len(index)
  for i in range (1,n):
    i = index[i]
    #rain <.01 F green
    styleall.append({
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 0,
                        'filter_query': f"{{{i}}} <.01" 
                      },
                      'backgroundColor': '#57cf5d',
                      'color': 'black'
                    },)
    #rain >=.01 - <.05 F yellow
    styleall.append({
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 0,
                        'filter_query': f"{{{i}}} >= .01 && {{{i}}} < .05" 
                      },
                      'backgroundColor': '#ffe76e',
                      'color': 'black'
                    },)
    #rain >.05 F red
    styleall.append({
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 0,
                        'filter_query': f"{{{i}}} >=.05" 
                      },
                      'backgroundColor': '#ff726e',
                      'color': 'black'
                    },)
    #Temp <=40 F red
    styleall.append({
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 1,
                        'filter_query': f"{{{i}}} <=40" 
                      },
                      'backgroundColor': '#ff726e',
                      'color': 'black'
                    },)
    #Temp >45 <=55F yellow
    styleall.append({
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 1,
                        'filter_query': f"{{{i}}} > 40 && {{{i}}} <=55" 
                      },
                      'backgroundColor': '#ffe76e',
                      'color': 'black'
                    },)
    #Temp >55F -80F green
    styleall.append({
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 1,
                        'filter_query': f"{{{i}}} > 55 && {{{i}}} <=80" 
                      },
                      'backgroundColor': '#57cf5d',
                      'color': 'black'
                    },)
    #Temp >80F -90F yellow
    styleall.append({
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 1,
                        'filter_query': f"{{{i}}} > 80 && {{{i}}} <=90" 
                      },
                      'backgroundColor': '#ffe76e',
                      'color': 'black'
                    },)
    #Temp >90F red
    styleall.append({
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 1,
                        'filter_query': f"{{{i}}} > 90" 
                      },
                      'backgroundColor': '#ff726e',
                      'color': 'black'
                    },)
    #Wind < 10 MPH Green
    styleall.append({
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 2,
                        'filter_query': f"{{{i}}} <=10" 
                      },
                      'backgroundColor': '#57cf5d',
                      'color': 'black'
                    },)
    
    #Wind 10 - 20 MPH yellow
    styleall.append(
                    {
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 2,
                        'filter_query': f"{{{i}}} > 10 && {{{i}}} <20" 
                      },
                      'backgroundColor': '#ffe76e',
                      'color': 'black'
                    },)
    #Wind > 20 mph red
    styleall.append(
                    {
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 2,
                        'filter_query': f"{{{i}}} >=20" 
                      },
                      'backgroundColor': '#ff726e',
                      'color': 'black'
                    },
                    )
    #cloud cover <20%
    styleall.append(
                    {
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 3,
                        'filter_query': f"{{{i}}} <=20" 
                      },
                      'backgroundColor': '#ebeded',
                      'color': 'black'
                    },
                    )
    #cloud cover 20 -50%
    styleall.append(
                    {
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 3,
                        'filter_query': f"{{{i}}} >20 && {{{i}}} <=50" 
                      },
                      'backgroundColor': '#c2c2c2',
                      'color': 'black'
                    },
                    )
     #cloud cover 50 - 70%
    styleall.append(
                    {
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 3,
                        'filter_query': f"{{{i}}} >50 && {{{i}}} <=70" 
                      },
                      'backgroundColor': '#a8a8a8',
                      'color': 'black'
                    },
                    )
    #cloud cover 70-100%
    styleall.append(
                    {
                      'if': {
                        'column_id': f"{i}",
                        'row_index': 3,
                        'filter_query': f"{{{i}}} >70 && {{{i}}} <=100" 
                      },
                      'backgroundColor': '#969292',
                      'color': 'black'
                    },
                    )
  return(styleall)

  
