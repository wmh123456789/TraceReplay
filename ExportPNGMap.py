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

def ExportPNG(FloorList,MallName,RootDir):
	for Floor in FloorList:
		mxdfile = '{0}\{1}\{1}.mxd'.format(RootDir,MallName)
		xmlfile = '{0}\{1}\Binary\{1}.Floor{2}.xml'.format(RootDir,MallName,Floor)
		PNGName = '{0}_{1}.png'.format(MallName,Floor)
		layer = gis.ParseStandardMapXMLFile(xmlfile)
		print 'Exporting {}'.format(PNGName)
		print 'getbound:',str(layer.getbound())
		xmin,xmax,ymin,ymax = layer.getbound()
		imgh = int((ymax-ymin)*10.0+200*2)
		imgw = int((xmax-xmin)*10.0+200*2)
		print 'imgw,imgh:',imgw,imgh
		mxd = arcpy.mapping.MapDocument(mxdfile)
		for i,df in enumerate(arcpy.mapping.ListDataFrames(mxd)):
			# print i

			MarginFactor = -1.0 # Modify the margin of the output PNG,-1~2 for different bld
			SetExtent(df,xmin-10*MarginFactor,xmax+10*MarginFactor,
						ymin-10*MarginFactor,ymax+10*MarginFactor)
			# SetExtent(df,xmin,xmax,ymin,ymax)
			print 'XMin=',str(df.extent.XMin)
			print 'YMin=',str(df.extent.YMin)
			print 'XMax=',str(df.extent.XMax)
			print 'YMax=',str(df.extent.YMax)

			arcpy.mapping.ExportToPNG(mxd,PNGName,df,
								df_export_width=imgw, 
								df_export_height=imgh)

def main():
	MallName = 'ChaoYangDaYueCheng'
	FloorList = ['AEON']
	RootDir = 'E:\MDBGenerate\= MDB_Modify_BJ\= ModifiedOK'
	ExportPNG(FloorList,MallName,RootDir)


if __name__ == '__main__':
	main()

