KERNEL_DIR := /lib/modules/$(shell uname -r)/build
PWD_DIR := $(PWD)
TARGET := speaker

obj-m += $(TARGET).o


all:
	@make -C $(KERNEL_DIR) M=$(PWD_DIR) modules


clean:
	@make -C $(KERNEL_DIR) M=$(PWD_DIR) clean
