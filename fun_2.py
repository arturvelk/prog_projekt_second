import streamlit as st
import pandas as pd
import folium
from shapely.geometry import Polygon, mapping
import json
from streamlit_folium import folium_static 
import s3fs
import os

fs = s3fs.S3FileSystem(anon=False)

#@st.experimental_memo(ttl=600)

def read_file(filename):
    with fs.open(filename) as f:
        return f.read().decode("utf-8")

def read_json(filename):
    return json.loads(read_file(filename))


data_district_90 = read_json("s3://election-sara-artur/val_90_megye.json")
data_district_94 = read_json("s3://election-sara-artur/val_94_megye.json")
data_district_98 = read_json("s3://election-sara-artur/val_98_megye.json")
data_district_02 = read_json("s3://election-sara-artur/val_02_megye.json")
data_district_06 = read_json("s3://election-sara-artur/val_06_megye.json")
data_district_10 = read_json("s3://election-sara-artur/val_10_megye.json")
data_district_14 = read_json("s3://election-sara-artur/val_14_megye.json")
data_district_18 = read_json("s3://election-sara-artur/val_18_megye.json")

data_jaras_90 = read_json("s3://election-sara-artur/val_90_jaras.json")
data_jaras_94 = read_json("s3://election-sara-artur/val_94_jaras.json")
data_jaras_98 = read_json("s3://election-sara-artur/val_98_jaras.json")
data_jaras_02 = read_json("s3://election-sara-artur/val_02_jaras.json")
data_jaras_06 = read_json("s3://election-sara-artur/val_06_jaras.json")
data_jaras_10 = read_json("s3://election-sara-artur/val_10_jaras.json")
data_jaras_14 = read_json("s3://election-sara-artur/val_14_jaras.json")
data_jaras_18 = read_json("s3://election-sara-artur/val_18_jaras.json")

data_pest_90 = read_json("s3://election-sara-artur/val_90_pest.json")
data_pest_94 = read_json("s3://election-sara-artur/val_94_pest.json")
data_pest_98 = read_json("s3://election-sara-artur/val_98_pest.json")
data_pest_02 = read_json("s3://election-sara-artur/val_02_pest.json")
data_pest_06 = read_json("s3://election-sara-artur/val_06_pest.json")
data_pest_10 = read_json("s3://election-sara-artur/val_10_pest.json")
data_pest_14 = read_json("s3://election-sara-artur/val_14_pest.json")
data_pest_18 = read_json("s3://election-sara-artur/val_18_pest.json")

def highlight_style(feature): 
    """
    style_function for when choropleth button
    is highighted
    """
    return {'fillOpacity': 1,
         'weight': 1}

