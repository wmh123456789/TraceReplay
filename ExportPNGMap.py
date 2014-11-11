import os
import shutil
import da, mdb,gis
import arcpy
import xml.etree.ElementTree as ET

def SetExtent(df,xmin,xmax,ymin,ymax):
	newExtent = df.extent
	newExtent.XMin = xmin
	newExtent.YMin = ymin
	newExtent.XMax = xmax
	newExtent.YMax = ymax
	df.extent = newExtent


mxdfile = 'E:\MDBGenerate\= MDB_Modify_BJ\= ModifiedOK\MSRA\MSRA.mxd'
xmlfile = 'E:\MDBGenerate\= MDB_Modify_BJ\= ModifiedOK\MSRA\Binary\MSRA.Floor2F.xml'

layer = gis.ParseStandardMapXMLFile(xmlfile)

print str(layer.getbound())

xmin,xmax,ymin,ymax = layer.getbound()

imgh = int((ymax-ymin)*10.0+200*2)
imgw = int((xmax-xmin)*10.0+200*2)
print imgw,imgh

mxd = arcpy.mapping.MapDocument(mxdfile)
for i,df in enumerate(arcpy.mapping.ListDataFrames(mxd)):
	print i

	SetExtent(df,xmin-20,xmax+20,ymin-20,ymax+20)
	print 'XMin=',str(df.extent.XMin)
	print 'YMin=',str(df.extent.YMin)
	print 'XMax=',str(df.extent.XMax)
	print 'YMax=',str(df.extent.YMax)

	arcpy.mapping.ExportToPNG(mxd,str(i)+'.png',df,
						df_export_width=imgw, 
						df_export_height=imgh)
