```
wordsPairRdd
    key      value
    (python, 1)
    (python, 1)
    (java, 1)
    (jvm, 1)
    (java, 1)
    (python, 1)
table 
key , acc
python , acc-accumulator = 2
java, acc = 1
jvm, acc = 3

   lambda acc, occ: acc + occ

   then it calls lambda for python (acc 0, occ 1 value from tuple), returns 0 + 1 = 1,
      then returned value updated in table - python

   calls lambda for python (acc 1, occ 1), returns 1 + 1 = 2, 2 is updated in table python


    calls lambda for java (acc 0, occ 1), returns 0 + 1 = 1, 1 is updated in table java 
    calls lambda for jvm (acc 0, occ 1), returns 0 + 1 = 1, 1 is updated in table jvm 
    calls lambda for java (acc 1, occ 1), returns 1 + 1 = 2, 2 is updated in table java 
    calls lambda for python (acc 2, occ 1), returns 2 + 1 = 3, 3 is updated in table python

   
wordCounts = wordsPairRdd.reduceByKey(lambda acc, occ: acc + occ)

```
