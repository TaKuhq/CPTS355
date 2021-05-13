-- CptS 355 - Spring 2020 Assignment 2
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework
-- Name: Hongqi Guo        discussed:->  tutor: David

module HW2
     where


{- intersect & intersectTail & intersectAll - 22%-}
--intersect
--add remove same number function.
removesame :: Eq t=> [t] -> [t]
removesame [] = []
--if x = xs,then return true,else just return x.
removesame (x : xs) = if (x `elem` xs) then removesame xs else x : removesame xs
intersect :: Eq a => [a] -> [a] -> [a]
intersect  x [] = []
intersect  [] y = []
intersect (x : xs)(y : ys) = if (x `elem` (y : ys) )
                         then removesame ( x : intersect xs (y : ys) )
                         else intersect xs ( y : ys)
--intersectTail
intersectTail :: Eq a => [a] -> [a] -> [a]
intersectTail [] [] = []
intersectTail (x : xs)(y : ys) = helper (x : xs)(y : ys) []
     where
          helper :: Eq a => [a] -> [a] -> [a] -> [a]
          helper x [] acc = []
          helper [] y acc = []
          helper (x : xs) (y : ys) acc = if (x `elem` (y : ys))
                              then  removesame (x : helper xs (y : ys) (x : acc))
                              else  ( helper xs (y : ys) (x : acc))


--intersectAll
intersectAll:: Ord a => [[a]] -> [a]
intersectAll [] = []
intersectAll (x : xs)= foldr intersect x xs


{-2 - partition - 10%-}
partition :: (a -> Bool) -> [a] -> ([a], [a])
partition op [] = ([],[])
--partition op iL = (filter (== op) ) (filter ( /= op) iL) 
partition op iL = ( (filter op iL ),  (filter (not.op) iL))


{- 3 - sumL, sumMaybe, and sumEither - 27% -}

--sumL
sumL :: (Num b) => [[b]] -> b
sumL [] = 0
sumL iL =foldr (+) 0 ( map (foldr (+) 0) iL)
 


-- sumMaybe 

sumMaybe :: (Num a) => [[(Maybe a)]] -> Maybe a
addMaybe (Just x) (Just y) = (Just(x+y))
addMaybe Nothing Nothing = Nothing
addMaybe Nothing (Just x) = (Just x)
addMaybe (Just x) Nothing = (Just x)

sumMaybe  [] = Nothing
sumMaybe [[Just iL]] = Just (iL)
sumMaybe (iL) = foldr addMaybe (Nothing) ( map (foldr addMaybe (Nothing)) (iL))

-- sumEither

data IEither  = IString String | IInt Int
                deriving (Show, Read, Eq)

getInt x = read x::Int
addf ((IString x)) (IString y) = (IInt (getInt(x)+getInt(y)))
addf (IString x) (IInt y) = (IInt ((getInt(x)+y)))
addf (IInt x)(IInt y) = (IInt ((x+y)))
addf (IInt x)(IString y) = (IInt ((x + getInt(y))))

sumEither:: Foldable t => [t IEither] -> IEither
sumEither iL = foldr addf (IInt 0) ( map (foldr addf (IInt 0)) (iL))


{-4 - depthScan, depthSearch, addTrees - 37%-}

data Tree a = LEAF a | NODE a (Tree a) (Tree a)
              deriving (Show, Read, Eq)
 
--depthScan
depthScan :: Tree a -> [a]
depthScan (LEAF x) = [x]
depthScan (NODE n t1 t2) = (depthScan t1)  ++ (depthScan t2) ++ [n]


--depthSearch
depthSearch (LEAF x)  = if x/2== 0 then True else False



--addTrees
addTrees :: Num a => Tree a -> Tree a -> Tree a
addTrees (LEAF x)(LEAF y) = (LEAF(x + y))
addTrees (LEAF x) (NODE n t1 t2) = (NODE (x + n) t1 t2)
addTrees (NODE n t1 t2) (LEAF x) = (NODE (x + n) t1 t2)
addTrees (NODE n1 l1 r1) (NODE n2 l2 r2) = (NODE (n1 + n2)) (addTrees l1 l2) (addTrees r1 r2)

{- 5- Create two trees of type Tree. The height of both trees should be at least 4. Test your functions depthScan, depthSearch, addTrees with those trees. 
The trees you define should be different than those that are given.   -}
l11 = LEAF "11"
l21 = LEAF "12"
l31 = LEAF "13"
l41 = LEAF "14"
l51 = LEAF "15"
n11 = NODE "5" l11 l21 
n21 = NODE "6" n11 l31
n31 = NODE "9" n21 l41
t41 = NODE "7" n31 l51 
 


ll1 = LEAF "105"
ll2 = LEAF "1"
ll3 = LEAF "23"
ll4 = LEAF "14"
ll5 = LEAF "5"
nl1 = NODE "5" ll1 ll2 
nl2 = NODE "66" nl1 ll3
nl3 = NODE "97" nl2 ll4
tl4 = NODE "77" nl3 ll5 




maxi :: (Ord a) => [a] -> a   
maxi [x] = x  
maxi (x:xs)   
    | x > maxTail = x  
    | otherwise = maxTail  
    where maxTail = maxi xs

