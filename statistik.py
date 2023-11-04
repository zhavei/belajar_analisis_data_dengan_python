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
df.duplicated().sum()

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

#Missing value (sum missing value)
product_df.isnull().sum()

#outlier menggunakan IQR method
q25, q75 = np.percentile(data, 25), np.percentile(data, 75)
iqr = q75 - q25
cut_off = iqr * 1.5
minimum, maximum = q25 - cut_off, q75 + cut_off
 
outliers = [x for x in data if x < minimum or x > maximum]

# droping missing value
products_df = pd.read_csv("product.csv")
products_df.dropna(axis=0, inplace=True)

df_ = pd.DataFrame({"name": ['Alfred', 'Batman', 'Catwoman'],
                   "toy": [np.nan, 'Batmobile', 'Bullwhip'],
                   "born": [pd.NaT, pd.Timestamp("1940-04-25"),
                            pd.NaT]})

df_.dropna(axis='columns')

# Interpolation interpolasi 
# interpolasi sering digunakan untuk 
# mengisi nilai yang hilang atau tidak tercatat dalam data

from scipy import interpolate
# Data yang sudah diketahui
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 15, 5, 20, 8])
# Membuat fungsi interpolasi dengan metode linear
f = interpolate.interp1d(x, y, kind='linear')
# Menghitung nilai yang diinterpolasi
x_new = 2.5
y_new = f(x_new)
print(f"Hasil interpolasi pada x = {x_new} adalah y = {y_new}")

data = [
    (1, 20),
    (2, 22),
    (3, 24),
    (4, 26),
    (5, 28),
    (6, 30),
    (7, 32),
    (8, 34),
    (9, 36),
    (10, 38),
    ]
def interpolate_quadratic(data, x):
    """
    Interpolasi kuadrat

    Args:
        data: Data titik
        x: Nilai x yang akan diinterpolasi

    Returns:
        Nilai y yang diinterpolasi
    """

    # Mencari titik data terdekat
    i = np.argmin(np.abs(data[:, 0] - x))

    # Menghitung koefisien polinomial
    a = (data[i + 1, 1] - data[i - 1, 1]) / (data[i + 1, 0] - data[i - 1, 0])
    b = (data[i, 1] - a * data[i, 0])

    # Menghitung nilai y
    y = a * x ** 2 + b * x + data[i, 1]

    return y


# Mendapatkan nilai suhu udara di hari ke-11
y = interpolate_quadratic(data, 11)

print(y)
