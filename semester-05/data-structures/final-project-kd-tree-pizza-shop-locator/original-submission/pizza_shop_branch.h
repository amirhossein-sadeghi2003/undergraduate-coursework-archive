#pragma once
#include "point.h"
#include "pizza_shop_main.h"
#include <string.h>
#include <iostream>
using namespace std;
class pizza_shop_branch :public pizza_shop_main
{
	friend class pizza_shop_main;
	friend class tree;
private:
	string name_main_shop;

public:
	pizza_shop_branch();
	pizza_shop_branch(string, point, string);
	string get_name_main_shop();
	void print() override;
	~pizza_shop_branch();
};

