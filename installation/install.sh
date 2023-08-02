#!/bin/bash

INSTALL_DIR="$(pwd)"
INSTALL_PATH="$HOME/bin/BioInfoSwissKnife"


echo "Creating installation directory..."
mkdir -p "$INSTALL_PATH"

echo "Installing scripts..."

# Copying profile file
cp -f bash-profile-file.txt ~/.bioinfoswisskniferc.sh

# Append to bashrc if necessary.
if ! grep -q ".bioinfoswisskniferc.sh" ~/.bashrc; then
	echo "" >> ~/.bashrc
	echo "source ~/.bioinfoswisskniferc.sh" >> ~/.bashrc
	echo "" >> ~/.bashrc
fi

# Refresh ~/.bashrc
source ~/.bashrc

# Syncing scripts to installation file
rsync -ah --delete ./ $INSTALL_PATH/

# make everything in bin file executable
chmod +x $INSTALL_PATH/bin/*

echo
echo "Installation complete."
echo

