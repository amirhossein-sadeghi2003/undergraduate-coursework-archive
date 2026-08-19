#!/bin/bash


MODULE_NAME="speaker"
NODE_NAME="speakernode"
USER_APP="user"
USER_SOURCE="user.c"


echo "Building the kernel module..."
if make; then
    echo "Module built successfully."
else
    echo "Module build failed."
    exit 1
fi

echo "Inserting the module..."
if sudo insmod ${MODULE_NAME}.ko; then
    echo "Module inserted successfully."
else
    echo "Failed to insert module."
    exit 1
fi


echo "Creating device node..."
major=$(awk "\$2==\"${MODULE_NAME}\" {print \$1}" /proc/devices)

if [ -z "$major" ]; then
    echo "Error: Major number for ${MODULE_NAME} not found in /proc/devices."
    exit 1
fi

if sudo mknod /dev/${NODE_NAME} c $major 0; then
    echo "Device node /dev/${NODE_NAME} created with major number $major."
else
    echo "Failed to create device node."
    exit 1
fi


if gcc -o ${USER_APP} ${USER_SOURCE}; then
    echo "${USER_APP} compiled successfully."
else
    echo "Failed to compile ${USER_SOURCE}."
    exit 1
fi

echo "Build and installation completed."
