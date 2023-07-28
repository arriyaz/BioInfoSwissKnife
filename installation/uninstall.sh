#!/bin/bash


INSTALL_DIR="$(pwd)"
INSTALL_PATH="$HOME/bin/BioInfoSwissKnife"



echo "Uninstalling scripts..."

# Remove the scripts
rm -rf $INSTALL_PATH/bin/ $INSTALL_PATH/scripts/ \
    $INSTALL_PATH/bash-profile-file.txt $INSTALL_PATH/install.sh


echo "Cleaning .bashrc file..."

# Remove .bioinfoswisskniferc.sh file
rm -f ~/.bioinfoswisskniferc.sh

# Remove the .bioinfoswisskniferc.sh containing line from .bashrc
sed -i '/.bioinfoswisskniferc.sh/d' ~/.bashrc

# Remove trailing empty line from .bashrc
sed -i -e :a -e '/^\n*$/{$d;N;ba' -e '}' ~/.bashrc

# Refresh .bashrc file
source ~/.bashrc


echo
echo "Uninstallation complete."
echo
echo
echo "For complete uninstallation delete ${INSTALL_PATH}"
echo