{-Haskell HW2 HUnit test cases
 Please add at least 2 additional tests for each problem-}

module HW2SampleTests
    where

import Test.HUnit
import Data.Char
import Data.List (sort)
import HW2

{- Two useful functions in the HUnit package are assertEqual and assertBool.
The arguments to 'assertEqual' are:
      a descriptive string
      the expected value
      the value being tested
The arguments to 'assertBool' are:
      a descriptive string
      the boolean value being tested
-}

-- Sample Tree Integer examples given in the assignment prompt; make sure to provide your own tree examples for both tree data types
-- Your trees should have minimum 4 levels. 
t1 =  NODE 
         "Science" 
         (NODE "and" (LEAF "School")(NODE 
                                      "Engineering" 
                                      (LEAF "of") 
                                      (LEAF "Electrical"))) 
          (LEAF "Computer")

t2 = NODE 1 (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 7 (LEAF 8) (LEAF 9))
tree4 = NODE 12 (NODE 2 (NODE 33 (LEAF 54) (LEAF 55)) (LEAF 66)) (NODE 71 (LEAF 38) (LEAF 91))
tree5 = NODE 10 (NODE 72 (NODE 32 (LEAF 44) (LEAF 56)) (LEAF 61)) (NODE 73 (LEAF 82) (LEAF 11))



t3  = NODE 1 (NODE 2 (NODE 3 (LEAF 2) (LEAF 5)) (LEAF 1)) (NODE 1 (LEAF 8) (LEAF 5))
                                                                
left = NODE 1 (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 7 (LEAF 8) (LEAF 9))
right = NODE 1 (NODE 2 (LEAF 3) (LEAF 6)) (NODE 7 (NODE 8 (LEAF 10) (LEAF 11)) (LEAF 9))


left1 = NODE 1 (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 7 (LEAF 8) (LEAF 9))
right1 = NODE 3 (NODE 12 (LEAF 13) (LEAF 16)) (NODE 17 (NODE 18 (LEAF 1) (LEAF 1)) (LEAF 19))


left2 = NODE 1 (NODE 2 (NODE 3 (LEAF 4) (LEAF 5)) (LEAF 6)) (NODE 7 (LEAF 8) (LEAF 9))
right2 = NODE 5 (NODE 25 (LEAF 35) (LEAF 56)) (NODE 57 (NODE 85 (LEAF 105) (LEAF 151)) (LEAF 59))

l1 = LEAF "1"
l2 = LEAF "2"
l3 = LEAF "3"
l4 = LEAF "4"
n1 = NODE "5" l1 l2
n2 = NODE "6" n1 l3
t4 = NODE "7" n2 l4

p1a_test1 = TestCase (assertEqual "intersect [2,2,5,6,6,8,9] [1,3,2,2,4,4,5,7,8,10]" (sort [2,5,8])  (sort (intersect [2,2,5,6,6,8,9] [1,3,2,2,4,4,5,7,8,10])) ) 
p1a_test2 = TestCase (assertEqual "intersect [5,6,7,8,9] [8,8,10,10,11,12,5]" (sort [5,8])  (sort (intersect [5,6,7,8,9] [8,8,10,10,11,12,5])) ) 
p1a_test3 = TestCase (assertEqual "intersect [\"a\",\"b\",\"d\"] [\"c\",\"e\",\"f\",\"g\"]" []  (intersect ["a","b","d"] ["c","e","f","g"]) ) 
p1a_test4 = TestCase (assertEqual "intersect [1,1,1,1,1,1,13,14] [9,8,7,6,5,4,3,2,1]" (sort [1])  (intersect [1,1,1,1,1,1,13,14] [9,8,7,6,5,4,3,2,1]) )
p1a_test5 = TestCase (assertEqual "intersect [\"a\",\"b\",\"d\"] [\"c\",\"e\",\"f\",\"g\"]" []  (intersect ["a","b","d"] ["c","e","f","g"]) )

