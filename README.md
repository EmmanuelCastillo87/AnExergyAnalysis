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

Entalpy and entropy was obtained from the iapws library (Python implementation of standards from The InternationalAssociation for the Properties of Water and Steam).
The humidity ratio and the saturation pressure of the water were also take in account.
And some constants (approximations) were condidered too (air resistance, air specific heat capacity and atmospheric pressure).

Results (pandas DataFrame tables) are write into two simple text files. One deals with each replica and the other give us a probabilistic view of each sample.

####  First file contents:
|  Sample  |  T_init  |  P_init  |  T_stag  |  P_stag  |  Water_mass  |  Air_mass  |  Ex_water  |  Ex_air  |  Total_exergy  |  Experiment  |
|  ------  |  ------  |  ------  |  ------  |  ------  |  ----------  |  --------  |  --------  |  ------  |  ------------  |  ----------  |
|  DistWaterPlasmid150W1  |  323.19  |  99421.95  |  364.96  |  99461.75  |  0.010  |  0.040  |  104.324017  |  101.466817  |  205.790834  |  0  |
|  DistWaterPlasmid150W2  |  322.88  |  99422.82  |  354.73  |  99447.80  |  0.010  |  0.040  |  61.777571  |  60.213348  |  121.990918  |  0  |
|  DistWaterPlasmid150W3  |  323.62  |  99420.43  |  354.19  |  99450.36  |  0.010  |  0.040  |  56.926994  |  55.747229  |  112.674223  |  0  |
|  DistWaterPlasmid150W_UVC1  |  323.91  |  99422.66  |  349.21  |  99444.01  |  0.010  |  0.040  |  39.334773  |  38.564616  |  77.899389  |  1  |
|  DistWaterPlasmid150W_UVC2  |  325.33  |  99422.13  |  347.03  |  99435.06  |  0.010  |  0.040  |  29.013694  |  28.346703  |  57.360397  |  1  |
|  DistWaterPlasmid150W_UVC3  |  323.64  |  99422.08  |  340.02  |  99448.29  |  0.010  |  0.040  |  16.777676  |  17.101102  |  33.878778  |  1  |
|  DistWaterEcoli150W1  |  324.19  |  99418.64  |  350.71  |  99437.05  |  0.025  |  0.025  |  107.724466  |  26.283646  |  134.008112  |  2  |
|  DistWaterEcoli150W2  |  324.42  |  99421.98  |  356.14  |  99451.38  |  0.025  |  0.025  |  152.575672  |  37.282906  |  189.858578  |  2  |
|  DistWaterEcoli150W3  |  324.05  |  99422.05  |  354.78  |  99449.37  |  0.025  |  0.025  |  143.599787  |  35.086615  |  178.686402  |  2  |
|  SnowEcoli150W1  |  324.32  |  99421.51  |  360.68  |  99467.81  |  0.025  |  0.025  |  198.892979  |  48.761029  |  247.654008  |  3  |
|  SnowEcoli150W2  |  324.52  |  99420.02  |  355.11  |  99453.48  |  0.025  |  0.025  |  142.146777  |  34.880726  |  177.027503  |  3  |
|  SnowEcoli150W3  |  324.37  |  99422.41  |  356.18  |  99443.26  |  0.025  |  0.025  |  153.438817  |  37.289658  |  190.728475  |  3  |
|  RainwaterEcoli150W1  |  332.71  |  99422.14  |  362.86  |  99467.98  |  0.025  |  0.025  |  135.183754  |  33.481432  |  168.665186  |  4  |
|  RainwaterEcoli150W2  |  322.97  |  99419.41  |  358.80  |  99463.42  |  0.025  |  0.025  |  194.024736  |  47.550173  |  241.574910  |  4  |
|  RainwaterEcoli150W3  |  323.10  |  99420.76  |  352.74  |  99441.18  |  0.025  |  0.025  |  134.207205  |  32.679315  |  166.886520  |  4  |
