# This file is part of the madwifi package from livna/rpmfusion
# You have to consider using ath_pci only if ath5k.ko
# from newer kernel do not work with your hardware.
#
# In this case you have to swich this comment line:
# ( comment also the  madwifi file  in the same directory).
blacklist ath5k
#blacklist ath_pci
