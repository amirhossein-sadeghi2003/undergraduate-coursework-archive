#include "pizza_shop_main.h"



pizza_shop_main::pizza_shop_main()
{
	is_main_shop = true;
}

pizza_shop_main::pizza_shop_main(string name, point address)
{
	this->name = name;
	this->address = address;
	is_main_shop = true;
}

string pizza_shop_main::get_name()
{
	return name;
}
point pizza_shop_main::get_address()
{
	return address;
}

void pizza_shop_main::print() {
	cout << "Hello." << endl;
}
pizza_shop_main::~pizza_shop_main()
{
}
