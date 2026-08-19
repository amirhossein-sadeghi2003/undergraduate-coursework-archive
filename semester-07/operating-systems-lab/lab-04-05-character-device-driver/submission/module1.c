#include <linux/module.h>
#include <linux/init.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/uaccess.h>
#include <linux/random.h>

#define DEVICE_NAME "module"
#define BUF_LEN 100

static int major;
static char buffer[BUF_LEN];
//static int buf_pos = 0;

static ssize_t my_module_read(struct file *, char *, size_t , loff_t *);
static ssize_t my_module_write(struct file *, const char *, size_t, loff_t *);
static int my_module_open(struct inode *, struct file *);
static int my_module_release(struct inode *, struct file *);



static int my_module_open(struct inode *inode, struct file *file) {
    printk(KERN_INFO "your module(devise) is opened.\n");
    return 0;
}

static int my_module_release(struct inode *inode, struct file *file) {
    printk(KERN_INFO "your module(device) is closed.\n");
    return 0;
}

static ssize_t my_module_read(struct file *file, char *buffer_for_user, size_t len, loff_t *offset) {
    char buff_for_random_bits[20];
    int i;

    for (i = 0; i < len; i++) {
        get_random_bytes(&buff_for_random_bits[i], 1);
    }

    if (copy_to_user(buffer_for_user, buff_for_random_bits, len)) {
        return -EFAULT;
    }

    printk(KERN_INFO "data is sent to user.\n");
    return len;
}

static ssize_t my_module_write(struct file *file, const char *buffer_for_user, size_t len, loff_t *offset) {
    if (copy_from_user(buffer, buffer_for_user, len)) {
        return -EFAULT;
    }

    printk(KERN_INFO "data is written in kernel space(device): %s\n", buffer);
    return len;
}

static struct file_operations fops = {
    .open = my_module_open,
    .release = my_module_release,
    .read = my_module_read,
    .write = my_module_write,
};

 


static int __init my_module_init(void) {
  major = register_chrdev(0, DEVICE_NAME, &fops);
  if (major < 0){
    printk(KERN_ALERT "my_module(device) load failed!\n");
  	return major;
  }
  printk(KERN_INFO "my_module(device)  is loaded: %d\n", major);
  return 0;
}




static void __exit my_module_exit(void) {
    unregister_chrdev(major, DEVICE_NAME);
    printk(KERN_INFO "Exit function...\n");
}


module_init(my_module_init);
module_exit(my_module_exit);

MODULE_LICENSE("GPL");

