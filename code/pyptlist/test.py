from pyautocad import APoint
from vector import Vector
import unittest
from math import *
from polygon import Polygon

class mytest(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    
    def testplane(self):
        p1=APoint(1,0)
        p2=APoint(0,1)
        p3=APoint(-1,0)
        vec1=Vector(p2,p1)
        vec2=Vector(p2,p3)
        vec10=Vector(p1,p2)
        vecx=Vector(p3,p1)
        self.assertEqual(vec1.direction,-vec10.direction)
        self.assertAlmostEqual(vec1.norm,sqrt(2))
        self.assertAlmostEqual(vec1.norm,sqrt(2))
        self.assertAlmostEqual(vec1.angle(vec2),1.5*pi)
        self.assertAlmostEqual(vec1.proj(vec2),0)
        self.assertEqual(vec1.intersect(vec2),APoint(0,1))
        self.assertEqual(vecx.proj_vec(vec1),APoint(1,0))
        self.assertEqual(vec1.side(p1),0)
        self.assertEqual(vec1.side(p2),0)
        self.assertEqual(vec1.Contains(p2),2)
        self.assertEqual(vec1.Contains(p1),4)
        po1=vec1.divide(1)
        self.assertEqual(po1,APoint(0.5,0.5))
        po2=vec1.divide(-2)
        self.assertEqual(po2,APoint(2,-1))
        po3=vec1.divide(-0.5)
        self.assertEqual(po3,APoint(-1,2))
        self.assertEqual(vec1.Contains(po1),3)
        self.assertEqual(vec1.Contains(po2),5)
        self.assertEqual(vec1.Contains(po3),1)
        self.assertEqual(vec1.Contains(p3),0)
        self.assertEqual(vec2.side(po3),1)
        self.assertEqual(vec2.side(po2),-1)
        vec4=Vector(APoint(1,1))
        self.assertEqual(vec4.intersect(vec1),APoint(0.5,0.5))

    def testPolygon(self):
        pol=[APoint(0,0),APoint(2,0),APoint(2,1),APoint(0,1)]
        poly=Polygon(pol)
        self.assertEqual(poly.Center,APoint(1,0.5))
        self.assertEqual(poly.Area(),2)
        self.assertEqual(poly.Bottomleft,APoint(0,0))
        self.assertEqual(poly.Topright,APoint(2,1))
        self.assertEqual(poly.L,4)
        self.assertEqual(poly.Direction(),True)
        self.assertAlmostEqual(poly.GetLongestDiagonalLine()[2],sqrt(5))
        self.assertEqual(poly.Contains(APoint(1,0.5)),True)
        self.assertEqual(poly.Contains(APoint(-2,1)),False)
        print(poly.Contains(APoint(2,1)))

        




        





if __name__=="__main__":
    unittest.main()