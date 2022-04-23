# Importing required libraries
import seaborn as sb
import matplotlib.pyplot as plt
import numpy as np

# Importing required libraries for Uniform Distribution
from scipy.stats import uniform

# Importing required modules for Binomaial Distribution.
from scipy.stats import binom

# Importing the required modules for Binomial Distribution
from scipy.stats import bernoulli

# Importing required modules for Expontial Distribution
from scipy.stats import expon

# import required libraries for Normal Distribution
from scipy.stats import norm

while True:
    print(
        "Select type of Distribution.\n1:Uniform Distribution.\n2:Binomial Distribution.\n3:Poisoon "
        "Distribution.\n4:Exponential Distribution.\n5:Normal Distribution.")

    ch = int(input("Enter your choice."))
    if ch == 1:
        # taking random variables from Uniform distribution
        data = uniform.rvs(size=100000, loc=5, scale=10)

        # Plotting the results
        sb.set_style('whitegrid')
        ax = sb.distplot(data, bins=30, color='k')
        ax.set(xlabel='interval')
        plt.show()


    elif ch == 2:
        pb = binom(n=20, p=0.6)

        x = np.arange(1, 21)
        pmf = pb.pmf(x)

        # Visualizing the distribution
        sb.set_style('whitegrid')
        plt.vlines(x, 0, pb.pmf(x), colors='k', linestyles='-', lw=5)
        plt.ylabel('Probability')
        plt.xlabel('Intervals')
        plt.show()

    elif ch == 3:
        # Applying the bernoulli class
        data = bernoulli.rvs(size=5000, p=0.8)

        # Visualizing the results
        sb.set_style('whitegrid')
        sb.displot(data, discrete=True, shrink=.8, color='k')
        plt.show()

    elif ch == 4:

        # Applying the expon class methods
        x = np.linspace(0.001, 10, 100)
        pdf = expon.pdf(x)

        # Visualizing the results
        sb.set_style('whitegrid')
        plt.plot(x, pdf, 'r-', lw=2, alpha=0.6, label='expon pdf', color='k')
        plt.xlabel('intervals')
        plt.ylabel('Probability Density')
        plt.show()

    elif ch == 5:
        # Creating the distribution
        data = np.arange(1, 10, 0.01)
        pdf = norm.pdf(data, loc=5.3, scale=1)

        # Visualizing the distribution

        sb.set_style('whitegrid')
        sb.lineplot(data, pdf, color='black')
        plt.ylabel('Probability Density')

    elif ch == 0:
        break

    else:
        print("Please, Select proper option.")