p1b_test1 = TestCase (assertEqual "intersectTail [2,2,5,6,6,8,9] [1,3,2,2,4,4,5,7,8,10]" (sort [2,5,8])  (sort (intersectTail [2,2,5,6,6,8,9] [1,3,2,2,4,4,5,7,8,10])) ) 
p1b_test2 = TestCase (assertEqual "intersectTail [5,6,7,8,9] [8,8,10,10,11,12,5]" (sort [5,8])  (sort (intersectTail [5,6,7,8,9] [8,8,10,10,11,12,5])) ) 
p1b_test3 = TestCase (assertEqual "intersectTail [\"a\",\"b\",\"d\"] [\"c\",\"e\",\"f\",\"g\"]" []  (intersectTail ["a","b","d"] ["c","e","f","g"]) ) 
p1b_test4 = TestCase (assertEqual "intersectTail [1,1,1,1,1,1,13,14] [9,8,7,6,5,4,3,2,1]" (sort [1])  (intersectTail [1,1,1,1,1,1,13,14] [9,8,7,6,5,4,3,2,1]) )
p1b_test5 = TestCase (assertEqual "intersectTail [\"a\"] [\"c\",\"e\",\"f\",\"g\"]"  []  (intersectTail ["a"] ["c","e","f","g"]) )


p1c_test1 = TestCase (assertEqual "intersectAll [[1,3,3,4,5,5,6],[3,4,5],[4,4,5,6],[3,5,6,6,7,8]]" (sort [5])  (sort (intersectAll [[1,3,3,4,5,5,6],[3,4,5],[4,4,5,6],[3,5,6,6,7,8]])) )
p1c_test2 = TestCase (assertEqual "intersectAll [[3,4],[-3,-4,3,4],[-3,-4,5,6]] " []  (sort (intersectAll [[3,4],[-3,-4,3,4],[-3,-4,5,6]])) )
p1c_test3 = TestCase (assertEqual "intersectAll [[3,4,5,5,6],[4,5,6],[],[3,4,5]] " []  (sort (intersectAll [[3,4,5,5,6],[4,5,6],[],[3,4,5]])) )
p1c_test4 = TestCase (assertEqual "intersectAll [[1,4,5,5,6],[3,4,5],[4,4,5,6],[3,4,6,6,7,8]]" (sort [4])  (sort (intersectAll [[1,3,3,4,5,5,6],[3,4,5],[4,4,5,6],[3,4,6,6,7,8]])) )
p1c_test5 = TestCase (assertEqual "intersectAll [[1,3,3,4,5,5,6],[1,3,4,5],[1,4,4,5,6],[1,3,5,6,6,7,8]]" (sort [1,5])  (sort (intersectAll [[1,3,3,4,5,5,6],[1,3,4,5],[1,4,4,5,6],[1,3,5,6,6,7,8]])) )


p2_test1 = TestCase (assertEqual "partition (\\x -> (x<=4)) [1,7,4,5,3,8,2,3]" ([1,4,3,2,3],[7,5,8])  (partition (\x -> (x<=4)) [1,7,4,5,3,8,2,3]) )
p2_test2 = TestCase (assertEqual "partition null [[1,2],[1],[],[5],[],[6,7,8]]" ([[],[]],[[1,2],[1],[5],[6,7,8]])  (partition null [[1,2],[1],[],[5],[],[6,7,8]]) )
p2_test3 = TestCase (assertEqual "partition (elem 1) [[1,2],[1],[],[5],[],[6,7,8]] " ([[1,2],[1]],[[],[5],[],[6,7,8]])  (partition (elem 1) [[1,2],[1],[],[5],[],[6,7,8]] ) )
p2_test4 = TestCase (assertEqual "partition (\\x -> (x>=4)) [1,7,4,5,3,8,2,3]" ([7,4,5,8],[1,3,2,3])  (partition (\x -> (x>=4)) [1,7,4,5,3,8,2,3]) )
p2_test5 = TestCase (assertEqual "partition (elem 5) [[1,2],[1],[],[5],[],[5,6,7,8]] " ([[5],[5,6,7,8]],[[1,2],[1],[],[]])  (partition (elem 5) [[1,2],[1],[],[5],[],[5,6,7,8]] ) )


p3a_test1 = TestCase (assertEqual "sumL [[1,2,3],[4,5],[6,7,8,9],[]]" 45 (sumL [[1,2,3],[4,5],[6,7,8,9],[]]) ) 
p3a_test2 = TestCase (assertEqual "sumL [[10,10],[10,10,10],[10]]" 60 (sumL [[10,10],[10,10,10],[10]]) ) 
p3a_test3 = TestCase (assertEqual "sumL [[]]" 0 (sumL [[]]) ) 
p3a_test4 = TestCase (assertEqual "sumL [[1,2,3],[]]" 6 (sumL [[1,2,3],[]]) ) 
p3a_test5 = TestCase (assertEqual "sumL [[1,1,1,1,1],[],[2,2,2,2,2],[]]" 15 (sumL [[1,1,1,1,1],[],[2,2,2,2,2],[]]) ) 


