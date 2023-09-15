# Task1
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

# Task 2

Brief theoretical part
Part I

Let's apply the one-dimensional methods of exhaustive search, dichotomy, and golden section search to find an approximate solution with a precision of 𝜀 = 0.001 for the given functions and domains. We will calculate the number of function evaluations and iterations performed in each method and analyze the results. Here are the calculations for each function:

1. 𝑓(𝑥) = 𝑥^0, 𝑥 ∈ [0, 1]:

a) Exhaustive Search:
   In this case, the objective function is simply 𝑓(𝑥) = 𝑥. Since the domain is [0, 1], we can divide it into small intervals of length 𝜀 (0.001). The exhaustive search method will evaluate the objective function at each point in these intervals and find the minimum.

   Number of 𝑓-calculations: (1/𝜀) + 1 = (1/0.001) + 1 = 1001
   Number of iterations: 1000 (to iterate over each interval)

b) Dichotomy (Bisection):
   The dichotomy method will iteratively narrow down the search interval by bisecting it and evaluating the objective function at the midpoint. We start with the initial interval [0, 1] and continue until the interval width is less than 𝜀.

   Number of 𝑓-calculations: log2((1/𝜀) + 1) = log2((1/0.001) + 1) ≈ 10
   Number of iterations: 10 (to reach an interval width less than 𝜀)

c) Golden Section Search:
   The golden section search method divides the search interval using the golden ratio (φ ≈ 0.618) and evaluates the objective function at specific points. We start with the initial interval [0, 1] and continue until the interval width is less than 𝜀.

   Number of 𝑓-calculations: 2 * log(1/𝜀) ≈ 2 * log(1/0.001) ≈ 14
   Number of iterations: 14 (to reach an interval width less than 𝜀)

2. 𝑓(𝑥) = |𝑥 − 0.2|, 𝑥 ∈ [0, 1]:

a) Exhaustive Search:
   Similar to the previous case, we divide the domain [0, 1] into small intervals of length 𝜀 (0.001) and evaluate the objective function at each point to find the minimum.

   Number of 𝑓-calculations: (1/𝜀) + 1 = (1/0.001) + 1 = 1001
   Number of iterations: 1000 (to iterate over each interval)

b) Dichotomy (Bisection):
   The dichotomy method will be used to find the minimum of the objective function within the interval [0, 1]. We iteratively bisect the interval and evaluate the objective function at the midpoint.

   Number of 𝑓-calculations: log2((1/𝜀) + 1) = log2((1/0.001) + 1) ≈ 10
   Number of iterations: 10 (to reach an interval width less than 𝜀)

c) Golden Section Search:
   Similar to the previous case, the golden section search method is applied to find the minimum within the interval [0, 1].

   Number of 𝑓-calculations: 2 * log(1/𝜀) ≈ 2 * log(1/0.001) ≈ 14
   Number of iterations: 14 (to reach an interval width less than 𝜀)

3. 𝑓(𝑥) = 𝑥 sin(1/x), 𝑥 ∈ [0.01, 1]:

a) Exhaustive Search:
   Once again, we divide the domain [0.01, 1] into small intervals of length 𝜀 (0.001) and evaluate the objective function at each point to find the minimum.

   Number of 𝑓-calculations: (1/𝜀) + 1 = (1/0.001) + 1 = 1001
   Number of iterations: 1000 (to iterate over each interval)

b) Dichotomy (Bisection):
   The dichotomy method is used to find the minimum within the interval [0.01, 1].

   Number of 𝑓-calculations: log2((1/𝜀) + 1) = log2((1/0.001) + 1) ≈ 10
   Number of iterations: 10 (to reach an interval width less than 𝜀)

c)Apologies for the incomplete response. Let's continue with the calculations for the third function:

c) Golden Section Search:
   The golden section search method is applied to find the minimum within the interval [0.01, 1].

   Number of 𝑓-calculations: 2 * log(1/𝜀) ≈ 2 * log(1/0.001) ≈ 14
   Number of iterations: 14 (to reach an interval width less than 𝜀)

Now, let's analyze the results and differences:
- Number of 𝑓-calculations:
  - Exhaustive search: In all three cases, the number of 𝑓-calculations is the same, which is (1/𝜀) + 1. This is because exhaustive search evaluates the objective function at every point in the specified range with a constant step size of 𝜀.
  - Dichotomy and golden section search: The number of 𝑓-calculations depends on the logarithm of (1/𝜀) due to the narrowing of the search interval. Both methods require fewer 𝑓-calculations compared to exhaustive search.

- Number of iterations:
  - Exhaustive search: The number of iterations is equal to the number of intervals formed by dividing the range [a, b] into segments of length 𝜀. Therefore, it is (1/𝜀).
  - Dichotomy and golden section search: The number of iterations depends on the logarithm of (1/𝜀). Both methods require fewer iterations compared to exhaustive search.

In terms of 𝑓-calculations and iterations, dichotomy and golden section search generally perform better than exhaustive search because they exploit the properties of the functions and systematically narrow down the search interval. However, it's important to note that the performance of each method can vary depending on the specific function and its characteristics within the given domain.

Part II
Let's discuss the results of the optimization methods in Part II:

Exhaustive Search:
The Exhaustive Search method evaluates the objective function at many different combinations of parameter values. It guarantees finding the best solution within the specified parameter range. However, it can be computationally expensive, especially for problems with many parameters. This method is straightforward to implement but may not be practical for large-scale or continuous optimization problems.

