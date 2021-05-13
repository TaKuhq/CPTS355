-- CptS 355 - Spring 2020 Assignment 1
-- Please include your name and the names of the students with whom you discussed any of the problems in this homework
-- student name : Hongqi Guo
-- discussed : yuyang song // jihui sheng // tutor: David
module HW1
     where

-- 1a. exists
exists :: Eq t => t -> [t] -> Bool
--if g is empty,then return False
exists g [] = False 
--If there is a n value in the list, then return true,otherwise return n
exists n (x : xs) = if n == x then True else exists n xs 

-- 1b. type for exists
-- By using the type class Eq, 
-- the value of exists is compared with the value in list one by one 
-- and output as a bool value.

-- 1.c countInList
countInList :: (Num p, Eq t) => t -> [t] -> p
-- Assign g value to 0
countInList g [] = 0
--This step determines whether the input n value is equal to x.
--If =, add 1 to the value of g
countInList n (x : xs) = if n == x then (countInList n xs) + 1  else countInList n xs


-- 2. listDiff
--I made an equation that removed the same numbers in parts x and y.
removeFromList :: Eq t=> t-> [t] -> [t]
remvoeFromList x [] = []
removeFromList x (y :ys) = if x == y then ys else y : removeFromList x ys

listDiff :: Eq a => [a] -> [a] -> [a]
listDiff x [] = x
listDiff [] y = []
--this part I use countlist to determine if the x and y parts are the same.
listDiff (x : xs) (y : ys) = if (countInList y (x : xs) /= 0)
     --if not,Use Removefromlist to delete the number in the x part.
      then listDiff(removeFromList y (x : xs)) ys 
      --if same,keep x value.
      else listDiff (x : xs) ys


-- 3. firstN
firstN :: (Ord t, Num t) => [a] -> t -> [a] 
--Assume empty
firstN [] y = []
--Outputs the values ​​in the list.
--Each time it is output, the value of y is decreased by one.
firstN (x : xs) y = if y >= 1 then x : (firstN xs (y-1)) else []

-- 4. busFinder
busFinder :: Eq t => t -> [(a, [t])] -> [a] 
--Assume empty
busFinder y []  = [] 
--First I used the input y value to compare with the second data of the snd equation proposed tuple. 
--If there is the same use of fst to present the first data of the tuple and present the data,
-- if not continue to run.
busFinder y (x:xs) = if (exists y (snd x)) then ((fst x):(busFinder y xs )) else (busFinder y xs ) 


-- 5. cumulativeSums
cumulativeSums :: Num a => [a] -> [a]
--If there is a null value, the output is null.
cumulativeSums [] = []
--Use the helper equation to temporarily save the output a value.
cumulativeSums (a : as) = a : helper a as
--Take out the value of n.
     where helper n [] = []
     --Add the value of n to the second value of a and save it in the helper equation.
           helper n (a : as) = (n + a) : helper (n + a) as
          

-- 6. groupNleft
--Construct a takelist equation, which is similar to the firstN equation. 
--Its role is to get the number of inputs 
--and output a list of the number of responses.
takeList :: (Num i, Ord i) => i -> [a] -> [a]   
takeList y []  = []
--Outputs the values ​​in the list.
--Each time it is output, the value of y is decreased by one.
takeList y (x : xs)  = if y >= 1 then x : (takeList  (y-1) xs) else []
--Construct a dropList equation, which is the opposite of the takeList equation.
--Its role is to get a number and list, 
--delete the corresponding number of lists and output.
dropList :: Int -> [a] -> [a]
--assume xs value
dropList 0 xs = xs
--if output is empty,return empty.
dropList _ [] = []
--Each time it is output, the value of y is decreased by one.
dropList y (_:xs) = dropList (y-1) xs
groupNleft :: Int -> [a] -> [[a]] 
--Assume empty
groupNleft n [] = []
--Compare the value of n with list. 
--First use the takelist equation to take out n lists,
--and then use droplist to delete it.
groupNleft n (x : xs) = if n > 0 then (takeList n (x : xs)) : (groupNleft n (dropList n (x : xs))) else []
