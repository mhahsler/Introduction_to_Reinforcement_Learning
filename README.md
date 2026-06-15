
# Reinforcement Learning: Lecture Material, Simple Python Code Examples and Assignments

[![License: CC BY-NC-SA 4.0](https://img.shields.io/badge/License-CC_BY_NC_SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

<a href="http://incompleteideas.net/book/the-book.html">
  <img src="assets/RL_book_cover.jpg" align="right" style="height:15em;float: right">
</a>

__Under development!__ Caution, this page is currently incomlete and there may be 
missing files and mistakes in the provided materials.

This repository contains lecture material, simple Python code examples, and assignments for the course CS 5/7329 Reinforcement Learning taught by [Michael Hahsler](https://michael.hahsler.net/) at the [Department of Computer Science at SMU](https://www.smu.edu/Lyle/Academics/Departments/CS).

The code examples cover several chapters of the textbook 

> Richard S. Sutton, Andrew G. Barto,
> [_Reinforcement Learning: An Introduction,_](http://incompleteideas.net/book/the-book.html) 
> 2nd edition, MIT Press, Cambridge, MA, 2018.

Deep Reinforcement Learning (DRL) is based on the review paper

> Vincent François-Lavet, Peter Henderson, Riashat Islam, Marc G. Bellemare and Joelle Pineau, 
> [An Introduction to Deep Reinforcement Learning,](https://arxiv.org/abs/1811.12560) 
> _Foundations and Trends in Machine Learning,_ 11:3-4, pp 219-354. http://dx.doi.org/10.1561/2200000071, 2018.

Studying the material requires

* Python programming skills.
* Knowledge of AI basics (how intelligent agents interact with an environment).
* Knowledge of how to use machine learning techniques including deep learning. 
* Basic knowledge of probability and statistics, linear algebra, and calculus.

## Table of Contents

| Module | Book Chapter | Lecture Slides | Code |
| :----- | :----------- | :------------: | :--: |
| 1 | 1: Introduction | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter01.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter01.pptx) | [Code](Intro) | 
| 2 | 3: Finite Markov Decision Processes | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter03.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter03.pptx) | [Code](MDP) | 
|  |  **Part I: Tabular Methods** | |  | 
| 3 | 4: Dynamic Programming | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter04.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter04.pptx) | [Code](DP)  | 
| 4 | 5: Monte Carlo Methods | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter05.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter05.pptx) | [Code](MC) | 
| 5 | 6: Temporal-Difference Learning | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter06.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter06.pptx) | [Code](TD) | 
| - | 7: n-step Bootstrapping | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter07.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter07.pptx) | - | 
| - | 8: Planning and Learning with Tabular Methods | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter08.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter08.pptx) | - | 
|  |  **Part II: Approximate Solution Methods** | |  | 
| 6 | 9-10: Prediction and Control using Approximation | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter09.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter09.pptx) | [Code](Approximation) | 
| 7 | 12: Eligibility Traces | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter12.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter12.pptx) | [Code](Eligibility_Traces) | 
| 9 | 13: Policy Gradient Methods | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter13.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Chapter13.pptx) | [Code](Policy_Gradient) | 
|  |  **Looking Deeper** | |  |                                                                                                 | 10 | 17.3: Partial Observability | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Partial_Observability.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Partial_Observability.pptx) | - |
| 10 | 17.4: Reward Engineering | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Reward_Engineering.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_Reward_Engineering.pptx) | [Code](TD) |
| 10 | DRL: Deep Reinforcement Learning | [PDF](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_DRL.pdf), [PowerPoint](https://mhahsler.github.io/Introduction_to_Reinforcement_Learning/slides/Lecture_DRL.pptx) | [Code](DRL) | 
| 11 | X: Current Applications | - | - | 

## HOWTOs
* How to [debug in Jupyer Notebooks](https://colab.research.google.com/github/mhahsler/Introduction_to_Artificial_Intelligence/blob/master/HOWTOs/debugging_in_notebooks.ipynb)
* How to [profile Python code](https://colab.research.google.com/github/mhahsler/Introduction_to_Artificial_Intelligence/blob/master/HOWTOs/profiling_code.ipynb) to improve runtime.
* How to [make charts with mathplotlib and tables with pandas](https://colab.research.google.com/github/mhahsler/Introduction_to_Artificial_Intelligence/blob/master/HOWTOs/charts_and_tables.ipynb)
* How to [use random numbers and arrays in numpy](https://colab.research.google.com/github/mhahsler/Introduction_to_Artificial_Intelligence/blob/master/HOWTOs/random_numbers_and_arrays.ipynb)


## License

<a href="https://creativecommons.org/licenses/by-nc-sa/4.0/">
  <img src="assets/by-nc-sa.png" align="left" style="height:2em;float: left">
</a>

Introduction to Reinforcement Learning &copy; 2026 [Michael Hahsler](http://michael.hahsler.net) and others is licensed under 
[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).
