#include "pizza_shop_branch.h"



pizza_shop_branch::pizza_shop_branch()
{
	is_main_shop = false;
}

pizza_shop_branch::pizza_shop_branch(string name, point address, string name_main_shop)
{
	this->name = name;
	this->address = address;
	this->name_main_shop = name_main_shop;
	is_main_shop = false;
}

string pizza_shop_branch::get_name_main_shop()
{
	return name_main_shop;
}

void pizza_shop_branch::print() {
	cout << "Salam" << endl;
}
pizza_shop_branch::~pizza_shop_branch()
{
}
