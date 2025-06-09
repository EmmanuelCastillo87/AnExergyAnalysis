import numpy as np
import pandas as pd
from iapws import IAPWS97
import matplotlib.pyplot as plt

# Function to calculate saturation pressure of water vapor at temperature T (K)
def saturation_pressure_water(T):
    # Using IAPWS97 saturation pressure function
    sat = IAPWS97(T=T, x=0)  # x=0 for saturated liquid, just to get Psat
    return sat.P * 1e6  # Convert MPa to Pa

# Function to calculate humidity ratio (mass of water vapor per mass of dry air)
def humidity_ratio(P_v, P_total):
    # P_v = partial pressure of water vapor
    return 0.622 * P_v / (P_total - P_v)

# Function to calculate exergy per unit mass of water or air
def exergy(h, s, h0, s0, T0):
    # Exergy per unit mass = (h - h0) - T0*(s - s0)
    return (h - h0) - T0 * (s - s0)

# CONSTANTS (approximate)
R_air = 287.05  # J/kg-K
cp_air = 1005   # J/kg-K
P_atm = 99325   # Pa

# Data
df = pd.DataFrame({
    'Measure': ['DistWaterPlasmid150W1', 'DistWaterPlasmid150W2', 'DistWaterPlasmid150W3', 'DistWaterPlasmid150W_UVC1', 
                'DistWaterPlasmid150W_UVC2', 'DistWaterPlasmid150W_UVC3', 'DistWaterEcoli150W1', 'DistWaterEcoli150W2', 
                'DistWaterEcoli150W3', 'SnowEcoli150W1', 'SnowEcoli150W2', 'SnowEcoli150W3', 'RainwaterEcoli150W1', 
                'RainwaterEcoli150W2', 'RainwaterEcoli150W3'],
    'T_init': [25.04, 24.73, 25.47, 25.76, 27.18, 25.49, 26.04, 26.27, 25.9, 26.17, 26.37, 26.22, 34.56, 24.82, 24.95],
    'P_init': [96.95, 97.82, 95.43, 97.66, 97.13, 97.08, 93.64, 96.98, 97.05, 96.51, 95.02, 97.41, 97.14, 94.41, 95.76],
    'T_stag': [66.81, 56.58, 56.04, 51.06, 48.88, 41.87, 52.56, 57.99, 56.63, 62.53, 56.96, 58.03, 64.71, 60.65, 54.59],
    'P_stag': [136.75, 122.8, 125.36, 119.01, 110.06, 123.29, 112.05, 126.38, 124.37, 142.81, 128.48, 118.26, 142.98, 138.42, 116.18],
    'Water_mass': [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025],
    'Air_mass': [0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025, 0.025]
})

# Preprocess data
df['T_init'] = df['T_init'] + 298.15      # Convert °C to °K
df['T_stag'] = df['T_stag'] + 298.15      # Convert °C to °K
df['P_init'] = df['P_init'] + P_atm       # Take in account the atmospheric pressure at Earth's surface
df['P_stag'] = df['P_stag'] + P_atm       # Take in account the atmospheric pressure at Earth's surface

# Create empty lists to store operation results
ex_water = []
ex_air = []
total_exergy = []

# Calculate exergy for each row in the dataframe
for index, row in df.iterrows():
    T0 = row['T_init']
    P0 = row['P_init']
    T_stag = row['T_stag']
    P_stag = row['P_stag']

    # Reference state properties of water at T0 and P0
    water_ref = IAPWS97(T=T0, P=P0 / 1e6)  # P in MPa
    h0_water = water_ref.h * 1000  # kJ/kg to J/kg
    s0_water = water_ref.s * 1000  # kJ/kg-K to J/kg-K

    # Reference state properties of dry air at T0 and P0
    s0_air = cp_air * np.log(T0 / T0) - R_air * np.log(P0 / P0)  # zero by definition

    # Calculate water properties at final temperature and pressure
    water_final = IAPWS97(T=T_stag, P=P_stag / 1e6)
    h_water = water_final.h * 1000  # J/kg
    s_water = water_final.s * 1000  # J/kg-K

    # Calculate saturation pressure and humidity ratio at final temperature
    P_sat = saturation_pressure_water(T_stag)
    # Assume total pressure = P_stag, partial pressure of water vapor = saturation pressure at T_stag
    w_final = humidity_ratio(P_sat, P_stag)

    # Air properties at final temperature and pressure (ideal gas assumptions)
    h_air0 = cp_air * T0
    s_air0 = cp_air * np.log(T0 / T0) - R_air * np.log(P0 / P0)  # zero
    h_air = cp_air * T_stag
    s_air = cp_air * np.log(T_stag / T0) - R_air * np.log(P_stag / P0)

    # Calculate exergies per unit mass
    ex_water.append(exergy(h_water, s_water, h0_water, s0_water, T0) * row['Water_mass'])
    ex_air.append(exergy(h_air, s_air, h_air0, s_air0, T0) * row['Air_mass'])

    # Total exergy in the closed tube
    total_exergy.append(ex_water[index] + ex_air[index])

# Add calculations (made inside the loop avobe) to the dataframe
df['Ex_water'] = ex_water
df['Ex_air'] = ex_air
df['Total_exergy'] = total_exergy

# Create a new dataframe to make the exergetic analysis
df1 = pd.DataFrame()
df['Experiment'] = df.index // 3
df1['Experiment'] = ['DistWaterPlasmid', 'DistWaterPlasmid_UVC', 'DistWaterEcoli', 'SnowEcoli', 'RainwaterEcoli']
df1['T_mean'] = df.groupby('Experiment')['T_stag'].mean()
df1['Ex_mean'] = df.groupby('Experiment')['Total_exergy'].mean()
df1['2StdErr_T'] = (df.groupby('Experiment')['T_stag'].std() / 3 ** 0.5) * 2
df1['2StdErr_Ex'] = (df.groupby('Experiment')['Total_exergy'].std() / 3 ** 0.5) * 2

# Graph a errorbar
y = df1['T_mean']
x = df1['Ex_mean']
yerr = df1['2StdErr_T']
xerr = df1['2StdErr_Ex']
plt.errorbar(x, y, xerr=xerr, yerr=yerr, fmt='o', capsize=5, ecolor='red') #, label='Data with error')
plt.ylabel('Temperature (K)')
plt.xlabel('Exergy (J)')
plt.legend()
plt.grid(True)
for index, row in df1.iterrows():
    if index == 3:
        plt.text(row['Ex_mean'] + 2, row['T_mean'] - 1, row['Experiment'], fontsize=10, ha='left', va='top')
    elif index == 0:
        plt.text(row['Ex_mean'] - 2, row['T_mean'] + 1, row['Experiment'], fontsize=10, ha='right', va='top')
    else:
        plt.text(row['Ex_mean'] + 2, row['T_mean'] + 1, row['Experiment'], fontsize=10, ha='left', va='top')

plt.show()

# Save the results
with open('output1.txt', 'w') as f:
    f.write(df.to_string(index=False))

with open('output2.txt', 'w') as f:
    f.write(df1.to_string(index=False))