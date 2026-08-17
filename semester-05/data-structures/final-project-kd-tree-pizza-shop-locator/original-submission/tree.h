#pragma once
#include "pizza_shop_main.h"
#include "pizza_shop_branch.h"
#include "point.h"
#include "neighbourhood.h"
#include <vector>
#include <cmath>
using namespace std;

class tree
{
	friend class pizza_shop_main;
private:
	vector <pizza_shop_main*> shops;
	vector <pizza_shop_main*> Shops;
	vector <neighbourhood*> neighbourhoods;
	pizza_shop_main* r;

public:
	tree();
	void sort_by_x(vector<pizza_shop_main>&);
	void sort_by_y(vector<pizza_shop_main>&);
	pizza_shop_main* build2DTree(std::vector<pizza_shop_main>&, int);
	pizza_shop_main* nearestNeighbor(pizza_shop_main*, point*, int);
	pizza_shop_main* closest(pizza_shop_main*, pizza_shop_main*, point*);
	void Avail_P();
	void ADD_P();
	void ADD_N();
	void ADD_Br();
	int hash_function(string, int);
	int search_by_name_shop(string);
	void Del_Br();
	int search_by_name_neighbourhood(string);
	void List_P();
	void List_Brs();
	void Near_P();
	void Near_Br();
	void Most_Brs();
	bool is_full(point*, pizza_shop_main*, string);
	bool is_empty();

	~tree();
};

