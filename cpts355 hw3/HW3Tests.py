import unittest
from hw3 import *

class HW3Tests(unittest.TestCase):
    def setUp(self):
        pass
    def test_sumSales(self):
        salesLog= {'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}}
        summedLog = {'Fri': 30, 'Mon': 80, 'Sat': 220, 'Thu': 80, 'Tue': 180, 'Wed': 225}
        #1
        salesLog1= {'Amazon':{'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}}
        summedLog1 = {'Wed': 125, 'Sat': 220, 'Mon': 50, 'Tue': 120, 'Fri': 30, 'Thu': 50}
        #2
        salesLog2= {'Amazon':{'Mon':130,'Wed':100,'Sat':200},'Ebay':{'Tue':60,'Wed':100,'Thu':30}}
        summedLog2 = {'Mon': 130, 'Wed': 200, 'Sat': 200, 'Tue': 60, 'Thu': 30}

        self.assertDictEqual(sumSales(salesLog),summedLog)
        self.assertDictEqual(sumSales(salesLog1),summedLog1)
        self.assertDictEqual(sumSales(salesLog2),summedLog2)


    def test_sumSalesN(self):
        salesLogN = [{'Amazon':{'Mon':30,'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Wed':25,'Fri':30},'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50}, 'Ebay':{'Mon':100,'Sat':30}},{'Amazon':{'Sun':88},'Etsy':{'Fri':55},'Ebay':{'Mon':40},'Shopify':{'Sat':35}}]
        summedLogN = {'Fri': 135,'Mon':245,'Sat':285,'Sun': 88,'Thu': 120,'Tue':180,'Wed':225}
        #1
        salesLogN1 = [{'Amazon':{'Wed':100,'Sat':200},'Etsy':{'Mon':50,'Tue':20,'Fri':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},{'Etsy':{'Thu':40, 'Fri':50}, },{'Amazon':{'Sun':88},'Etsy':{'Fri':55},'Ebay':{'Mon':40},'Shopify':{'Sat':35}}]
        summedLogN1 = {'Wed': 100, 'Sat': 255, 'Mon': 90, 'Tue': 120, 'Fri': 135, 'Thu': 90, 'Sun': 88}
        #2
        salesLogN2 = [{'Ebay':{'Tue':60,'Wed':100,'Thu':30},'Shopify':{'Tue':100,'Thu':50,'Sat':20}},{'Shopify':{'Mon':25},'Etsy':{'Thu':40, 'Fri':50}, 'Ebay':{'Mon':100,'Sat':30}}]
        summedLogN2 = {'Tue': 160, 'Wed': 100, 'Thu': 120, 'Sat': 50, 'Mon': 125, 'Fri': 50}

        self.assertDictEqual(sumSalesN(salesLogN),summedLogN)
        self.assertDictEqual(sumSalesN(salesLogN1),summedLogN1)
        self.assertDictEqual(sumSalesN(salesLogN2),summedLogN2)


    def test_searchDicts(self):
        #searchDicts inputs
        dictList = [{"x":1,"y":True,"z":"found"},{"x":2},{"y":False}]
        self.assertEqual(searchDicts(dictList,"x"),2)
        self.assertEqual(searchDicts(dictList,"y"),False)
        self.assertEqual(searchDicts(dictList,"z"),"found")
        self.assertEqual(searchDicts(dictList,"t"),None)
        #1
        dictList1 = [{"y":False,"z":"found"},{"x":2},{"y":True,"z":"bug"}]
        self.assertEqual(searchDicts(dictList1,"x"),2)
        self.assertEqual(searchDicts(dictList1,"y"),True)
        self.assertEqual(searchDicts(dictList1,"z"),"bug")
        #2
        dictList = [{"x":1,"y":True,"z":"found"},{"y":False},{"t":"yes","y":True}]
        self.assertEqual(searchDicts(dictList,"x"),1)
        self.assertEqual(searchDicts(dictList,"y"),True)
        self.assertEqual(searchDicts(dictList,"z"),"found")
        self.assertEqual(searchDicts(dictList,"t"),"yes")


       


    def test_searchDicts2(self):
        dictList2 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"x":1}), (1,{"y":False}), (1,{"x":3, "z":"three"}), (2,{})]
        self.assertEqual(searchDicts2(dictList2,"x"),1)
        self.assertEqual(searchDicts2(dictList2,"y"),False)
        self.assertEqual(searchDicts2(dictList2,"z"),"zero")
        self.assertEqual(searchDicts2(dictList2,"t"),None)
        #1
        dictList22 = [(0,{"x":0,"y":True}),(1,{"y":False}), (1,{"x":3, "z":"three"})]
        self.assertEqual(searchDicts2(dictList22,"x"),3)
        self.assertEqual(searchDicts2(dictList22,"y"),False)
        self.assertEqual(searchDicts2(dictList22,"z"),"three")
        #2
        dictList23 = [(0,{"x":0,"y":True,"z":"zero"}), (0,{"y":False}), (1,{"x":1}),(2,{})]
        self.assertEqual(searchDicts2(dictList23,"x"),1)
        self.assertEqual(searchDicts2(dictList23,"y"),False)
        self.assertEqual(searchDicts2(dictList23,"z"),"zero")





    def test_busStops(self):
        routes = {
            "Lentil": ["Chinook", "Orchard", "Valley", "Emerald","Providence", "Stadium", "Main", "Arbor", "Sunnyside", "Fountain", "Crestview", "Wheatland", "Walmart", "Bishop", "Derby", "Dilke"],
            "Wheat": ["Chinook", "Orchard", "Valley", "Maple","Aspen", "TerreView", "Clay", "Dismores", "Martin", "Bishop", "Walmart", "PorchLight", "Campus"],
            "Silver": ["TransferStation", "PorchLight", "Stadium", "Bishop","Walmart", "Shopco", "RockeyWay"],
            "Blue": ["TransferStation", "State", "Larry", "TerreView","Grand", "TacoBell", "Chinook", "Library"],
            "Gray": ["TransferStation", "Wawawai", "Main", "Sunnyside","Crestview", "CityHall", "Stadium", "Colorado"]
        }
        self.assertEqual(busStops(routes,"Stadium"),['Lentil', 'Silver', 'Gray'])
        self.assertEqual(busStops(routes,"Bishop"),['Lentil', 'Wheat', 'Silver'])
        self.assertEqual(busStops(routes,"EECS"),[])
        #1
        self.assertEqual(busStops(routes,"PorchLight"),['Wheat', 'Silver'])
        #2
        self.assertEqual(busStops(routes,"Larry"),['Blue'])



    def test_palindromes(self):
        self.assertEqual(palindromes ('cabbbaccab'),['abbba', 'acca', 'baccab', 'bb', 'bbb', 'cabbbac', 'cc'] )
        self.assertEqual(palindromes ('bacdcabdbacdc') ,['abdba', 'acdca', 'bacdcab', 'bdb', 'cabdbac', 'cdc', 'cdcabdbacdc', 'dcabdbacd'])
        self.assertEqual(palindromes (' myracecars')  ,['aceca', 'cec', 'racecar'])
        #1
        self.assertEqual(palindromes ('01222102247') ,['0122210', '12221', '22', '222'])
        #2
        self.assertEqual(palindromes (' ILECKEECSCPTS355')  ,['55', 'CSC', 'EE'])

    class OddsEvens(object):
        def __init__(self,init):
            self.current = init
        def __next__(self):
            result = self.current
            self.current += 2
            return result
        def __iter__(self):
            return self

    #This function assumes that the first value in L is less than or equal to N.
    def getUntilN(self,L,N):
        tempL = []
        for item in L:
            tempL.append(item)
            if item>=N: break
        return tempL

    def test_interlaceIter(self):
    	#test 1
        iSequence = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        self.assertEqual(iSequence.__next__(),1)
        self.assertEqual(iSequence.__next__(),'a')
        self.assertEqual(iSequence.__next__(),2)
        rest = []
        for item in iSequence:
            rest.append(item)
        self.assertEqual(rest,['b',3,'c',4,'d',5,'e',6,'f',7,'g'])
        2
        iSequence2 = interlaceIter(iter([1,2,3,4]),iter("abcd"))
        self.assertEqual(iSequence2.__next__(),1)
        self.assertEqual(iSequence2.__next__(),'a')
        self.assertEqual(iSequence2.__next__(),2)
        rest = []
        for item in iSequence2:
            rest.append(item)
        self.assertEqual(rest,['b', 3, 'c', 4, 'd'])

        #3
        iSequence3 = interlaceIter(iter([1,2,3,4,5,6,7]),iter("abcdefg"))
        self.assertEqual(iSequence3.__next__(),1)
        self.assertEqual(iSequence3.__next__(),'a')
        rest = []
        for item in iSequence3:
            rest.append(item)
        self.assertEqual(rest,[2, 'b', 3, 'c', 4, 'd', 5, 'e', 6, 'f', 7, 'g'])

        #test2
        naturals = interlaceIter(self.OddsEvens(1),self.OddsEvens(2))
        self.assertEqual(naturals.__next__(),1)
        first20 = self.getUntilN(naturals,20)
        self.assertEqual(first20,[x for x in range(2,21)])
        self.assertEqual(naturals.__next__(),21)


    def test_typeHistogram(self):
    	#test 1
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 3), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('str', 3), ('int', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), sorted([('int', 2), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence1,5)), [])
        #2
        iSequence12 = interlaceIter(iter([1,2,3,4,5,6,7,8,9,10,11,12,13,14]),iter("abcdefghijklm"))
        self.assertEqual(sorted(typeHistogram(iSequence12,5)), sorted([('int', 3), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence12,5)), sorted([('str', 3), ('int', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence12,5)), sorted([('int', 3), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence12,5)), sorted([('int', 2), ('str', 3)]))
        #3
        iSequence13 = interlaceIter(iter([1,2,3,4]),iter("abcd"))
        self.assertEqual(sorted(typeHistogram(iSequence13,5)), sorted([('int', 3), ('str', 2)]))
        self.assertEqual(sorted(typeHistogram(iSequence13,5)), sorted([('str', 2), ('int', 1)]))
        self.assertEqual(sorted(typeHistogram(iSequence13,5)), [])
        #test 2
        iSequence1 = interlaceIter(iter([1,2,3,4,5,6,7,8,9]),iter("abcdefg"))
        iSequence2 = interlaceIter(iSequence1, iter([(1,'a'),(2,'b'),(3,'c'),(4,'d')]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)),sorted([('int', 2), ('str', 2),('tuple',4)]))
        self.assertEqual(sorted(typeHistogram(iSequence2,8)), [])




if __name__ == '__main__':
    unittest.main()

