14) Describe the sets which are defined by the following four statements in one or more
words:
a) What is the union of:
i) The set of all english vowels
ii) the set of all english non-vowel letters

A:{A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z}

b) What is the intersection of:
i) platonic solids with a number of sides >=4 but < 10
ii) platonic solids with 8 or more sides

A:
platonic_solids = {4,6,8,12,20}
p_s_intersection_set = {8}

c) What is the difference of:
i) people under 6 feet tall
ii) people over 5 feet tall

A:
difference_set = under_6.difference(over_5) =
{1,2,3,4}


d) What is the symmetric difference of:
i) months from January to April
ii) months from March to December

A:
symmetric_difference_set = {'January','Feburary','May','June','July','August', \
'Sepetember','October','November','December'}



15)
a) What will the following code print out?
a = { 2 , 5 , 7 , 8 , 9 }
b = { 2 , 4 , 3 , 1 , 8 , 10 }
c = a.intersection(b)
a.add( 10 )
c.add( 15 )
d = a.difference(c)
e = b.union(a)
print (e, c)
print (e.symmetric_difference(c))

A：
c = {2,8}
a = { 2 , 5 , 7 , 8 , 9 ,10}
c = {2,8,15}
d = {5,7,9,10}
e = {2,4,3,1,8,10,5,7,9}
print out:
    {2,4,3,1,8,10,5,7,9} {2,8,15}
    {4,3,1,10,5,7,9,15}

b) What is the difference between .add() and .union() for sets?
The .add() method adds a value to the existing set, while the .union() method
creates a new set with the contents of the two sets put together.