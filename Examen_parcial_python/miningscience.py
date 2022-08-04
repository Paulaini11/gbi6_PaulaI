import csv
import pandas as pd
import re
import matplotlib.pyplot as plt

def download_pubmed(keyword): 
    """ Función que extrae listado de artículos desde pubmed """
    
     
    from Bio import Entrez
 
    
    Entrez.email = "paula.iniguez@est.ikiam.edu.ec"
    Entr=Entrez.read(Entrez.esearch(db="pubmed",
                        term= keyword,
                        usehistory="y"))
    
    webenv=Entr["WebEnv"]
    query_key=Entr["QueryKey"]
    hand1=Entrez.efetch(db="pubmed",
                      rettype='medline',
                      retmode="text",
                      retstart=0,
                      retmax=543, webenv=webenv, query_key=query_key)
    out_hand1 = open(keyword+".txt", "w")
    p=hand1.read()
    out_hand1.write(p)
    out_hand1.close()
    hand1.close()
    return p

def map_science():
    import os
    os.getcwd()

    with open("Biohydrogen.txt") as f:
        my_text = f.read()
    my_text= re.sub(r'\n\s{6}', ' ', my_text)

    zipcodes = re.findall(r'[A-Z]{2}\s(\d{5}), USA', my_text)
    unique_zipcodes = list(set(zipcodes))
    unique_zipcodes.sort()


    import pgeocode
    zip_lat_long = pgeocode.Nominatim('US').query_postal_code(unique_zipcodes)
    zip_lat_long = zip_lat_long.to_dict()

    zip_code = zip_lat_long['postal_code'].values()
    zip_long = zip_lat_long['longitude'].values()
    zip_lat = zip_lat_long['latitude'].values()
    zip_count = []
    for i in zip_lat_long['postal_code'].values():
        a = zipcodes.count(i)
        zip_count.append(a)


    import matplotlib.pyplot as plt
    %matplotlib inline
    plt.scatter(zip_long, zip_lat, s = zip_count, c= zip_count)
    plt.colorbar()
    params = plt.gcf()
    plSize = params.get_size_inches()
    params.set_size_inches( (plSize[0] * 3, plSize[1] * 3) )
    plt.show()
    