#!/usr/bin/env python
# coding: utf-8

import sys
import MiniGeoJSON as mgjson

def MiniGeoJSONExample():
    fc = mgjson.FeatureCollection()
    square = mgjson.Square(0, 0, 1, 1) # square of (x,y): (0,0) -> (1,1)
    square.setProperty({"ID": 1})
    fc.addFeature(square)
    print(fc.toJSON())

if __name__ == "__main__":
    MiniGeoJSONExample()
