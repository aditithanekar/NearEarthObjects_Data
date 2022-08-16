"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, 'r') as infile:
        neos=[]
        reader = csv.DictReader(infile)
        for elem in reader:
            neo=NearEarthObject(designation=elem['pdes'])
            if elem['name']!= '':
                neo.name= elem['name']
            if elem['diameter']!= '':
                neo.diameter= float(elem['diameter'])
            if elem['pha']=='Y':
                neo.hazardous=True
                
            neos.append(neo)
        return neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as incad:
        ca_list=[]
        ca_data= json.load(incad)
        for i in range(len(ca_data["data"])):
            ca=CloseApproach(_designation=ca_data["data"][i][0], time=ca_data["data"][i][3], distance=float(ca_data["data"][i][4]), velocity=float(ca_data["data"][i][7]))
            ca_list.append(ca)
        return ca_list
