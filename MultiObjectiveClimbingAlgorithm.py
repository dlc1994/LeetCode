# encoding: utf-8
'''
@author: Lingcheng Dai
@contact: 2013210288@bupt.edu.cn
@file: MultiObjectiveClimbingAlgorithm.py
@time: 2018/9/5 21:42
'''
# encoding:utf8
from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random

#define objective function
def evaluate(x1, x2):
    # x1, x2 = vector
    # def mul(x1, x2, alis=1):
    #     return alis * np.exp(-(x1 * x1 + x2 * x2))
    # return mul(x1, x2) + mul(x1, x2, 2)
    # x = np.array(vector)
    # simulations = sum(100.0 * (x[1:] - x[:-1] ** 2.0) ** 2.0 + (1 - x[:-1]) ** 2.0)
    # H = np.exp(-(x1**2 + x2**2)/ 2 / 3**2)
    return -(x1**2+x2**2)


def show(X, Y, Z):
    fig = plt.figure()
    ax = Axes3D(fig)
    plt.title("demo_hill_climbing")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow', )
    ax.set_xlabel('x label', color='r')
    ax.set_ylabel('y label', color='g')
    ax.set_zlabel('z label', color='b')
    plt.show()

def MultiObjectClimb(X0, x_range):
    best_sol = X0
    while True:
        best_evaluate = evaluate(best_sol[0], best_sol[1])
        current_best_value = best_evaluate
        sols = [best_sol]

        for i in range(len(best_sol)):
            if best_sol[i] > x_range[i][0]:
                sols.append(best_sol[0:i] + [best_sol[i]-0.0001] + best_sol[i+1:])
            if best_sol[i] < x_range[i][1]:
                sols.append(best_sol[0:i] + [best_sol[i]+0.0001] + best_sol[i+1:])
        print(sols)
        for s in sols:
            el = evaluate(s[0], s[1])
            if el < best_evaluate:
                best_sol = s
                best_evaluate = el
        if abs(best_evaluate - current_best_value)<=0.001:
            break

def drawPaht(X, Y, Z, px, py, pz):
    fig = plt.figure()
    ax = Axes3D(fig)
    plt.title("demo_hill_climbing")
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow', )
    ax.set_xlabel('x label', color='r')
    ax.set_ylabel('y label', color='g')
    ax.set_zlabel('z label', color='b')
    ax.plot(px,py,pz,'r.') #绘点
    plt.show()

#产生[a,b]区间内小数点后几位的若干个随机数
def GenerateRamdom(bound, Count, precision):
    low_bound, high_bound = bound
    GenerateList=[]
    for i in range(1, Count + 1):
        GenerateList.append(round(random.uniform(low_bound, high_bound), precision))
        i += 1
    return GenerateList

if __name__ == '__main__':
    X = np.arange(-10, 10, 1)
    Y = np.arange(-10, 10, 1)
    # Z = [([0] * len(X)) for i in range(len(Y))]
    # print(Z)
    # for x in X:
    #     for y in Y:
    #         Z[x][y] = evaluate([x, y])
    # Z = np.array(Z, dtype=float)
    # print(Z.shape)
    X, Y = np.meshgrid(X, Y)
    Z = evaluate(X, Y)
    # len_x = len(X)
    # len_y = len(Y)
    # (evaluate([X, Y]))
    # 随机登山点
    # st_x = np.random(0, len_x - 1)
    # st_y = np.random(0, len_y - 1)

    # x_range = [ [-2, 4], [-2, 4] ]
    # x0 = [GenerateRamdom(x_range[0]), GenerateRamdom(x_range[1])]


    show(X,Y,Z)