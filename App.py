###############
#### PILOT. #####
###############

import streamlit as st
import pandas as pd
import numpy as np
import io
import re
from datetime import datetime
from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter
import requests


import matplotlib.pyplot as plt
import seaborn as sns


st.set_page_config(page_title="Chiran EDA App", layout="wide")
st.title("Chiran's EDA Web App")

st.markdown("""
Upload your file below to perform EDA. Typically expects Col1=id, Col2=categorical_column, Col3=numerical_column 

""")

file = st.file_uploader("Upload File in Excel", type=["xlsx"], key='file')

# Read into DataFrames

if all([file]):
    # Load the  file
    df = pd.read_excel(file)

    # 2. Initial Data Inspection
    st.write("First 5 rows of the DataFrame:")
    st.dataframe(df.head())

    #print("\nLast 5 rows of the DataFrame:")
    st.dataframe(df.tail())
    
    #print("\nInformation about the DataFrame (data types, non-null counts):")
    st.write(df.info())
    
    #print("\nDescriptive statistics for numerical columns:")
    st.write(df.describe())
    
    # 3. Handle Missing Values
    #print("\nMissing values count per column:")
    #print(df.isnull().sum())
    
    # Example: Fill missing numerical values with the mean
    # df['numerical_column'].fillna(df['numerical_column'].mean(), inplace=True)
    
    # Example: Drop rows with any missing values
    # df.dropna(inplace=True)
    
    # 4. Handle Duplicates
    # print(f"\nNumber of duplicate rows: {df.duplicated().sum()}")
    # df.drop_duplicates(inplace=True)
    
    # 5. Univariate Analysis (Analyzing single variables)
    # Example: Value counts for a categorical column
    st.write("\nValue counts for 'categorical_column':")
    st.write(df['categorical_column'].value_counts())
    
    # Example: Histogram for a numerical column
    fig, ax = plt.subplots() # Create a Matplotlib figure and axes
    plt.figure(figsize=(8, 6))
    sns.histplot(df['numerical_column'], kde=True, ax=ax)
    ax.set_title('Distribution of Numerical Column')
    ax.set_title('Numerical Column')
    ax.set_ylabel('Frequency')
    st.pyplot(fig)


    # 6. Bivariate Analysis (Analyzing relationships between two variables)
    # Example: Scatter plot for two numerical columns
    # plt.figure(figsize=(8, 6))
    # sns.scatterplot(x='numerical_column_1', y='numerical_column_2', data=df)
    # plt.title('Scatter Plot of Two Numerical Columns')
    # plt.xlabel('Numerical Column 1')
    # plt.ylabel('Numerical Column 2')
    # plt.show()
    
    # Example: Box plot for a numerical and categorical column
    fig, ax = plt.subplots() # Create a Matplotlib figure and axes
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='categorical_column', y='numerical_column', data=df)
    ax.set_title('Box Plot of Numerical Column by Categorical Column')
    ax.set_title('Categorical Column')
    ax.set_ylabel('Numerical Column')
    st.pyplot(fig)
    
    # 7. Correlation Analysis (for numerical variables)
    # print("\nCorrelation matrix:")
    # print(df.corr(numeric_only=True))
    
    # plt.figure(figsize=(10, 8))
    # sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
    # plt.title('Correlation Matrix')
    # plt.show()
