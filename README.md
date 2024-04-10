# Subject-Grounding
*Description: repository containing noise data and pipeline analysis for subject grounding, for the ISMRM Reproducibility Challenge 2024.*
EMI reduction is essential to utilize low-field point-of-care MRI devices in different environments with different noise conditions. Subject grounding has the potential to reduce EMI and stabilize noise levels. Therefore, it is crucial to replicate the study and investigate whether the EMI reduction can be reproduced for a different body part, environment, and noise conditions.


## Leiden experiments
The subject grounding approach was originally tested in the Leiden University Medical Center, in Leiden, the Netherlands. This approach was originally proposed to reduce electromagnetic interference (EMI) by subject grounding through ECG electrodes for neuroimaging. An Halbach-array Point-Of-Care MR scanner operating at 46 mT was used in this experiment. Subject grounding was achieved using a variable number of ECG patches, in different locations, depending on the imaged area. Quantification was performed by acquiring a noise scan for each scenario and fitting a polynomial function to estimate the noise level. The improvement in SNR in the images was also quantified.

## Valencia experiments
The team in Valencia will try to replicate the subject grounding approach for extremity imaging. The Valencia site is equipped with an Halbach-array MR scanner, operating at 70 mT. Their setup is optimized for extremity imaging, which requires different receiver coils than those used for neuroimaging in Leiden. This difference could affect the noise distribution. Additionally, the number and locations of the ECG electrodes may need to be adjusted due to the difference in body parts.
Furthermore, the replicators use a conductive cloth as their reference method to reduce EMI, while the original author's team used arc shields. The replicators team will then compare the performance of subject grounding with and without a conductive cloth. They aim to test the stability of the EMI reduction by recruiting 2/3 volunteers under different conditions, including: with and without subject grounding, with and without the conductive cloth.

In each folder, the data, analysis and results of each site can be found.

