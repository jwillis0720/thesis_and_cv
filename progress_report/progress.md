#Progress Report

##Development of the RosettaHTS docking algorithm

Optimization of the RosettaHTS docking algorithm has continued, with the current version capable of frequently obtaining a < 2.0 Å pose within 25 models during a self docking study (figure).  The current protocol initially uses coarse grained docking with a grid based scoringencoding shape complimentarity and hydrogen bonding information.  Based on the initial prediction, fine grained docking using the Rosetta energy function is performed.  During fine grained docking, the backbone, side chains, and ligand are flexible. The current docking protocol can process a single ligand in 15-30 minutes, depending on the size of the protein.

###The Rosetta energy function has a limited ability to perform rank order prediction.

The current implementation of the Rosetta energy function is limited in its ability to accurately predict binding affinity.  While correct poses of a single ligand can frequently be distinguished using binding energy (citation), comparison of the energies of different ligands is generally poor (citation).  A search of the literature indicates that this problem is not specific to Rosetta, but rather a general limitation of current ligand docking technology. 

##Integration of Chemical information with RosettaHTS



##Publication schedule

##Future directions