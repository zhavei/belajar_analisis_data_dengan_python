#mean
import numpy as np
##import scipy.constants as stats
from scipy import stats
import pandas as pd
import matplotlib.pyplot as plt

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