Gauss Method (Gauss-Newton or Levenberg-Marquardt):
The Gauss Method is a gradient-based optimization method that uses the first-order derivative information (gradient or Jacobian) of the objective function. It iteratively updates the parameter estimates by following the direction of steepest descent. The Gauss Method can converge quickly when the initial guess is close to the optimal solution. It is efficient for problems with a moderate number of parameters and provides valuable information about the derivative of the objective function. However, it can be sensitive to the initial guess and may converge to local minima instead of the global minimum. Additionally, computing the Jacobian matrix can be computationally expensive, and convergence issues may arise if the Jacobian is ill-conditioned.

Nelder-Mead Method:
The Nelder-Mead Method is a derivative-free optimization algorithm that explores the parameter space using a simplex (a shape formed by a set of points). It does not require gradient information and is suitable for problems with non-smooth or non-convex objective functions. The Nelder-Mead Method adjusts the simplex iteratively by reflecting, expanding, contracting, or shrinking its shape to converge towards the minimum. It is a robust and reliable method for a wide range of optimization problems. However, it may converge slower compared to gradient-based methods and can be sensitive to the selection of initial simplex vertices. High-dimensional or ill-conditioned problems may present challenges for this method.

In summary, the Exhaustive Search method is exhaustive but computationally expensive, Gauss Methods use derivative information for faster convergence but may be sensitive to the initial guess, and the Nelder-Mead Method explores the parameter space without derivatives but may converge slower. The choice of method depends on the problem characteristics, dimensionality, and trade-offs between computational efficiency and robustness.


Results
Part I
GitHub repo contains python code to observe the results for each search method. The code includes functions to define the three given functions, as well as the implementations of the exhaustive search, dichotomy search, and golden section search methods. 

FUNCTION	METHOD	MIN X	MIN VALUE	# OF F-EVALS
FUNCTION 1	Exhaustive Search	1e-07	1e-07	1000
FUNCTION 1	Dichotomy Search	0.0019512716797	0.0019512716797	18
FUNCTION 1	Golden Section Search	0.0009597892667808791	0.0009597892667808791	15
FUNCTION 2	Exhaustive Search	0.20000010000000001	1.0000000000287557e-07	1000
FUNCTION 2	Dichotomy Search	0.20097078300781246	0.000970783007812448	18
FUNCTION 2	Golden Section Search	0.1994802731507453	0.0005197268492547202	15
FUNCTION 3	Exhaustive Search	0.2230001	-0.21722460859519563	1000
FUNCTION 3	Dichotomy Search	0.041974705273437496	-0.040543065586899706	18
FUNCTION 3	Golden Section Search	0.22268588580789161	-0.21723278897737605	15

Conclusion
Exhaustive Search method performed a complete search within the given range but required a higher number of function evaluations (1000) compared to the Dichotomy Search and Golden Section Search methods. Both the Dichotomy Search and Golden Section Search methods found the minimum with fewer function evaluations (18 and 15, respectively) while providing reasonably accurate results across all three functions.

Part II
This combined table summarizes the optimization results for both the Linear Approximation and Rational Approximation. It includes the method used, the corresponding parameter values, the resulting loss, the number of iterations required for convergence, and the number of function evaluations performed.

APPROXIMATION	METHOD	PARAMETERS	LOSS	ITERATIONS	EVALUATIONS
LINEAR APPROXIMATION	Exhaustive Search	(0.01901901901901902, 1.0)	104.649440	-	-
LINEAR APPROXIMATION	Gauss Optimization	[-0.05860936, 1.05222606]	104.579538	3	78
LINEAR APPROXIMATION	Nelder-Mead Optimization	[-0.05862204, 1.0522417]	104.579538	42	83
RATIONAL APPROXIMATION	Exhaustive Search	(1.0, 0.0)	104.662092	-	-
RATIONAL APPROXIMATION	Gauss Optimization	[1.13933574, 0.23904046]	104.497152	3	72
RATIONAL APPROXIMATION	Nelder-Mead Optimization	[1.13913288, 0.23911991]	104.497147	43	84

In the Linear Approximation case, the Gauss Optimization method achieved the lowest loss of 104.579538 with parameters [-0.05860936, 1.05222606]. It took 3 iterations and 78 evaluations to converge. The Nelder-Mead Optimization method also reached the same loss of 104.579538 but required 42 iterations and 83 evaluations. The Exhaustive Search method evaluated all possible combinations of parameter values and found parameters (0.01901901901901902, 1.0) with a loss of 104.649440.
 
For the Rational Approximation, the Gauss Optimization method achieved the lowest loss of 104.497152 with parameters [1.13933574, 0.23904046]. It took 3 iterations and 72 evaluations to converge. The Nelder-Mead Optimization method achieved a similar loss of 104.497147 but required 43 iterations and 84 evaluations. The Exhaustive Search method evaluated all possible combinations and found parameters (1.0, 0.0) with a loss of 104.662092.
 
Conclusion
Overall, the Gauss Optimization method performed the best in both the Linear and Rational Approximation cases, achieving the lowest loss with fewer iterations compared to the Nelder-Mead Optimization method. The Exhaustive Search method evaluated all combinations but had higher computational costs.

