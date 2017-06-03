# coding: utf-8
import json

class FeatureCollection():
	def __init__(self):
		self.featureCollection = self.getFeatureCollectionBase()
	
	def getFeatureCollectionBase(self):
		return {
		  "type": "FeatureCollection",
		  "crs": {
		    "type": "name",
		    "properties":{ "name": "urn:ogc:def:crs:OGC:1.3:CRS84" }
		  },
		  "features": []
		}
	
	def addFeature(self, featureObject):
		self.featureCollection["features"].append(featureObject.feature)
	
	def toJSON(self):
		return json.dumps(self.featureCollection)


class PolygonBase():
	def __init__(self):
		self.feature = self.getBase()
	
	def getBase(self):
		return {
		  "type": "Feature",
		  "properties": { },
		  "geometry": {
		    "type": "Polygon",
		    "coordinates": [ [ ] ]
		  }
		}

	def setProperty(self, data):
		for k in data.keys():
			self.feature["properties"][k] = data[k]


class Square(PolygonBase):
	def __init__(self, ulx, uly, lrx, lry):
		self.feature = self.getPolygonFeatureBase(ulx, uly, lrx, lry)
	
	def getPolygonFeatureBase(self, ulx, uly, lrx, lry):
		feature = self.getBase()
		feature["geometry"]["coordinates"][0].append([ulx, uly])
		feature["geometry"]["coordinates"][0].append([ulx, lry])
		feature["geometry"]["coordinates"][0].append([lrx, lry])
		feature["geometry"]["coordinates"][0].append([lrx, uly])
		feature["geometry"]["coordinates"][0].append([ulx, uly])
		return feature


class Rectangle(PolygonBase):
	def __init__(self, ulxy, llxy, lrxy, urxy):
		self.feature = self.getPolygonFeatureBase(ulxy, llxy, lrxy, urxy)
	
	def getPolygonFeatureBase(self, ulxy, llxy, lrxy, urxy):
		feature = self.getBase()
		feature["geometry"]["coordinates"][0].append([ulxy[0], ulxy[1]])
		feature["geometry"]["coordinates"][0].append([llxy[0], llxy[1]])
		feature["geometry"]["coordinates"][0].append([lrxy[0], lrxy[1]])
		feature["geometry"]["coordinates"][0].append([urxy[0], urxy[1]])
		feature["geometry"]["coordinates"][0].append([ulxy[0], ulxy[1]])
		return feature

