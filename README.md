# AnExergyAnalysis

This reposotiry makes an exeergetic analysis for a experiment carried out in 2019 on which rainwater and snow samples were collected from a roof and garden at Thompson
Rivers University. 

The expoerimnent was composed by 5 samples (each with 3 replicas):
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
- $h$ is the entalpia at the end
- $h_0$ is the entalpia at the begin
- $T_0$ is the initial temeperature
- $s$ is the entropy at the end
- $s_0$ is the entropy at the begin

The humidity ratio and the saturation pressure of the water were also take in account. Also 
