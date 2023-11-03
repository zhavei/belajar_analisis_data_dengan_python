#mean
import numpy as np
##import scipy.constants as stats
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt
import sqlalchemy as sqla


#contoh mean / rata-rata
# Data
nilai_ujian = [80, 75, 65, 90, 100]
# Hitung mean
mean = np.mean(nilai_ujian)
# Print mean
print("Mean:", mean)

jumlah_kucing = np.array([3, 2, 1, 1, 2, 3, 2, 1, 0, 2])

print("nilai mean", jumlah_kucing.mean())
print("nilai median", np.median(jumlah_kucing))

mode_jumlah_kucing = stats.mode(jumlah_kucing)[0]
print("mode -> nilai yang paling sering muncul :", mode_jumlah_kucing)

##Measuring Dispersion

#Range
range = jumlah_kucing.max() - jumlah_kucing.min()
print("nilai range untuk melihat perbedaan antara\nnilai maksimum dan minimum :", range)

#Interquartile Range
iqr = np.percentile(jumlah_kucing, 75) - np.percentile(jumlah_kucing, 25)
print("Interquartile Range :", iqr)

#variance
jumlah_kucing_series = pd.Series(jumlah_kucing)
print("variance" , jumlah_kucing_series.var())

#Standard Deviation
print("standart deviation: " , jumlah_kucing_series.std())

##Measuring Asymmetric
plt.hist(jumlah_kucing, bins=4)
plt.show()

#Skewness
print("distribusi nilai skewness kanan atau kiri", jumlah_kucing_series.skew())

##Data Relationship
sample_data = {
    "name":["bebek", "alia", "ayam", "kocheng", "buwung"],
    'age': [24, 22, 23, 25, 28],  
    'communication_skill_score': [85, 70, 75, 90, 90],
    'quantitative_skill_score': [80, 90, 80, 75, 70]
}

#Correlation
df = pd.DataFrame(sample_data)
df_corr = df.corr(numeric_only=True)
print(df_corr)

#Covariance
df.cov(numeric_only=True)

##dara wrangling
#csv_data = pd.read_csv("sales1.csv", delimiter=",")
#df_read_excel = pd.read_excel("data.xlsx", sheet_name="Sheet1")
#df_read_jso = pd.read_json("data.json")
url = "https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list"
df_read_html = pd.read_html(url)[0]
print(df_read_html)

db = sqla.create_engine("sqlite:///mydata.sqlite")
pd.read_sql_table("table_name", db)
pd.read_sql_query("SELECT * FROM table_name", db)

product_df = pd.read_csv("product.csv")
orders_df = pd.read_csv("orders.csv")
 
new_order_df = pd.merge(
    left=product_df,
    right=orders_df,
    how="inner",
    left_on="product_id",
    right_on="product_id"
)
