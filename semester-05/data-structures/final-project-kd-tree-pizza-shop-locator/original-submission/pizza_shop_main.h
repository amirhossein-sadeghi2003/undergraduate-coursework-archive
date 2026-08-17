#pragma once
#include "point.h"
#include <string.h>
#include <iostream>
#include <vector>
//#include "pizza_shop_branch.h"
using namespace std;
class pizza_shop_main
{
	friend class pizza_shop_branch;
	friend class tree;
private:
	point address;
	string name;
	pizza_shop_main* left;
	pizza_shop_main* right;
	pizza_shop_main* parent;
	vector<pizza_shop_branch*> branches;
	bool is_main_shop;

public:
	pizza_shop_main();
	pizza_shop_main(string, point);
	string get_name();
	point get_address();
	virtual void print();
	~pizza_shop_main();
};

