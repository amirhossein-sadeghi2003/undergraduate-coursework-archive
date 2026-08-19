
#!/bin/bash
make
sudo insmod module1.ko

major=$(awk "\$2==\"module\" {print \$1}" /proc/devices)
sudo mknod /dev/module c $major 1
gcc -o user user.c

echo "my_module is created and installed without error."

