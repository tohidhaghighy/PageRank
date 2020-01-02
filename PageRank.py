import numpy as np
import pandas as pd
from scipy import sparse

class PageRank:
    def __init__(self,alpha,beta):
        self.alpha=alpha
        self.beta=beta

    #ورودی را کابر میگیرد
    def input_array(self):
        row = int(input("Enter the Number of rows:"))
        column = int(input("Enter the Number of columns:"))
        data = []
        for c in range(column):
            row_list = []
            for r in range(row):
                row_list.append(float(input("Enter value for i={}&j{} = ".format(c, r))))
            data.append(row_list)
        data_array = np.array(data)
        return data_array

    # ترانهاده ماتریس را تولید میکند
    def Transpose_Matrix(self,matrix):
        return matrix.T

    #تبدیل ماتریس مجاورت به ماتریس مارکوف که جمع ستون ها 1 شود
    def ConvertMatrix_To_Markov(self,matrix):
        M = np.zeros(matrix.shape)
        for c in range(matrix.shape[1]):
            s = matrix[:, c].sum()
            if(s!=0):
                M[:, c] = matrix[:, c]/s
        return M
    
    #فقط نود های غیر صفر را نگه میدارد
    def Spars_Matrix(self,matrix):
        return sparse.csc_matrix(matrix)

    #تابع پیج رنک
    def PageRank_Function(self,M_Matrix,V_Matrix,EN_Matrix):
        # مقادیر اولیه
        finish_num = 1
        beta = self.beta
        alpha = self.alpha
        while(finish_num>alpha):
            print("-----------------------------------------------------")
            print(beta * (M_Matrix * V_Matrix))
            V_Rank = beta * (M_Matrix * V_Matrix) + (1-beta) * EN_Matrix
            print(V_Rank)
            
            #scall mikonam ta har marhalle jam 1 shavad
            rescale = 1 / V_Rank.sum()
            V_Rank = V_Rank * rescale
            #ماتریس جدید را از قبلی کم میکند تا شرط پایان را ایجاد کند
            v_d = abs(V_Rank - V_Matrix)
            finish_num = v_d.sum()
            # ابدیت رنک صفحات
            V_Matrix = V_Rank
        #از حالت ماتریسی در میاورد و به ارایه تبدیل میکند
        df_all=V_Rank
        listall_df=list(map(float, df_all))
        #2 تا صفحه برتر را میدهد
        return listall_df