p3b_test1 = TestCase (assertEqual "sumMaybe [[(Just 1),(Just 2),(Just 3)],[(Just 4),(Just 5)],[(Just 6),Nothing ],[],[Nothing ]]" (Just 21) (sumMaybe [[(Just 1),(Just 2),(Just 3)],[(Just 4),(Just 5)],[(Just 6),Nothing ],[],[Nothing ]]) )
p3b_test2 = TestCase (assertEqual "sumMaybe [[(Just 10),Nothing],[(Just 10), (Just 10), (Just 10),Nothing,Nothing]]" (Just 40) (sumMaybe [[(Just 10),Nothing],[(Just 10), (Just 10), (Just 10),Nothing,Nothing]]) )
p3b_test3 = TestCase (assertEqual "sumMaybe [[Nothing ]]" (Nothing) (sumMaybe [[Nothing ]]) )
p3b_test4 = TestCase (assertEqual "sumMaybe [[Nothing,(Just 5)]]" (Just 5) (sumMaybe [[Nothing,(Just 5)]]) )
p3b_test5 = TestCase (assertEqual "sumMaybe [[(Just 100),(Just 10)],[(Just 60),(Just 30)]]" (Just 200) (sumMaybe [[(Just 100),(Just 10)],[(Just 60),(Just 30)]]) )


p3c_test1 = TestCase (assertEqual "sumEither [[IString \"1\",IInt 2,IInt 3],[IString \"4\",IInt 5],[IInt 6,IString \"7\"],[],[IString \"8\"]]" (IInt 36) (sumEither [[IString "1",IInt 2,IInt 3],[IString "4",IInt 5],[IInt 6,IString "7"],[],[IString "8"]]) )
p3c_test2 = TestCase (assertEqual "sumEither [[IString \"10\" , IInt 10],[],[IString \"10\"],[]]" (IInt 30) (sumEither [[IString "10" , IInt 10],[],[IString "10"],[]]) )
p3c_test3 = TestCase (assertEqual "sumEither  [[]]" (IInt 0) (sumEither  [[]]) )
p3c_test4 = TestCase (assertEqual "sumEither [[IString \"1\",IInt 2,IInt 3],[IString \"4\",IInt 5],[],[IString \"5\"]]" (IInt 20) (sumEither [[IString "1",IInt 2,IInt 3],[IString "4",IInt 5],[],[IString "5"]]) )
p3c_test5 = TestCase (assertEqual "sumEither [[IString \"10\" , IInt 10],[],[IString \"80\"],[]]" (IInt 100) (sumEither [[IString "10" , IInt 10],[],[IString "80"],[]]) )



p4a_test1 = TestCase (assertEqual "depthScan t1"  ["School","of","Electrical","Engineering","and","Computer","Science"] (depthScan t1) ) 
p4a_test2 = TestCase (assertEqual "depthScan t2" [4,5,3,6,2,8,9,7,1] (depthScan t2) ) 
p4a_test3 = TestCase (assertEqual "depthScan tree4" [54,55,33,66,2,38,91,71,12] (depthScan tree4) ) 
p4a_test4 = TestCase (assertEqual "depthScan tree5" [44,56,32,61,72,82,11,73,10] (depthScan tree5) ) 


p4b_test1 = TestCase (assertEqual "depthSearch t3 1" 3 (depthSearch t3 1) ) 
p4b_test2 = TestCase (assertEqual "depthSearch t3 5" 4 (depthSearch t3 5) )
p4b_test3 = TestCase (assertEqual "depthSearch t3 4" (-1) (depthSearch t3 4) )
p4b_test4 = TestCase (assertEqual "depthSearch t3 2" 4 (depthSearch t3 2) )
p4b_test5 = TestCase (assertEqual "depthSearch t3 10" (-1) (depthSearch t3 10) )


