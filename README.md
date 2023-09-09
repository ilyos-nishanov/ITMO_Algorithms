# ITMO_Algorithms
BD&amp;ML

This is the repo of my code I did at ITMO MsBD&ML Algorithms course in the fall of 2023.
Task 1.

Report in pdf
Times New Roman 12pt, 1.0 spacing Send to: algorithms_itmo@mail.ru
Email topic: Task# X, Name and surname, Academic group
A separate email for each task!
Use any programming language you want. You can use existing implementations. The numerical results and plots should be informative and correct.

Title page:


FEDERAL STATE AUTONOMOUS EDUCATIONAL
INSTITUTION OF HIGHER EDUCATION
ITMO UNIVERSITY



Report
on the practical task No. 1 “Experimental time complexity analysis”




Performed by
Ilyosjon Nishanov
J4133c
Accepted by
Dr Petr Chunaev



	



St. Petersburg 2023
Goal
Analyzing the experimental study of the time complexity of different algorithms

Formulation of the problem
The time complexity of algorithms is a vital aspect in computer science and computational fields. By conducting experimental studies on the time complexity of different algorithms, researchers can gain a deeper understanding of how algorithms perform in terms of their execution time as the input size increases. This knowledge is significant for several reasons. First of all for algorithm selection. Experimental studies help researchers and developers choose the most efficient algorithm for a particular problem. By comparing the time complexities of different algorithms, they can identify the most suitable one that will provide optimal performance.
Secondly, for algorithm optimization, computational performance and problem-solving efficiency. Experimental studies provide insights into the bottlenecks and inefficiencies of algorithms. By analyzing the time complexity and observing the actual execution times, researchers can identify areas for optimization and enhance the algorithm's efficiency. The study of time complexity helps in estimating the computational resources required by an algorithm. It allows researchers to predict the performance of an algorithm on different hardware and software configurations, enabling better resource allocation and system design. Understanding the time complexity of algorithms enables researchers to design more efficient algorithms for solving complex problems. By analyzing the time complexity, they can develop algorithms that can handle large-scale data and computational challenges more effectively.
Last but not least experimental studies of the time complexity of algorithms helps advance computational fields. Many fields, such as data analysis, machine learning, and optimization, heavily rely on efficient algorithms. Experimental studies on time complexity contribute to the advancement of these fields by providing insights into algorithmic efficiency, leading to faster and more accurate computations.

Brief theoretical part
Time complexity analysis is a fundamental aspect of algorithm design and analysis. It provides a theoretical understanding of how the execution time of an algorithm grows as the input size increases. Experimental studies complement this theoretical analysis by providing empirical evidence of the actual execution times of algorithms for different input sizes. Here are some key concepts and approaches related to the experimental study of time complexity:
1. Time Complexity: Time complexity is a measure of the computational resources (typically time) required by an algorithm to solve a problem as a function of the input size. It describes the relationship between the input size and the number of operations performed by the algorithm.
2. Big O Notation: Big O notation is commonly used to express the upper bound of an algorithm's time complexity. For example, if an algorithm has a time complexity of O(n^2), it means the number of operations grows quadratically with the input size.
3. Algorithmic Paradigms: Different algorithmic paradigms, such as divide and conquer, dynamic programming, and greedy algorithms, have their own characteristic time complexities. Experimental studies help validate the theoretical predictions and compare the actual performance of algorithms within these paradigms.
4. Methodological Approaches: Experimental studies of time complexity typically involve the following methodological approaches:
   a. Input Generation: Researchers generate inputs of varying sizes to evaluate the algorithm's performance. Input generation methods can include random data, worst-case scenarios, or real-world data.
   b. Execution Time Measurement: The execution time of the algorithm is measured using timestamps or profiling tools. Multiple runs are performed to account for variations in system load and ensure accurate average execution times.
   c. Statistical Analysis: Researchers analyze the collected data to derive meaningful insights. Statistical techniques, such as calculating mean, standard deviation, and confidence intervals, are employed to assess the algorithm's performance and compare it with theoretical expectations.
   d. Benchmarking: Benchmarking involves comparing the execution times of different algorithms for the same problem. Researchers run multiple algorithms on the same inputs and measure their performance to identify the most efficient solution.
   e. Complexity Classes: Experimental studies can focus on comparing algorithms belonging to the same complexity class, such as polynomial-time algorithms (P), exponential-time algorithms (EXP), or NP-hard problems. This analysis helps validate the theoretical classifications and provides a practical understanding of algorithmic efficiency.
Experimental studies of time complexity play a crucial role in algorithm analysis and design. They help researchers validate theoretical predictions, refine algorithmic choices, and optimize performance. By comparing empirical results with theoretical expectations, researchers gain insights into algorithm behavior, identify areas for improvement, and make informed decisions about algorithm selection and optimization. These studies contribute to the advancement of computational fields, enabling more efficient and scalable solutions to complex problems.

Results
This chapter aims to analyze the empirical execution time of various algorithms and functions implemented on an n-dimensional random vector. The algorithms and functions include a constant function, sum of elements, product of elements, polynomial evaluation using direct calculation and Horner's method, Bubble Sort, Quick Sort, and Timsort. The execution times are measured for five runs with varying values of n from 1 to 2000. The empirical results are then compared to the theoretical time complexities of the algorithms to evaluate their performance.
We will generate an n-dimensional random vector, denoted as v=[v_1, v_2, ..., v_n], where the elements are non-negative. We will then implement each algorithm or function and measure the execution time using timestamps. For each algorithm, we run the program five times with varying values of n from 1 to 2000. The average execution time is calculated for each value of n. Afterwards we will conduct a theoretical analysis of the time complexity for each algorithm. This analysis provides an estimation of the expected time required based on the algorithm's design and operations performed. Then we will plot the average execution time as a function of n to visualize the empirical results. The theoretical time complexities are compared with the empirical measurements to evaluate the performance of the algorithms. Any disparities between the empirical and theoretical time complexities are noted and discussed.

        Constant Function	 O(1)
        Sum of Elements	 O(n)
        Product of Elements	 O(n)
        Polynomial Evaluation (Direct)	 O(n)
        Polynomial Evaluation (Horner)	 O(n)
        Bubble Sort	 O(n^2)
        Quick Sort	 O(n log n)
        Timsort	 O(n log n)



Conclusions
Make conclusions on the results obtained and on the achievement of the goal of your work


Appendix
Present the listings of programs written for performing the task, with comments. You can use a GitHub link instead
