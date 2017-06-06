#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 15:22:52 2017

@author: priyankadesouza
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 10:55:57 2017

@author: priyankadesouza
"""

import os
import MisrToolkit as Mtk
import numpy as np 
  
def run(FILE_NAME):
        pre_FILE_NAME="/Volumes/My Passport/MISR/"
        FN=pre_FILE_NAME+FILE_NAME
        gridname="RegParamsPerMixture"
        print(gridname)
        f1 = open('Mixtures_final_UNEP.csv', 'a+')
        f2 = open('Mixtures_final_Alliance.csv', 'a+')
        f3 = open('Mixtures_final_Scholastica.csv', 'a+')
        f4 = open('Mixtures_final_KGSA.csv', 'a+')
        f5 = open('Mixtures_final_AllSaints.csv', 'a+')
        colheader="File Name"+" ,"+ "1" +" ,"+ "2"+" ,"+ "3"+" ,"+ "4"+" ,"+ "5"+" ,"+ "\n"
        f1.write(colheader)
        f2.write(colheader)
        f3.write(colheader)
        f4.write(colheader)
        f5.write(colheader)
        print("writing header to the file")
        
        #167,168,169,170: Path list
        path=int(FILE_NAME[21:24])
#UNEP site: (-1.232873, 36.814971)
#Alliance: (-1.265285, 36.662683)
#St Scholastica: (-1.253113, 36.856531)
#KGSA: (-1.311156, 36.786974)
#All Saints: (-1.310663, 36.810548)
        region_unep=Mtk.MtkRegion(-1.232873, 36.814971, 10.0,10.0, 'm')
        region_alliance=Mtk.MtkRegion(-1.265285, 36.662683, 10.0, 10.0, 'm')
        region_scholastica=Mtk.MtkRegion(-1.253113, 36.856531, 10.0, 10.0, 'm')
        region_kgsa=Mtk.MtkRegion(-1.311156, 36.856531, 10.0, 10.0, 'm')
        region_allsaints=Mtk.MtkRegion(-1.310663, 36.810548, 10.0, 10.0, 'm')
        map_info_unep=region_unep.snap_to_grid(path, 17600)
        map_info_alliance=region_alliance.snap_to_grid(path, 17600)
        map_info_scholastica=region_scholastica.snap_to_grid(path, 17600)
        map_info_kgsa=region_kgsa.snap_to_grid(path, 17600)
        map_info_allsaints=region_allsaints.snap_to_grid(path, 17600)

        
        m=Mtk.MtkFile(FN)
        flag=True
        if(gridname in m.grid_list):
                flag=True
        else:
                flag=False
        if (flag==False):
            return

        lat,lon=map_info_unep.create_latlon()
        outstring1=FILE_NAME+" ,"
        outstring2=FILE_NAME+" ,"
        outstring3=FILE_NAME+" ,"
        outstring4=FILE_NAME+" ,"

        for i in range(0,74):
            fieldname1='OptDepthPerMixture['+ str(i)+']'
            fieldname2='AerRetrSuccFlag['+str(i)+']'
            d1=m.grid(gridname).field(fieldname1).read(region_unep)
            d2=m.grid(gridname).field(fieldname1).read(region_unep)
            n1=d1.data()
            n2=d2.data()
            
            nlines=n1.shape[0]
            nsamples=n1.shape[1]
            print(nsamples)
            outstring1=outstring1+ " ,"+ str(n1[0,0])+" ,"+str(n2[0,0])

        outstring1=outstring1+" ,"+str(lat[0,0])+", "+str(lon[0,0])

        outstring=outstring1+"\n"
        print(outstring)
        f1.write(outstring)

        lat,lon=map_info_alliance.create_latlon()
        outstring1=FILE_NAME+" ,"
        outstring2=FILE_NAME+" ,"
        outstring3=FILE_NAME+" ,"
        outstring4=FILE_NAME+" ,"
        
        for i in range(0,74):
            fieldname1='OptDepthPerMixture['+ str(i)+']'
            fieldname2='AerRetrSuccFlag['+str(i)+']'
            d1=m.grid(gridname).field(fieldname1).read(region_alliance)
            d2=m.grid(gridname).field(fieldname1).read(region_alliance)
            n1=d1.data()
            n2=d2.data()
            
            nlines=n1.shape[0]
            nsamples=n1.shape[1]
            outstring1=outstring1+ " ,"+ str(n1[0,0])+" ,"+str(n2[0,0])

        outstring1=outstring1+" ,"+str(lat[0,0])+", "+str(lon[0,0])

        outstring=outstring1+"\n"
        print(outstring)
        f2.write(outstring)

        lat,lon=map_info_scholastica.create_latlon()
        outstring1=FILE_NAME+" ,"
        outstring2=FILE_NAME+" ,"
        outstring3=FILE_NAME+" ,"
        outstring4=FILE_NAME+" ,"
        
        for i in range(0,74):
            fieldname1='OptDepthPerMixture['+ str(i)+']'
            fieldname2='AerRetrSuccFlag['+str(i)+']'
            d1=m.grid(gridname).field(fieldname1).read(region_scholastica)
            d2=m.grid(gridname).field(fieldname1).read(region_scholastica)
            n1=d1.data()
            n2=d2.data()
            
            nlines=n1.shape[0]
            nsamples=n1.shape[1]
            outstring1=outstring1+ " ,"+ str(n1[0,0])+" ,"+str(n2[0,0])

        outstring1=outstring1+" ,"+str(lat[0,0])+", "+str(lon[0,0])

        outstring=outstring1+"\n"
        print(outstring)
        f3.write(outstring)

        lat,lon=map_info_kgsa.create_latlon()
        outstring1=FILE_NAME+" ,"
        outstring2=FILE_NAME+" ,"
        outstring3=FILE_NAME+" ,"
        outstring4=FILE_NAME+" ,"
        
        for i in range(0,74):
            fieldname1='OptDepthPerMixture['+ str(i)+']'
            fieldname2='AerRetrSuccFlag['+str(i)+']'
            d1=m.grid(gridname).field(fieldname1).read(region_kgsa)
            d2=m.grid(gridname).field(fieldname1).read(region_kgsa)
            n1=d1.data()
            n2=d2.data()
            
            nlines=n1.shape[0]
            nsamples=n1.shape[1]
            outstring1=outstring1+ " ,"+ str(n1[0,0])+" ,"+str(n2[0,0])

        outstring1=outstring1+" ,"+str(lat[0,0])+", "+str(lon[0,0])

        outstring=outstring1+"\n"
        print(outstring)
        f4.write(outstring)

        lat,lon=map_info_allsaints.create_latlon()
        outstring1=FILE_NAME+" ,"
        outstring2=FILE_NAME+" ,"
        outstring3=FILE_NAME+" ,"
        outstring4=FILE_NAME+" ,"
        
        for i in range(0,74):
            fieldname1='OptDepthPerMixture['+ str(i)+']'
            fieldname2='AerRetrSuccFlag['+str(i)+']'
            d1=m.grid(gridname).field(fieldname1).read(region_allsaints)
            d2=m.grid(gridname).field(fieldname1).read(region_allsaints)
            n1=d1.data()
            n2=d2.data()
            
            nlines=n1.shape[0]
            nsamples=n1.shape[1]
            outstring1=outstring1+ " ,"+ str(n1[0,0])+" ,"+str(n2[0,0])

        outstring1=outstring1+" ,"+str(lat[0,0])+", "+str(lon[0,0])

        outstring=outstring1+"\n"
        print(outstring)
        f5.write(outstring)





if __name__ == "main":
    
#    os.chdir("/Volumes/My Passport/062319526211867")
    fileList=open('/Users/priyankadesouza/Downloads/fileList.txt','r')
    
    for line in fileList:
        
        FILE_NAME = str(line.strip())
        print(FILE_NAME)
        run(FILE_NAME)
