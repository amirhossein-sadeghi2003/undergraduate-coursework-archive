#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/fs.h>
#include <linux/uaccess.h>
#include <linux/random.h>
#include <linux/ioctl.h>
#include <linux/slab.h>  

#define DEVICE_NAME "speaker"


MODULE_LICENSE("GPL");


static char buffer[1024];


static int major;
static int volume = 50;  
static bool is_muted = false;

long device_ioctl(struct file *file, unsigned int cmd, unsigned long arg);


static int device_open(struct inode *inode, struct file *file) {
    printk(KERN_INFO "Device is opened.\n");
    return 0;
}

static int device_release(struct inode *inode, struct file *file) {
    printk(KERN_INFO "Device  is closed.\n");
    return 0;
}



static ssize_t device_read(struct file *file, char *user_buffer, size_t len, loff_t *offset) {
    char *temp_buf;
    int i;

    
    temp_buf = kmalloc(len, GFP_KERNEL);
    if (!temp_buf) {
        printk(KERN_ERR "speaker: Some problem happened during allocating memory!\n");
        return -ENOMEM;
    }

    if (is_muted) {
        printk(KERN_INFO "speaker: Microphone is muted.Empty buffer is sent.\n");
        memset(temp_buf, '\0', len);
    } 
    else {
        for (i = 0; i < len; i++) {
            get_random_bytes(&temp_buf[i], 1);
        }
    }

    
    if (copy_to_user(user_buffer, temp_buf, len)) {
        kfree(temp_buf); 
        return -EFAULT;
    }

    printk(KERN_INFO "Random data is readed from speaker.\n");

    kfree(temp_buf); 
    return len;
}


static ssize_t device_write(struct file *file, const char *user_buffer, size_t len, loff_t *offset) {
    if (volume == 0 || is_muted) {
        printk(KERN_INFO "Speaker: There is no output.beacuse it is muted or volume has set to zero.\n");
        return len;
    }
    
    
    if (copy_from_user(buffer, user_buffer, len)) {
        return -EFAULT;
    }
    

    printk(KERN_INFO " your data is written to speaker: %s\n", buffer);
    return len;
}



long device_ioctl(struct file *file, unsigned int cmd, unsigned long arg) {
    int volume_value;
    switch (cmd) {
        case _IO('s', 1):
            is_muted = true;
            printk(KERN_INFO "speaker: microphone  is muted\n");
            break;
        case _IO('s', 2):
            is_muted = false;
            printk(KERN_INFO "speaker: microphone is unmuted\n");
            break;
        case _IOW('s', 3, int):
            if (copy_from_user(&volume_value, (int __user *)arg, sizeof(volume_value))) {
                return -EFAULT;
            }
            if (volume_value >= 0 && volume_value <= 100) {
                volume = volume_value;
                printk(KERN_INFO "speaker: volume is set to %d\n", volume);
            } else {
                printk(KERN_WARNING "speaker: volume should be between 0 and 100!\n");
                return -EINVAL;
            }
            break;
        case _IOR('s', 4, int):
            if (copy_to_user((int __user *)arg, &volume, sizeof(volume))) {
                return -EFAULT;
            }
            printk(KERN_INFO "speaker: amount of volume is : %d\n", volume);
            break;
        default:
            return -ENOTTY;
    }
    return 0;
}






static struct file_operations fops = {
    .open = device_open,
    .release = device_release,
    .read = device_read,
    .write = device_write,
    .unlocked_ioctl = device_ioctl,
};

static int __init speaker_init(void) {
    major = register_chrdev(0, DEVICE_NAME, &fops);
    if (major < 0) {
        printk(KERN_ALERT "Some problem happened during registering device with major number %d\n", major);
        return major;
    }

    printk(KERN_INFO "Major number is %d.\n", major);
    return 0;
}

static void __exit speaker_exit(void) {
    unregister_chrdev(major, DEVICE_NAME);
    printk(KERN_INFO "Unregisterring!\n");
}

module_init(speaker_init);
module_exit(speaker_exit);



