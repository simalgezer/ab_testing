#First look at the data
import pandas as pd
from scipy.stats import ttest_1samp, shapiro, levene, ttest_ind, mannwhitneyu, pearsonr, spearmanr, kendalltau, \
    f_oneway, kruskal
import numpy as np
from statsmodels.stats import proportion as pr
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import statsmodels.stats.api as sms
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', 10)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

max_bid = pd.read_excel("/Users/simalgezer/Desktop/ab_testing.xlsx", sheet_name='Control Group', engine='openpyxl')
avg_bid = pd.read_excel("/Users/simalgezer/Desktop/ab_testing.xlsx", sheet_name='Test Group', engine='openpyxl')

def check_data(dataframe, head=5):
    print ("####### SHAPE #######")
    print (dataframe.shape)
    print ("####### INFO #######")
    print (dataframe.info ())
    print ("####### DESCRIBE #######")
    print (dataframe.describe ([0.01, 0.1, 0.25, 0.50, 0.75, 0.9, 0.95, 0.99]))
    print ("####### NA VALUES #######")
    print (dataframe.isnull ().sum ())
    print ("####### FIRST {} ROWS #######".format (head))
    print (dataframe.head (head))

check_data(max_bid)

sns.distplot(max_bid["Purchase"], hist=False)      
plt.show()

#Applying Shapiro Test to statistically test normal distribution
test_stat, pvalue = shapiro(max_bid["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
#Test Stat = 0.9773, p-value = 0.5891
#H0 cannot be rejected, the sample is normally distributed. p-value > 0.05

test_stat, pvalue = shapiro(avg_bid["Purchase"])
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
#Test Stat = 0.9589, p-value = 0.1541

#Applying Levene Test to statistically test variance homogeneity
test_stat, pvalue = levene(max_bid["Purchase"], avg_bid["Purchase"])
print("Test Stat = %.4f, p-value = %.4f" % (test_stat, pvalue))
#Test Stat = 2.6393, p-value = 0.1083
#H0 cannot be rejected, variances between control and test groups show homogeneity. p-value > 0.05

#H0 cannot be rejected, the sample is normally distributed. p-value > 0.05

#Applying two-independent sample t-test (parametric test)
test_stat, pvalue = ttest_ind(max_bid["Purchase"], avg_bid["Purchase"], equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))
#Test Stat = -0.9416, p-value = 0.3493
#H0 cannot be rejected. p-value > 0.05. 
#There is no statistically significant difference between the mean of the purchase variable of the two groups.

#Applying two-proportion z-test (AB-Testing)
max_bid["Purchase"].shape[0]     # Sample size is 40, n1>30 precondition is met.
avg_bid["Purchase"].shape[0]        # Sampe size is 40, n2>30 precondition is met.

max_bid["Purchase"].sum()
# 22035.762350809266
max_bid["Impression"].sum()
#4068457.962707891

avg_bid["Purchase"].sum()
#23284.243865938704
avg_bid["Impression"].sum()
#4820496.47030138

from statsmodels.stats.proportion import proportions_ztest
conversion_number = np.array([max_bid["Purchase"].sum(), avg_bid["Purchase"].sum()])
impression_number = np.array([max_bid["Impression"].sum(), avg_bid["Impression"].sum()])

ttest_z, p_value_z = proportions_ztest(conversion_number, impression_number)
print("t-test statistics: {}\np_value: {:.10f}".format(ttest_z, p_value_z))
#t-test statistics: 12.221173465876399
#p_value: 0.0000000000
#H0 hypothesis is rejected because p_value is less than 0.05. 
#There is a significant difference between the conversion rates of the two groups.

max_bid["Purchase"].sum()/max_bid["Impression"].sum()
#0.00541624432470298

avg_bid["Purchase"].sum()/avg_bid["Impression"].sum()
#0.004830258461839089
#Purchase (conversion) per impression of maximum bidding is better than of average bidding.
#This difference in conversion rates is in favor of the control group(maximum_bidding), as observed in z-test.


