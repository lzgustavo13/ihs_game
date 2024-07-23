#include <linux/module.h>
#define INCLUDE_VERMAGIC
#include <linux/build-salt.h>
#include <linux/elfnote-lto.h>
#include <linux/export-internal.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;
BUILD_LTO_INFO;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__section(".gnu.linkonce.this_module") = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif


static const struct modversion_info ____versions[]
__used __section("__versions") = {
	{ 0xbdfb6dbb, "__fentry__" },
	{ 0x92997ed8, "_printk" },
	{ 0x5b8239ca, "__x86_return_thunk" },
	{ 0xa78af5f3, "ioread32" },
	{ 0x88db9f48, "__check_object_size" },
	{ 0x6b10bee1, "_copy_to_user" },
	{ 0x6f67c9df, "pci_iounmap" },
	{ 0xad450e05, "pci_disable_device" },
	{ 0x3aef15d8, "pci_release_region" },
	{ 0xa5dcc49f, "pci_enable_device" },
	{ 0x75e44d76, "pci_read_config_word" },
	{ 0xb00d87a8, "pci_read_config_byte" },
	{ 0xb52dc92b, "pci_read_config_dword" },
	{ 0xe63d04a5, "pci_request_region" },
	{ 0x308eb9c7, "pci_iomap" },
	{ 0xd0da656b, "__stack_chk_fail" },
	{ 0x4441a697, "__pci_register_driver" },
	{ 0xe3ec2f2b, "alloc_chrdev_region" },
	{ 0x3d7e9aa9, "__class_create" },
	{ 0xa463c6ea, "cdev_init" },
	{ 0x4cc716d1, "device_create" },
	{ 0x6ee90a52, "cdev_add" },
	{ 0xcdbb65b3, "device_destroy" },
	{ 0x4e047f6b, "class_destroy" },
	{ 0x6bc3fbc0, "__unregister_chrdev" },
	{ 0xdad20e95, "pci_unregister_driver" },
	{ 0x1ae367ea, "cdev_del" },
	{ 0x13c49cc2, "_copy_from_user" },
	{ 0x4a453f53, "iowrite32" },
	{ 0xc4ae50da, "module_layout" },
};

MODULE_INFO(depends, "");

MODULE_ALIAS("pci:v00001172d00000004sv*sd*bc*sc*i*");
