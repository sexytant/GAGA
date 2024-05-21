from gaga.visual.component import Shape,Image
from gaga.visual.shape import Ellipse
from gaga.general.component import Base
from random import random
from typing import List

def createEllipsis(num: int,ellipseSize: float):
    ellipsis=[]
    for i in range(num):
        params={}
        params["x"]=Base(id=0,type="x",letter=random())
        params["y"]=Base(id=1,type="y",letter=random())
        params["width"]=Base(id=2,type="width",letter=random()*ellipseSize)
        params["height"]=Base(id=3,type="height",letter=random()*ellipseSize)
        params["red"]=Base(id=4,type="red",letter=random())
        params["green"]=Base(id=5,type="green",letter=random())
        params["blue"]=Base(id=6,type="blue",letter=random())
        ellipse=Ellipse(id=i,params=params,ellipseSize=ellipseSize)
        ellipsis.append(ellipse)
    return ellipsis

def createImage(id:int,shapes: List[Shape]):
    return Image(id,shapes,1.0)