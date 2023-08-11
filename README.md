# capsid-generator
This repository contains the codes and instructions to generate and visualize the capsid models to investigate icosahedral capsids with 3-fold centered hexamers or all skewed/split hexamers.

Description of each element in the repository:
+ `T-number_generator.py`: This Python script generates the sequence of T-number capsids up to a certain maximum T-number specified by the user (`Tmax` parameter). The script generates a `tsv` data file (`T-number_capsids_squences.tsv`).
+ `T_H.py`: Script that contains a function to determine icosahedral capsids that contain a centered hexamer on a global 3-fold axis.
+ `T-number_hexamer_symmetries_identifying_centered_hexamers.tsv`: Data file generated manually by editing `T-number_capsids_squences.tsv` to highlight the 3-fold hexamer-centered capsids screened with `T_H.py`.
+ `generate_shells.cxc`: ChimeraX command script to generate 3D capsid models and snapshots centered on the 3-fold axis. Each capsid that one wants to render must be specified individually. The script was tested using ChimeraX version 1.2.
+ `ChimeraX_rendering_instructions_EMDB_capsid.md`: Markdown file containing the instructions on how to generate the rendering of the SIO-2 procapsid, which was used as an empirical example of 3-fold hexamer centered capsid. Other EM maps can be rendered analogously.