addedTree = NODE 2 (NODE 4 (NODE 6 (LEAF 4) (LEAF 5)) (LEAF 12)) (NODE 14 (NODE 16 (LEAF 10) (LEAF 11)) (LEAF 18))
p4c_test1 = TestCase (assertEqual ("addTrees "++ (show left) ++ (show right)) addedTree  (addTrees left right) ) 

addedTree1 = NODE 4 (NODE 14 (NODE 16 (LEAF 4) (LEAF 5)) (LEAF 22)) (NODE 24 (NODE 26 (LEAF 1) (LEAF 1)) (LEAF 28))
p4c_test2 = TestCase (assertEqual ("addTrees1 "++ (show left1) ++ (show right1)) addedTree1 (addTrees left1 right1) ) 

addedTree2 = NODE 6 (NODE 27 (NODE 38 (LEAF 4) (LEAF 5)) (LEAF 62)) (NODE 64 (NODE 93 (LEAF 105) (LEAF 151)) (LEAF 68))
p4c_test3 = TestCase (assertEqual ("addTrees2 "++ (show left2) ++ (show right2)) addedTree2  (addTrees left2 right2) ) 


tests = TestList [ TestLabel "Problem 1a - test1 " p1a_test1,
                   TestLabel "Problem 1a - test2 " p1a_test2,
                   TestLabel "Problem 1a - test3 " p1a_test3,
                   TestLabel "Problem 1a - test4 " p1a_test4,
                   TestLabel "Problem 1a - test5 " p1a_test5,
                   
                   TestLabel "Problem 1b - test1 " p1b_test1,
                   TestLabel "Problem 1b - test2 " p1b_test2,                   
                   TestLabel "Problem 1b - test3 " p1b_test3,  
                   TestLabel "Problem 1b - test4 " p1b_test4,
                   TestLabel "Problem 1b - test5 " p1b_test5,

                   TestLabel "Problem 1c - test1 " p1c_test1,
                   TestLabel "Problem 1c - test2 " p1c_test2,
                   TestLabel "Problem 1c - test3 " p1c_test3,
                   TestLabel "Problem 1c - test4 " p1c_test4,
                   TestLabel "Problem 1c - test5 " p1c_test5,
                   
                   
                   TestLabel "Problem 2  - test1 " p2_test1,
                   TestLabel "Problem 2  - test2 " p2_test2,  
                   TestLabel "Problem 2  - test3 " p2_test3,
                   TestLabel "Problem 2  - test4 " p2_test4,
                   TestLabel "Problem 2  - test5 " p2_test5,

                   TestLabel "Problem 3a - test1 " p3a_test1,
                   TestLabel "Problem 3a - test2 " p3a_test2,  
                   TestLabel "Problem 3a - test3 " p3a_test3,  
                   TestLabel "Problem 3a - test4 " p3a_test4, 
                   TestLabel "Problem 3a - test5 " p3a_test5, 


                   TestLabel "Problem 3b - test1 " p3b_test1,
                   TestLabel "Problem 3b - test2 " p3b_test2,
                   TestLabel "Problem 3b - test3 " p3b_test3,
                   TestLabel "Problem 3b - test4 " p3b_test4,
                   TestLabel "Problem 3b - test5 " p3b_test5,

                   TestLabel "Problem 3c - test1 " p3c_test1,
                   TestLabel "Problem 3c - test2 " p3c_test2,
                   TestLabel "Problem 3c - test3 " p3c_test3,
                   TestLabel "Problem 3c - test4 " p3c_test4,
                   TestLabel "Problem 3c - test5 " p3c_test5,

                   TestLabel "Problem 4a - test1 " p4a_test1,
                   TestLabel "Problem 4a - test2 " p4a_test2,
                   TestLabel "Problem 4a - test3 " p4a_test3,
                   TestLabel "Problem 4a - test4 " p4a_test4,


                   TestLabel "Problem 4b - test1 " p4b_test1,
                   TestLabel "Problem 4b - test2 " p4b_test2,
                   TestLabel "Problem 4b - test3 " p4b_test3,
                   TestLabel "Problem 4b - test4 " p4b_test4,
                   TestLabel "Problem 4b - test5 " p4b_test5,

                   TestLabel "Problem 4c - test1 " p4c_test1,
                   TestLabel "Problem 4c - test2 " p4c_test2,
                   TestLabel "Problem 4c - test3 " p4c_test3
                  ] 
                  

-- shortcut to run the tests
run = runTestTT  tests