def state_style_90(state,data,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data[state]
    
    #Set state colour
    if not state_result:
        color = "#000000"
    elif max(state_result, key=state_result.get) == "SZDSZ":
        color =  "#0783c7"#blue
    elif max(state_result, key=state_result.get) == "FKGP":
        color = "#445f2b"
    elif max(state_result, key=state_result.get) == "MDF":
        color = "#3c8a5a"
    elif max(state_result, key=state_result.get) == "MSZP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style


def state_style_94(state,data,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data[state]
    
    #Set state colour
    if not state_result:
        color = "#000000"
    elif max(state_result, key=state_result.get) == "SZDSZ":
        color =  "#0783c7"#blue
    elif max(state_result, key=state_result.get) == "MSZP":
        color =  "#E71A29"  
    elif max(state_result, key=state_result.get) == "MDF":
        color = "#3C8A5A"
    elif max(state_result, key=state_result.get) == "FKGP":
        color = "#445F2B" #red
    elif max(state_result, key=state_result.get) == "FIDESZ":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def state_style_98(state,data,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data[state]
    
    #Set state colour
    if not state_result:
        color = "#000000"
    elif max(state_result, key=state_result.get) == "SZDSZ":
        color =  "#0783c7"#blue
    elif max(state_result, key=state_result.get) == "FKGP":
        color = "#445f2b"
    elif max(state_result, key=state_result.get) == "MIÉP":
        color = "#9E863E"
    elif max(state_result, key=state_result.get) == "MSZP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style


def state_style_02(state,data,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data[state]
    
    #Set state colour
    if not state_result:
        color = "#000000"
    elif max(state_result, key=state_result.get) == "SZDSZ":
        color =  "#0783c7"#blue
    elif max(state_result, key=state_result.get) == "CENTRUM":
        color = "#c6adb3"
    elif max(state_result, key=state_result.get) == "MIÉP":
        color = "#9E863E"
    elif max(state_result, key=state_result.get) == "MSZP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ-MDF":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def state_style_06(state,data,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data[state]
    
    #Set state colour
    if not state_result:
        color = "#000000"
    elif max(state_result, key=state_result.get) == "SZDSZ":
        color =  "#0783c7"#blue
    elif max(state_result, key=state_result.get) == "MDF":
        color = "#3C8A5A"
    elif max(state_result, key=state_result.get) == "MIÉP-JOBBIK":
        color = "#9E863E"
    elif max(state_result, key=state_result.get) == "MSZP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ-KDNP":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style


def state_style_10(state,data,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data[state]
    
    #Set state colour
    if not state_result:
        color = "#000000"
    elif max(state_result, key=state_result.get) == "LMP":
        color =  "#73c92d"#blue
    elif max(state_result, key=state_result.get) == "MDF":
        color = "#3C8A5A"
    elif max(state_result, key=state_result.get) == "JOBBIK":
        color = "#008371"
    elif max(state_result, key=state_result.get) == "MSZP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ-KDNP":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def state_style_14(state,data,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data[state]
    
    #Set state colour
    if not state_result:
        color = "#000000"
    elif max(state_result, key=state_result.get) == "LMP":
        color =  "#73c92d"#blue
    elif max(state_result, key=state_result.get) == "A HAZA NEM ELADÓ":
        color = "#BF3F3F"
    elif max(state_result, key=state_result.get) == "JOBBIK":
        color = "#008371"
    elif max(state_result, key=state_result.get) == "MSZP-EGYÜTT-DK-PM-MLP":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ-KDNP":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style

def state_style_18(state,data,function=False):
    """
    Returns the style for a state in a given year
    """
    
    state_result = data[state]
    
    #Set state colour
    if not state_result:
        color = "#000000"
    elif max(state_result, key=state_result.get) == "LMP":
        color =  "#73c92d"#blue
    elif max(state_result, key=state_result.get) == "DK":
        color = "#007FFF"
    elif max(state_result, key=state_result.get) == "JOBBIK":
        color = "#008371"
    elif max(state_result, key=state_result.get) == "MSZP-PM":
        color = '#e71a29' #red
    elif max(state_result, key=state_result.get) == "FIDESZ-KDNP":
        color = "#fd8100"
        
    
    #Set state style
    if function == False:
        # Format for style_dictionary
        state_style = {
            'opacity': 0.8,
            'color': color,
            "highlight" : True
        } 
    else:
        # Format for style_function
        state_style = {
             'fillOpacity': 0.8,
             'weight': 1,
             'fillColor': color,
             'color': '#000000',
             "highlight" : True}    
  
    return state_style


### Most jönnek a járás, pest, megye különbségek

def style_function_jaras_90(feature):
    """
    style_function used by the GeoJson folium function
    """

    state = feature['properties']['name']
    style = state_style_90(state,data_jaras_90,function=True)
    
    return style

def style_function_jaras_94(feature):

    state = feature['properties']['name']
    style = state_style_94(state,data_jaras_94,function=True)
    
    return style

def style_function_jaras_98(feature):

    state = feature['properties']['name']
    style = state_style_98(state,data_jaras_98,function=True)
    
    return style

def style_function_jaras_02(feature):

    state = feature['properties']['name']
    style = state_style_02(state,data_jaras_02,function=True)
    
    return style

def style_function_jaras_06(feature):

    state = feature['properties']['name']
    style = state_style_06(state,data_jaras_06,function=True)
    
    return style

def style_function_jaras_10(feature):

    state = feature['properties']['name']
    style = state_style_10(state,data_jaras_10,function=True)
    
    return style

def style_function_jaras_14(feature):

    state = feature['properties']['name']
    style = state_style_14(state,data_jaras_14,function=True)
    
    return style

def style_function_jaras_18(feature):

    state = feature['properties']['name']
    style = state_style_18(state,data_jaras_18,function=True)
    
    return style

#Megyék

def style_function_megye_90(feature):

    state = feature['properties']['NAME_1']
    style = state_style_90(state,data_district_90,function=True)
    
    return style

def style_function_megye_94(feature):

    state = feature['properties']['NAME_1']
    style = state_style_94(state,data_district_94,function=True)
    
    return style

def style_function_megye_98(feature):

    state = feature['properties']['NAME_1']
    style = state_style_98(state,data_district_98,function=True)
    
    return style

def style_function_megye_02(feature):

    state = feature['properties']['NAME_1']
    style = state_style_02(state,data_district_02,function=True)
    
    return style

def style_function_megye_06(feature):

    state = feature['properties']['NAME_1']
    style = state_style_06(state,data_district_06,function=True)
    
    return style

def style_function_megye_10(feature):

    state = feature['properties']['NAME_1']
    style = state_style_10(state,data_district_10,function=True)
    
    return style

def style_function_megye_14(feature):

    state = feature['properties']['NAME_1']
    style = state_style_14(state,data_district_14,function=True)
    
    return style

def style_function_megye_18(feature):

    state = feature['properties']['NAME_1']
    style = state_style_18(state,data_district_18,function=True)
    
    return style

#Pest

def style_function_pest_90(feature):

    state = feature['properties']['name']
    style = state_style_90(state,data_pest_94,function=True)
    
    return style
def style_function_pest_94(feature):

    state = feature['properties']['name']
    style = state_style_94(state,data_pest_94,function=True)
    
    return style

def style_function_pest_98(feature):

    state = feature['properties']['name']
    style = state_style_98(state,data_pest_98,function=True)
    
    return style
def style_function_pest_02(feature):

    state = feature['properties']['name']
    style = state_style_02(state,data_pest_02,function=True)
    
    return style

def style_function_pest_06(feature):

    state = feature['properties']['name']
    style = state_style_06(state,data_pest_06,function=True)
    
    return style

def style_function_pest_10(feature):

    state = feature['properties']['name']
    style = state_style_10(state,data_pest_10,function=True)
    
    return style

def style_function_pest_14(feature):

    state = feature['properties']['name']
    style = state_style_14(state,data_pest_14,function=True)
    
    return style

def style_function_pest_18(feature):

    state = feature['properties']['name']
    style = state_style_18(state,data_pest_18,function=True)
    
    return style