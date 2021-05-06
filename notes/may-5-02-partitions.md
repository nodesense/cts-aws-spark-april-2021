```
Partitions
    
    subset of the whole data, split to chunk.
    to get all the data, union (part 00, part 01, ..part 0n)
    data - split the data into chunks

    data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    1 partition - P0 - [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    2 Partitions
        P0 - [10, 20, 30, 40, 50]
        P1 - [60, 70, 80, 90, 100]

    3 partitions 
        P0 - [10, 20, 30, ]
        P1 - [40, 50, 60, ]
        P2 - [70, 80, 90, 100]

        .collect()

        union (P0, P1, P2) - [10, 20, 30, 40, 50, 60, 70, 80, 90,100]
        union (P2, P1, P0) - [70, 80, 90, 100,  40, 50, 60, 10, 20, 30]
        ```
