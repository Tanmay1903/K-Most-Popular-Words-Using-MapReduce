# K-Most-Popular-Words-Using-MapReduce
To implement Mapreduce Function in Hadoop to Identify the top 100 most Frequently occurring words in given dataset of 16GB.

## Problem Statement:
The objective of this programming assignment is to develop an efficient MapReduce solution to identify the top K most frequently
occurring words in a given dataset. The value of K is predefined and represents the number of words to be identified (e.g., K = 10).
It is essential to exclude stop words, such as common words like "the" and "a," based on a predetermined list of stop words. 
Additionally, the program should consider case sensitivity, treating words with different capitalizations as distinct entities.
The solution should be designed to handle large datasets using the MapReduce paradigm and should be executed separately for each 
of the three input data files. To ensure the code's accuracy and efficiency, it is advisable to test it initially on a smaller text file,
such as one with a size of 10MB, before scaling up to larger datasets.
To evaluate the program's performance, various metrics can be employed, including execution time, speedup, CPU utilization, and memory
usage. Other relevant metrics can also be utilized to provide a comprehensive analysis. It is crucial to justify the choice of algorithms
and data structures employed in the solution through a detailed explanation.
The input dataset primarily consists of English alphabets, white spaces, and hyphen-separated words. The program should be designed
to handle such inputs effectively. The implementation should strive to achieve the best possible execution time and overall performance
on the given computer system.

## System Configurations
-	Processor: Apple M1 chip.
-	Cores: 10 number of cores.
-	Memory: 8 GB RAM available on the system.
-	Storage Type: SSd storage with 256 GB storage space
-	Storage size available: Available disk space.
-	Operating System: macOS Ventura
-	Programming Language: Python3
-	Compiler and Runtime Environment: Hadoop

## Files in the Project
- ### mapper.py:
  - The mapper.py file is used in the Hadoop MapReduce framework to preprocess data before it is passed to the reducer. 
  - It imports the sys module, which is needed for reading from and writing to standard input and output.
  - It defines a list of English stopwords, which are common words that are generally filtered out of text data because
    they are not useful for analysis.
  - It reads each line from standard input and strips any leading or trailing whitespace. 
  - It splits the line into individual words using whitespace as the delimiter.
  - It loops through each word and, if the word is not a stopword, it writes the word to standard output with a count of 1. 
  - This output will be consumed by the reducer.py script, which will aggregate the counts for each word and produce a final output.
  - Overall, the purpose of this mapper.py file is to tokenize and normalize the text data, removing stopwords and preparing it for 
    further analysis or processing.
  
