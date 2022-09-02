# -*- coding: utf-8 -*- 
# %reset -f
"""
@author: Hiromasa Kaneko

Modified by
Copyright from: 11.17.2021
CSRS, RIKEN
Auther: Shunji Yamada
"""
# Demonstration of inverse GTMR (Generative Topographic Mapping Regression) with multiple y-variables

import matplotlib.figure as figure
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d
import numpy as np
#from dcekit.generative_model import GTM
from gtm import GTM
from gmr import GMR
import pandas as pd
from sklearn.datasets.samples_generator import make_s_curve

import sys
import os.path
from tkinter import messagebox

class module1:
 def __init__(self, filePath1, filePath2, dirPathOut):
 #def __init__(self, filePath1, filePath2, filePath3, dirPathOut):
    searchDir_input_data = filePath1 #sys.argv[1]     # ReadDir-input_data
    #searchDir_x_for_prediction = filePath2 #sys.argv[2]     # ReadDir-x_for_prediction
    searchDir_settings = filePath2 #sys.argv[3]     # ReadDir-settings
    saveDirName     = dirPathOut #sys.argv[4]      # saveDir

    #target_y_value = [-0.5, -5]  # y-target for inverse analysis
    # target_y_value = [0, 0]
    # target_y_value = [0.5, 5]

    # settings
    settings = pd.read_csv(searchDir_settings, index_col=0, header=0)
    target_y_value = settings.loc["target_y_value"].astype(float).to_list()
    print("target_y_value")
    print(target_y_value)
    number_of_y_to_predict = len(target_y_value)#3
    print("number_of_y_to_predict")
    print(number_of_y_to_predict)
    #target_y_value = [int(settings.loc["target_y_value", "parameter1"]),int(settings.loc["target_y_value", "parameter2"]),int(settings.loc["target_y_value", "parameter3"])]#[65,150,305]
    shape_of_map = [int(settings.loc["shape_of_map", "parameter1"]),int(settings.loc["shape_of_map", "parameter2"])]#[60,60]#[30, 30]
    shape_of_rbf_centers = [int(settings.loc["shape_of_rbf_centers", "parameter1"]),int(settings.loc["shape_of_rbf_centers", "parameter2"])]#[6,6]
    variance_of_rbfs = float(settings.loc["variance_of_rbfs", "parameter1"])#0.125
    lambda_in_em_algorithm = float(settings.loc["lambda_in_em_algorithm", "parameter1"])#0.0625
    number_of_iterations = int(settings.loc["number_of_iterations", "parameter1"])#20#300
    display_flag = settings.loc["display_flag", "parameter1"]#True

    #file_name = r"C:\Users\shunj\OneDrive\ドキュメント\Jupyter\testPLA20200904a2.csv"#'virtual_resin_x.csv'
    savepath0 = os.path.join(saveDirName, 'results.txt')
    #number_of_xy=323
    print('input data')
    #with open(savepath0, 'a') as f:
    #    print('input data', file=f)
    testx = pd.read_csv(searchDir_input_data, index_col=0, header=0)

    print(testx)
    #with open(savepath0, 'a') as f:
    #    print(testx, file=f)
    number_of_xy = len(testx.iloc[1,:])
    print("number_of_xy")
    print(number_of_xy)
    end_of_x = number_of_xy - number_of_y_to_predict
    numbers_of_x = list(range(0, end_of_x))
    #numbers_of_x = [0, 1, 2]
    print("numbers_of_x")
    print(numbers_of_x)
    numbers_of_y = list(range(end_of_x, number_of_xy))#[len(testx.iloc[1,:n])-3,len(testx.iloc[1,:n])-2,len(testx.iloc[1,:n])-1]
    print("numbers_of_y")
    print(numbers_of_y)
    #numbers_of_y = [3, 4]
    random_state_number = 30000
    number_of_samples = 1000
    noise_ratio_of_y = 0.1
    # Generate samples for demonstration
    """
    np.random.seed(seed=100)
    x1, color = make_s_curve(number_of_samples, random_state=random_state_number)
    raw_y1 = 0.3 * x1[:, 0] - 0.1 * x1[:, 1] + 0.2 * x1[:, 2]
    y1 = raw_y1 + noise_ratio_of_y * raw_y1.std(ddof=1) * np.random.randn(len(raw_y1))
    raw_y2 = np.arcsin(x1[:, 0]) + np.log(x1[:, 1]) - 0.5 * x1[:, 2] ** 4 + 5
    y2 = raw_y2 + noise_ratio_of_y * raw_y2.std(ddof=1) * np.random.randn(len(raw_y2))
    print(x1[:,0].shape)

    print(y1.shape)
    print(y2.shape)
    xy = np.vstack((y1,y2,x1[:,0],x1[:,1],x1[:,2]))
    xyt =xy.T
    np.savetxt('demo_data.csv', xyt, delimiter=",")
    #np.savetxt('demo_data_x1.csv', x1, delimiter=",")
    #np.savetxt('demo_data_y1.csv', y1, delimiter=",")
    #np.savetxt('demo_data_y2.csv', y2, delimiter=",")
    """
    x1 = testx.iloc[:,number_of_y_to_predict:]
    print('x1')
    print(x1)
    """
    y1 = testx["Tg"]
    print('y1')
    print(y1)
    y2 = testx["Tm"]
    print('y2')
    print(y2)
    y3 = testx["Td"]
    print('y3')
    print(y3)
    """
    yall = testx.iloc[:,:number_of_y_to_predict]
    print('yall')
    print(yall)
    """
    # plot y1 vs. y2
    plt.rcParams['font.size'] = 18
    #plt.figure(figsize=figure.figaspect(1))
    plt.figure(figsize=(10, 10))
    plt.scatter(y1, y2)
    plt.xlabel('y1')
    plt.ylabel('y2')
    #figurename1 = 'estimated_y_No'+str(figureNo)+'_in_cv.png'
    figurename1 = 'plot y1 vs. y2.png'
    figurepath1 = os.path.join(saveDirName, figurename1)
    plt.savefig(figurepath1)
    plt.show()
    """

    #variables = np.c_[x, y1, y2]

    variables = np.concatenate([x1, yall], axis=1)#np.c_[x1, y1, y2, y3]
    print('variables')
    print(variables)
    # standardize x and y
    autoscaled_variables = (variables - variables.mean(axis=0)) / variables.std(axis=0, ddof=1)
    target_y_value = np.array(target_y_value)
    autoscaled_target_y_value = (target_y_value - variables.mean(axis=0)[numbers_of_y]) / variables.std(axis=0, ddof=1)[
        numbers_of_y]

    # construct GTMR model
    model = GTM(shape_of_map, shape_of_rbf_centers, variance_of_rbfs, lambda_in_em_algorithm, number_of_iterations,
                display_flag)
    model.fit(autoscaled_variables)

    if model.success_flag:
        # calculate of responsibilities
        responsibilities = model.responsibility(autoscaled_variables)
        means, modes = model.means_modes(autoscaled_variables)

        plt.rcParams['font.size'] = 18
        for y_number in numbers_of_y:
            # plot the mean of responsibilities
            #plt.figure(figsize=figure.figaspect(1))
            plt.figure(figsize=(10, 10))
            plt.scatter(means[:, 0], means[:, 1], c=variables[:, y_number])
            plt.colorbar()
            plt.ylim(-1.1, 1.1)
            plt.xlim(-1.1, 1.1)
            plt.xlabel('z1 (mean)')
            plt.ylabel('z2 (mean)')
            figureNo = y_number - end_of_x
            figurename2 = 'the mean of responsibilities_y_No'+str(figureNo)+'.png'
            figurepath2 = os.path.join(saveDirName, figurename2)
            plt.savefig(figurepath2)
            plt.show()
            # plot the mode of responsibilities
            #plt.figure(figsize=figure.figaspect(1))
            plt.figure(figsize=(10, 10))
            plt.scatter(modes[:, 0], modes[:, 1], c=variables[:, y_number])
            plt.colorbar()
            plt.ylim(-1.1, 1.1)
            plt.xlim(-1.1, 1.1)
            plt.xlabel('z1 (mode)')
            plt.ylabel('z2 (mode)')
            figurename3 = 'the mode of responsibilities_y_No'+str(figureNo)+'.png'
            figurepath3 = os.path.join(saveDirName, figurename3)
            plt.savefig(figurepath3)
            plt.show()

        # GTMR prediction for inverse analysis
        mean_of_estimated_mean_of_x, mode_of_estimated_mean_of_x, responsibilities_y, py = \
            model.predict(autoscaled_target_y_value, numbers_of_y, numbers_of_x)

        # Check results of inverse analysis
        print('Results of inverse analysis')
        with open(savepath0, 'a') as f:
            print('Results of inverse analysis', file=f)
        x=x1.values
        mean_of_estimated_mean_of_x = mean_of_estimated_mean_of_x * x.std(axis=0, ddof=1) + x.mean(axis=0)
        mode_of_estimated_mean_of_x = mode_of_estimated_mean_of_x * x.std(axis=0, ddof=1) + x.mean(axis=0)
        #    print('estimated x-mean: {0}'.format(mean_of_estimated_mean_of_x))
        print('estimated x-mode: {0}'.format(mode_of_estimated_mean_of_x))
        with open(savepath0, 'a') as f:
            print('estimated x-mode: {0}'.format(mode_of_estimated_mean_of_x), file=f)

        estimated_x_mean_on_map = responsibilities_y.dot(model.map_grids)
        estimated_x_mode_on_map = model.map_grids[np.argmax(responsibilities_y), :]
        #    print('estimated x-mean on map: {0}'.format(estimated_x_mean_on_map))
        print('estimated x-mode on map: {0}'.format(estimated_x_mode_on_map))
        with open(savepath0, 'a') as f:
            print('estimated x-mode on map: {0}'.format(estimated_x_mode_on_map), file=f)
        #plt.figure(figsize=figure.figaspect(1))
        plt.figure(figsize=(10, 10))
        plt.scatter(modes[:, 0], modes[:, 1], c='blue')
        plt.scatter(estimated_x_mode_on_map[0], estimated_x_mode_on_map[1], c='red', marker='x', s=100)
        plt.ylim(-1.1, 1.1)
        plt.xlim(-1.1, 1.1)
        plt.xlabel('z1 (mode)')
        plt.ylabel('z2 (mode)')
        figurename3 = 'estimated x-mode on map.png'
        figurepath3 = os.path.join(saveDirName, figurename3)
        plt.savefig(figurepath3)
        plt.show()
        messagebox.showinfo("Finished", "Please check output directory.")
