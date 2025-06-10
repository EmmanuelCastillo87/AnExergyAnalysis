# An Exergy Analysis

This reposotiry makes an exeergetic analysis for a experiment carried out in December of 2019 on which rainwater and snow samples were collected from a roof and garden at Thompson
Rivers University. 

The experimnent was composed by 5 samples (each with 3 replicas):
|  N°  |  Iradiation  |  Medium  |  Bioindicator  |
|  --  |  ----------  |  ------  |  ------------  |
|  1  |  150We  |  Distilled water  |  Plasmid  |
|  2  |  150We & UVC  |  Distilled water  |  Plasmid  |
|  3  |  150We  |  Distilled water  |  Ecoli  |
|  4  |  150We  |  Snow  |  Ecoli  |
|  5  |  150We  |  Rain water  |  Ecoli  |

The samples were exposed to artificial ligth irradiation in CPC´s to test the disinfection effects of the simulated sunlight. The following equation was used to get the exergy of each sample: 

$A = (h - h_0) - T_0 * (s - s_0)$

Where:
- $A$ is the exergy
- $h$ is the enthlpy at the end
- $h_0$ is the enthlpy at the begin
- $T_0$ is the initial temeperature
- $s$ is the entropy at the end
- $s_0$ is the entropy at the begin

Enthalpy and entropy was obtained from the iapws library (Python implementation of standards from The InternationalAssociation for the Properties of Water and Steam).
The humidity ratio and the saturation pressure of the water were also take in account.
And some constants (approximations) were condidered too (air resistance, air specific heat capacity and atmospheric pressure).

Results (pandas DataFrame tables) are write into two simple text files. One deals with each replica and the other give us a probabilistic view of each sample.

###  First file contents:
|  Sample  |  T_init  |  P_init  |  T_stag  |  P_stag  |  Water_mass  |  Air_mass  |  Ex_water  |  Ex_air  |  Total_exergy  |  Experiment  |
|  ------  |  ------  |  ------  |  ------  |  ------  |  ----------  |  --------  |  --------  |  ------  |  ------------  |  ----------  |
|  DistWaterPlasmid150W1  |  323.19  |  99421.95  |  364.96  |  99461.75  |  0.01   |  0.04   |  104.32  |  101.46  |  205.79  |  0  |
|  DistWaterPlasmid150W2  |  322.88  |  99422.82  |  354.73  |  99447.80  |  0.01   |  0.04   |  61.77  |  60.21  |  121.99  |  0  |
|  DistWaterPlasmid150W3  |  323.62  |  99420.43  |  354.19  |  99450.36  |  0.01   |  0.04   |  56.92  |  55.74  |  112.67  |  0  |
|  DistWaterPlasmid150W_UVC1  |  323.91  |  99422.66  |  349.21  |  99444.01  |  0.01   |  0.04   |  39.33  |  38.56  |  77.89  |  1  |
|  DistWaterPlasmid150W_UVC2  |  325.33  |  99422.13  |  347.03  |  99435.06  |  0.01   |  0.04   |  29.01  |  28.34  |  57.36  |  1  |
|  DistWaterPlasmid150W_UVC3  |  323.64  |  99422.08  |  340.02  |  99448.29  |  0.01   |  0.04   |  16.77  |  17.10  |  33.87  |  1  |
|  DistWaterEcoli150W1  |  324.19  |  99418.64  |  350.71  |  99437.05  |  0.02   |  0.02   |  107.72  |  26.28  |  134.00  |  2  |
|  DistWaterEcoli150W2  |  324.42  |  99421.98  |  356.14  |  99451.38  |  0.02   |  0.02   |  152.57  |  37.28  |  189.85  |  2  |
|  DistWaterEcoli150W3  |  324.05  |  99422.05  |  354.78  |  99449.37  |  0.02   |  0.02   |  143.59  |  35.08  |  178.68  |  2  |
|  SnowEcoli150W1  |  324.32  |  99421.51  |  360.68  |  99467.81  |  0.02   |  0.02   |  198.89  |  48.76  |  247.65  |  3  |
|  SnowEcoli150W2  |  324.52  |  99420.02  |  355.11  |  99453.48  |  0.02   |  0.02   |  142.14  |  34.88  |  177.02  |  3  |
|  SnowEcoli150W3  |  324.37  |  99422.41  |  356.18  |  99443.26  |  0.02   |  0.02   |  153.43  |  37.28  |  190.72  |  3  |
|  RainwaterEcoli150W1  |  332.71  |  99422.14  |  362.86  |  99467.98  |  0.02   |  0.02   |  135.18  |  33.48  |  168.66  |  4  |
|  RainwaterEcoli150W2  |  322.97  |  99419.41  |  358.80  |  99463.42  |  0.02   |  0.02   |  194.02  |  47.55  |  241.57  |  4  |
|  RainwaterEcoli150W3  |  323.10  |  99420.76  |  352.74  |  99441.18  |  0.02   |  0.02   |  134.20  |  32.67  |  166.88  |  4  |

### Second file contents:
|  Experiment  |  T_mean  |  Ex_mean  |  2StdErr_T  |  2StdErr_Ex  |
|  ----------  |  ------  |  -------  |  ---------  |  ----------  |
|  DistWaterPlasmid  |  357.96  |  146.81  |  7.00  |  59.21  |
|  DistWaterPlasmid_UVC  |  345.42  |  56.37  |  5.54  |  25.43  |
|  DistWaterEcoli  |  353.87  |  167.51  |  3.26  |  34.12  |
|  SnowEcoli  |  357.32  |  205.13  |  3.41  |  43.24  |
|  RainwaterEcoli  |  358.13  |  192.37  |  5.88  |  49.21  |

### Error bars plot of temperature and exergy
(Add description and plot here)

## Python and modules
To perform this analysis the following Python and modules versions were used:
- Python: 3.1.05
- numpy: 1.26.4
- pandas: 2.2.2
- iapws: 1.5.4
- matplotlib: 3.5.2

## Learn more
If you want to know more about the experiemnt, the article is available in: (add link here when we have one)
