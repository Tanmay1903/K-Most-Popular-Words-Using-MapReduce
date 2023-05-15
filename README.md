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
- ### reducer.py:
  - The reducer.py file is also used in the Hadoop MapReduce framework, specifically to aggregate the output produced by the mapper. 
  - It initializes some variables to keep track of the current word being processed and its count.
  - It reads each line of input from standard input and strips any leading or trailing whitespace.
  - It splits the line into a word and a count value, which were separated by a tab character in the output produced by the mapper.
  - It tries to convert the count value to an integer, and silently ignores any lines where this conversion fails.
  - It compares the current word to the previous word. If they are the same, it adds the current count to the running total for that word.       If they are different, it outputs the total count for the previous word to standard output and resets the running total for the current     word.
  - Finally, it outputs the count for the last word to standard output, since the loop above only outputs when it detects a new word.
  - Overall, the reducer.py file is responsible for aggregating the counts of the words that were produced by the mapper.py file. It reads       the output of the mapper, which is sorted by word, and sums up the counts for each word, outputting the final results to standard           output.
- ### result.py:
  - The result.py script reads the output generated by the reducer.py script, which is a list of words and their corresponding count.
  - It uses the heapq library to get the top 100 words based on their count. The heapq.nlargest() function takes three arguments: the number     of items to return (100), the iterable to search (word_count.items()), and a key function to determine the order (lambda x: x[1], which     sorts the items by their second value, i.e. the count).
  - The script then loops through the top 100 words and their counts and prints them to standard output. The output consists of the word and     its count, separated by a space.
## How to run the code.
After successful installation of Hadoop, there are two steps to get the 'K-Most-Popular-Words-Using-MapReduce'. 
- Run the MapReduce Framework to read the file line-by-line, split the line into words and print each word (excluding stopwords) with count 1. Reducer is responsible for aggregating the counts of the words that were produced by the mapper.py file. It reads the output of the mapper, which is sorted by word, and sums up the counts for each word, outputting the final results to standard output. Cammand to run the MapReduce Framework is as follows:
  - ``` hadoop jar <PATH_TO_YOUR_HADOOP_STREAMING_JAR> -input <PATH_TO_YOUR_INPUT_FILE_IN_HADOOP> -output <PATH_TO_YOUR_OUTPUT_DIRECTORY_IN_HADOOP> -mapper "python3 <PATH_TO_YOUR_MAPPER_FILE>" -reducer "python3 <PATH_TO_YOUR_REDUCER_FILE>"```
Example in my case:
``` 
hadoop jar /Users/tanmaysingla/hadoop-3.3.5/share/hadoop/tools/lib/hadoop-streaming-3.3.5.jar -input /data/input/data_16GB.txt -output /data/output16 -mapper "python3 /Users/tanmaysingla/Desktop/BigDataAssn2/Assn_2_python/mapper.py" -combiner "python3 /Users/tanmaysingla/Desktop/BigDataAssn2/Assn_2_python/reducer.py" -reducer "python3 /Users/tanmaysingla/Desktop/BigDataAssn2/Assn_2_python/reducer.py"
```
