#importing necessary library to be used to plot graph of seasonal variation for LSA for data of 2009
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import winsound

#creating a dataframe that will be storing the data's read from an Excel sheet

#DAV dataframe
try:
    dav_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_DAV_Data_2009.xlsx")
    #dav_df.fillna(0, inplace=True)
    print("DAV excel opened successfully")
except Exception as e:
    print(f"Error: {e}")

#MUT dataframe
#try:
#    mut_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_MUT_Data_2009.xlsx")
#    mut_df.fillna(0, inplace=True)
#    print("MUT excel opened successfully")
#except Exception as e:
#    print(f"Error: {e}")

#YAP dataframe
try:
    yap_df = pd.read_excel(r"C:\Users\P C\PycharmProjects\GraphAutomationSchoolProject\data\Al Nawaf\Monthly_IQD_YAP_Data_2009.xlsx")
    #yap_df.fillna(0, inplace=True)
    print("YAP excel opened successfully")
except Exception as e:
    print(f"Error: {e}")

#print()

#creating an array that group the seasonal month
seasonal = {
    "march_equinox": np.array(["Feb", "Mar", "Apr"]),
    "jun_solstice": np.array(["May", "Jun", "Jul"]),
    "sep_equinox": np.array(["Aug", "Sep", "Oct"]),
    "dec_solstice": np.array(["Nov", "Dec", "Jan"])
}
seasonal_keys = []
for item in seasonal.keys():
    seasonal_keys.append(item)

#DAV calculation
#spliting DAV dataframe and collecting each column by storing it in a dict
dav_dict = {}
for key, value in dav_df.items():
    dav_dict[key] = np.array(value.tolist())

#print(dav_dict)

#creating an array that stores the average of DAV seasonal variation
#dict data of the average
dav_seasonal_avg = {
    "dav_avg_mar_equinox": [],
    "dav_avg_jun_solstice": [],
    "dav_avg_sep_equinox": [],
    "dav_avg_dec_solstice": []
}
seasonal_avg_keys = ["dav_avg_mar_equinox", "dav_avg_jun_solstice", "dav_avg_sep_equinox", "dav_avg_dec_solstice"]

#print(gen_avg)

#for loop to generate the data's of the average seasonal variation
i = 0
for gen_np in seasonal.keys():
    total_value = dav_dict[seasonal[gen_np][0]] + dav_dict[seasonal[gen_np][1]] + dav_dict[seasonal[gen_np][2]]
    avg = total_value/3
    for num in avg.tolist():
        dav_seasonal_avg[seasonal_avg_keys[i]].append(num)
    i += 1

#print(seasonal_avg)

#numpy data of the average which is the final data to plot
dav_fin_cal = {
    "dav_fin_mar_equinox": np.array(dav_seasonal_avg["dav_avg_mar_equinox"]),
    "dav_fin_jun_solstice": np.array(dav_seasonal_avg["dav_avg_jun_solstice"]),
    "dav_fin_sep_equinox": np.array(dav_seasonal_avg["dav_avg_sep_equinox"]),
    "dav_fin_dec_solstice": np.array(dav_seasonal_avg["dav_avg_dec_solstice"])
}
dav_fin_cal_keys = []
for keys in dav_fin_cal.keys():
    dav_fin_cal_keys.append(keys)

print(dav_fin_cal, "\n")
#print(dav_fin_cal_keys, "\n")

"""

#MUT calculation
#spliting DAV dataframe and collecting each column by storing it in a dict
mut_dict = {}
for key, value in mut_df.items():
    mut_dict[key] = np.array(value.tolist())

#print(dav_dict)

#creating an array that stores the average of MUT seasonal variation
#dict data of the average
mut_seasonal_avg = {
    "mut_avg_mar_equinox": [],
    "mut_avg_jun_solstice": [],
    "mut_avg_sep_equinox": [],
    "mut_avg_dec_solstice": []
}
mut_seasonal_avg_keys = ["mut_avg_mar_equinox", "mut_avg_jun_solstice", "mut_avg_sep_equinox", "mut_avg_dec_solstice"]

#print(gen_avg)

#for loop to generate the data's of the average seasonal variation
i = 0
for gen_np in seasonal.keys():
    total_value = mut_dict[seasonal[gen_np][0]] + mut_dict[seasonal[gen_np][1]] + mut_dict[seasonal[gen_np][2]]
    avg = total_value/3
    for num in avg.tolist():
        mut_seasonal_avg[mut_seasonal_avg_keys[i]].append(num)
    i += 1

#print(mut_seasonal_avg)

#numpy data of the average
mut_fin_cal = {
    "mut_fin_mar_equinox": np.array(mut_seasonal_avg["mut_avg_mar_equinox"]),
    "mut_fin_jun_solstice": np.array(mut_seasonal_avg["mut_avg_jun_solstice"]),
    "mut_fin_sep_equinox": np.array(mut_seasonal_avg["mut_avg_sep_equinox"]),
    "mut_fin_dec_solstice": np.array(mut_seasonal_avg["mut_avg_dec_solstice"])
}
mut_fin_cal_keys = []
for keys in mut_fin_cal.keys():
    mut_fin_cal_keys.append(keys)

#print(mut_fin_cal, "\n")
#print(mut_fin_cal_keys, "\n")

"""

#YAP calculation
#spliting YAP dataframe and collecting each column by storing it in a dict
yap_dict = {}
for key, value in yap_df.items():
    yap_dict[key] = np.array(value.tolist())

#print(dav_dict)

#creating an array that stores the average of YAP seasonal variation
#dict data of the average
yap_seasonal_avg = {
    "yap_avg_mar_equinox": [],
    "yap_avg_jun_solstice": [],
    "yap_avg_sep_equinox": [],
    "yap_avg_dec_solstice": []
}
yap_seasonal_avg_keys = ["yap_avg_mar_equinox", "yap_avg_jun_solstice", "yap_avg_sep_equinox", "yap_avg_dec_solstice"]

#print(gen_avg)

#for loop to generate the data's of the average seasonal variation
i = 0
for gen_np in seasonal.keys():
    total_value = yap_dict[seasonal[gen_np][0]] + yap_dict[seasonal[gen_np][1]] + yap_dict[seasonal[gen_np][2]]
    avg = total_value/3
    for num in avg.tolist():
        yap_seasonal_avg[yap_seasonal_avg_keys[i]].append(num)
    i += 1

#print(yap_seasonal_avg)

if i != 0:
    i = 0

#print(i)

#numpy data of the average which is the final data to plot
yap_fin_cal = {
    "yap_fin_mar_equinox": np.array(yap_seasonal_avg["yap_avg_mar_equinox"]),
    "yap_fin_jun_solstice": np.array(yap_seasonal_avg["yap_avg_jun_solstice"]),
    "yap_fin_sep_equinox": np.array(yap_seasonal_avg["yap_avg_sep_equinox"]),
    "yap_fin_dec_solstice": np.array(yap_seasonal_avg["yap_avg_dec_solstice"])
}
yap_fin_cal_keys = []
for keys in yap_fin_cal.keys():
    yap_fin_cal_keys.append(keys)

print(yap_fin_cal)
#print(yap_fin_cal_keys, "\n")

#plotting the graph of each seasonal variation
#generating the hourly time from 0hr - 23hrs
time_hr = np.array(list(range(24)))

#creating x ticks and y ticks for the graph
x_label = []
for num in time_hr:
    if num % 2 == 0:
        x_label.append(num)
nx_label = np.array(x_label)

y_label = list(range(-20, 170, 20))
ny_label = np.array(y_label)

#print(time_hr)

#foor loop to plot all the seasonal variation
for keys in seasonal.keys():
    plt.plot(time_hr, dav_fin_cal[dav_fin_cal_keys[i]], label='DAV', c='royalblue', marker='o', mfc='white',
             mec='royalblue',ms=9, lw=3, ls='-')
#    plt.plot(time_hr, mut_fin_cal[mut_fin_cal_keys[i]], label='MUT', c='crimson', marker='s', mfc='white',
#             mec='crimson', ms=7,lw=2, ls='--')
    plt.plot(time_hr, yap_fin_cal[yap_fin_cal_keys[i]], label='YAP', c='crimson', marker='s', mfc='white',
             mec='crimson', ms=9,lw=3, ls='--')
    plt.title(f"Seasonal Variation of {seasonal_keys[i].replace("_", " ").capitalize()} of 2009 Data for LSA", pad=25,
              fontsize=16, fontweight="bold")
    plt.xlabel('Local Time (hrs)', labelpad=25, fontsize=14, fontweight="bold")
    plt.ylabel('Sq(H) (nT)', fontsize=14, fontweight="bold")
    plt.xticks(nx_label, fontsize=12, fontweight="bold")
    plt.yticks(ny_label, fontsize=12, fontweight="bold")
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["font.sans-serif"] = ["Times New Roman"]
    ax = plt.gca()
    ax.spines['left'].set_position(('data', 0))
    ax.spines['bottom'].set_position(('data', 0))
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    plt.legend(bbox_to_anchor=(0.5, 1.10), loc="upper center", ncol=6, fontsize=12, labelspacing=0.4, frameon=False)
    plt.tight_layout()
    plt.show()
    i += 1
else:
    print("Graph as been saved successfully")

#alarm
winsound.Beep(1000, 1000)