#include "tree.h"
#include <cmath>
#include <iostream>
tree::tree()
{
	for (int i = 0; i < 100; i++) {
		Shops.push_back(NULL);
	}
	for (int i = 0; i < 100; i++) {
		neighbourhoods.push_back(NULL);
	}
}
void tree::sort_by_x(vector<pizza_shop_main>& shops) {
	bool swapped;
	for (size_t i = 0; i < shops.size() - 1; i++) {
		swapped = false;
		for (size_t j = 0; j < shops.size() - i - 1; j++) {
			point addr1 = shops[j].get_address();
			point addr2 = shops[j + 1].get_address();
			if ((addr1.get_x() > addr2.get_x()) || (addr1.get_x() == addr2.get_x() && addr1.get_y() > addr2.get_y())) {
				pizza_shop_main temp = shops[j];
				shops[j] = shops[j + 1];
				shops[j + 1] = temp;
				swapped = true;
			}
		}
	}
}			

void tree::sort_by_y(vector<pizza_shop_main>& shops) {
	bool swapped;
	for (size_t i = 0; i < shops.size() - 1; i++) {
		swapped = false;
		for (size_t j = 0; j < shops.size() - i - 1; j++) {
			point addr1 = shops[j].get_address();
			point addr2 = shops[j + 1].get_address();
			if ((addr1.get_y() > addr2.get_y()) || (addr1.get_y() == addr2.get_y() && addr1.get_x() > addr2.get_x())) {
				// Swap the elements
				pizza_shop_main temp = shops[j];
				shops[j] = shops[j + 1];
				shops[j + 1] = temp;
				swapped = true;
			}
		}
	}
}

pizza_shop_main* tree::build2DTree(vector<pizza_shop_main>& points, int depth = 0) {
	if (points.empty()) {
		r = NULL;
		return nullptr;
	}


	bool sortByX = (depth % 2) == 0;
	if (sortByX) {
		sort_by_x(points);
	}
	else {
		sort_by_y(points);
	}


	size_t median = (points.size() - 1) / 2;
	pizza_shop_main* root = new pizza_shop_main(points[median]);


	vector<pizza_shop_main> leftPoints(points.begin(), points.begin() + median);
	vector<pizza_shop_main> rightPoints(points.begin() + median + 1, points.end());
	root->left = build2DTree(leftPoints, depth + 1);
	root->right = build2DTree(rightPoints, depth + 1);
	r = root;
	return root;
}

double distSquared(pizza_shop_main* p0, point* p1) {
	double total = 0;

	int sub_x = (p0->get_address()).get_x() - p1->get_x();

	sub_x *= sub_x;
	int sub_y = (p0->get_address()).get_y() - p1->get_y();
	sub_y *= sub_y;
	double distance = sqrt(sub_x + sub_y);


	return distance;
}


pizza_shop_main* tree::closest(pizza_shop_main* n0, pizza_shop_main* n1, point* target) {
	if (n0 == nullptr) return n1;
	if (n1 == nullptr) return n0;
	double d1 = distSquared(n0, target);
	double d2 = distSquared(n1, target);
	if (d1 < d2)
		return n0;
	else
		return n1;
}

pizza_shop_main* tree::nearestNeighbor(pizza_shop_main* root, point* target, int depth = 0) {
	if (root == nullptr) return nullptr;
	pizza_shop_main* nextBranch = nullptr;
	pizza_shop_main* otherBranch = nullptr;
	int axis = depth % 2;
	if (axis == 0)
	{
		if (target->get_x() < root->get_address().get_x()) {
			nextBranch = root->left;
			otherBranch = root->right;
		}
		else {
			nextBranch = root->right;
			otherBranch = root->left;
		}
	}
	else {
		if (target->get_y() < (root->get_address()).get_y()) {
			nextBranch = root->left;
			otherBranch = root->right;
		}
		else {
			nextBranch = root->right;
			otherBranch = root->left;
		}
	}

	pizza_shop_main* temp = nearestNeighbor(nextBranch, target, depth + 1);
	pizza_shop_main* best = closest(temp, root, target);
	double radiusSquared = distSquared(best, target);
	if (axis == 0)
	{
		double dist = target->get_x() - root->get_address().get_x();
		if (radiusSquared >= dist * dist) {
			temp = nearestNeighbor(otherBranch, target, depth + 1);
			best = closest(temp, best, target);
		}
	}
	else
	{
		double dist = target->get_y() - root->get_address().get_y();
		if (radiusSquared >= dist * dist) {
			temp = nearestNeighbor(otherBranch, target, depth + 1);
			best = closest(temp, best, target);
		}
	}

	return best;
}
void tree::Near_P() {
	int x, y;
	pizza_shop_main* p;
	cout << "Enter x of your location." << endl;
	cin >> x;
	cout << "Enter y of your location." << endl;
	cin >> y;
	point* target = new point();
	target->set_x(x);
	target->set_y(y);
	p = nearestNeighbor(r, target, 0);

	cout << "Name: " << p->get_name() << endl;
	cout << "x: " << p->get_address().get_x() << "  y: " << p->get_address().get_y() << endl;


}
void tree::Near_Br() {
	int x, y;
	string name;
	cout << "Enter the name of main shop: " << endl;
	cin >> name;
	pizza_shop_main* p;
	pizza_shop_main* my_root;
	int index;
	vector<pizza_shop_main> temp;
	index = search_by_name_shop(name);
	if (index == -1) {
		cout << "Name not found." << endl;
		return;
	}
	else {
		p = Shops[index];

		for (auto i : p->branches) {
			temp.push_back(*i);
		}

		my_root = build2DTree(temp, 0);

	}
	cout << "Enter x of your location." << endl;
	cin >> x;
	cout << "Enter y of your location." << endl;
	cin >> y;
	point* target = new point();
	target->set_x(x);
	target->set_y(y);
	pizza_shop_main* pp;
	pp = nearestNeighbor(my_root, target, 0);
	cout << "Name: " << pp->get_name() << endl;
	cout << "x: " << pp->get_address().get_x() << endl;
	cout << "y: " << pp->get_address().get_y() << endl;
}




void tree::Avail_P()
{
	int R;
	int x;
	int y;
	bool is_exist_shop = false;
	point* center = new point();
	cout << "Enter x of current location: " << endl;
	cin >> x;
	cout << "Enter y of current location: " << endl;
	cin >> y;
	center->set_x(x);
	center->set_y(y);
	cout << "enter the radius: " << endl;
	cin >> R;
	int distance = 0;
	int cnt = 0;
	vector<pizza_shop_main> main_vec;
	for (auto i : shops) {
		main_vec.push_back(*i);
	}
	while (distance <= R)
	{
		pizza_shop_main* Best = nearestNeighbor(r, center, 0);
		distance = distSquared(Best, center);
		if (distance <= R) {
			cout << "Name: " << Best->get_name() << endl;
			is_exist_shop = true;
		}
		int counter = 0;
		for (auto i : main_vec) {
			if (i.get_name() == (*Best).get_name()) {
				main_vec.erase(main_vec.begin() + counter);
			}
			counter++;
		}
		build2DTree(main_vec, 0);
	}
	if (!is_exist_shop) {
		cout << "There is no pizza shop in this area." << endl;
	}
}
int tree::hash_function(string name, int i) {
	int sum_asci = 0;
	int hash_value;
	for (char ch : name) {
		sum_asci += static_cast<int>(ch);
	}
	hash_value = (sum_asci + i) % 100;
	return hash_value;
}

void tree::ADD_P()
{
	string name;
	cout << "\nEnter the name of the pizza shop: ";
	cin >> name;
	int x, y;
	cout << "Enter x of the new point:";
	cin >> x;
	cout << "\nEnter y of the new point:";
	cin >> y;
	point p(x, y);
	pizza_shop_main* ps = new pizza_shop_main();
	ps->name = name;
	ps->address = p;
	int counter = 0;
	int index;
	if (shops.size() != 0) {
		if (is_full(&p, r, name)) {
			return;
		}
	}
	while (counter < 100) {
		index = hash_function(name, counter);
		if (Shops[index] == NULL) {
			shops.push_back(ps);
			Shops[index] = ps;
			cout << "Added successfully." << endl;
			//cout << "index: " << index << endl;
			break;
		}
		else {
			counter++;
		}
	}
	vector<pizza_shop_main> main_vec;
	for (auto i : shops) {
		main_vec.push_back(*i);
	}
	build2DTree(main_vec, 0);

}
int tree::search_by_name_shop(string name) {
	int counter = 0;
	int index = hash_function(name, 0);
	while (counter < 100 and Shops[index] != NULL) {
		if (Shops[index]->get_name() == name) {
			cout << "Name found." << endl;
			return index;
		}
		else {
			counter++;
		}
	}
	cout << "Name not found." << endl;
	return -1;
}

void tree::ADD_N()
{
	int x1, x2, x3, x4, y1, y2, y3, y4;
	string name;
	cout << "Enter the name of the new neighbourhood: ";
	cin >> name;
	cout << "\nEnter x of the 1st new point:";
	cin >> x1;
	cout << "\nEnter y of the 1st new point:";
	cin >> y1;
	cout << "\nEnter x of the 2nd new point:";
	cin >> x2;
	cout << "\nEnter y of the 2nd new point:";
	cin >> y2;
	cout << "\nEnter x of the 3rd new point:";
	cin >> x3;
	cout << "\nEnter y of the 3rd new point:";
	cin >> y3;
	cout << "\nEnter x of the 4th new point:";
	cin >> x4;
	cout << "\nEnter y of the 4th new point:";
	cin >> y4;
	point p1(x1, y1);
	point p2(x2, y2);
	point p3(x3, y3);
	point p4(x4, y4);
	neighbourhood* n = new neighbourhood();
	n->set_name(name);
	n->set_points(p1, p2, p3, p4);
	int counter = 0;
	int index;
	while (counter < 100) {
		index = hash_function(name, counter);
		if (neighbourhoods[index] == NULL) {
			neighbourhoods[index] = n;
			cout << "Added successfully." << endl;
			cout << "index: " << index << endl;
			break;
		}
		else {
			counter++;
		}
	}
}

void tree::ADD_Br()
{
	string name;
	string main_name;
	cout << "\nEnter the name of the main branch of pizza shop: ";
	cin >> main_name;
	int index_of_main = search_by_name_shop(main_name);
	if (index_of_main != -1) {
		cout << "\nEnter the name of the pizza shop: ";
		cin >> name;

		int x, y;
		cout << "Enter x of the new point:";
		cin >> x;
		cout << "\nEnter y of the new point:";
		cin >> y;
		point p(x, y);
		if (shops.size() != 0) {
			if (is_full(&p, r, name)) {
				return;
			}
		}
		pizza_shop_branch* ps = new pizza_shop_branch();
		ps->name = name;
		ps->address = p;
		ps->name_main_shop = main_name;
		int counter = 0;
		int index;

		Shops[index_of_main]->branches.push_back(ps);

		while (counter < 100) {
			index = hash_function(name, counter);
			if (Shops[index] == NULL) {
				shops.push_back(ps);
				Shops[index] = ps;
				cout << "Added successfully." << endl;
				cout << "index: " << index << endl;
				break;
			}
			else {
				counter++;
			}
		}
		vector<pizza_shop_main> my_vec;
		for (auto i : shops) {
			my_vec.push_back(*i);
		}
		build2DTree(my_vec, 0);
	}

}
void tree::Del_Br() {
	int x, y;

	int counter = 0;
	int index_del;
	cout << "Enter the x of point: " << endl;
	cin >> x;
	cout << "Enter the y of point: " << endl;
	cin >> y;
	for (auto i : shops) {
		if (i->get_address().get_x() == x and i->get_address().get_y() == y) {
			index_del = search_by_name_shop(i->get_name());
			if (i->is_main_shop == true) {
				cout << "You can not delete main store!!!" << endl;
				return;
			}
			pizza_shop_main* ptr = Shops[index_del];
			pizza_shop_branch* psb = dynamic_cast<pizza_shop_branch*>(ptr);
			int main_index = search_by_name_shop(psb->get_name_main_shop());
			pizza_shop_main* main_shop = Shops[main_index];
			int ctr = 0;
			for (auto i : main_shop->branches) {
				if (i->get_name() == psb->get_name()) {
					main_shop->branches.erase(main_shop->branches.begin() + ctr);
				}
				ctr++;
			}
			Shops[index_del] = NULL;
			shops.erase(shops.begin() + counter);
			vector<pizza_shop_main> main_vec;
			for (auto i : shops) {
				main_vec.push_back(*i);
			}
			build2DTree(main_vec, 0);
			return;
		}
		counter++;
	}
	
	cout << "There is no pizza shop in this location." << endl;
}
int tree::search_by_name_neighbourhood(string name) {
	int counter = 0;
	int index = hash_function(name, 0);
	while (counter < 100 and neighbourhoods[index] != NULL) {
		if (neighbourhoods[index]->get_name() == name) {
			cout << "pizza shop found." << endl;
			return index;
		}
		else {
			counter++;
		}
	}
	cout << "name not found." << endl;
	return -1;
}
void tree::List_P() {
	string name;
	cout << "Enter the name." << endl;
	cin >> name;
	int index;
	neighbourhood* x;
	index = search_by_name_neighbourhood(name);
	if (index != -1) {
		x = neighbourhoods[index];
		point a = x->get_point_a();
		point b = x->get_point_b();
		point c = x->get_point_c();
		point d = x->get_point_d();
		for (auto i : shops) {
			point p;
			p = i->get_address();
			double s1, s2, s3, s4, s, n1, n2;
			n1 = (0.5) * abs((a.get_x() * (b.get_y() - c.get_y())) + (b.get_x() * (c.get_y() - a.get_y())) + (c.get_x() * (a.get_y() - b.get_y())));
			n2 = (0.5) * abs((a.get_x() * (d.get_y() - c.get_y())) + (d.get_x() * (c.get_y() - a.get_y())) + (c.get_x() * (a.get_y() - d.get_y())));
			s1 = (0.5) * abs((a.get_x() * (b.get_y() - p.get_y())) + (b.get_x() * (p.get_y() - a.get_y())) + (p.get_x() * (a.get_y() - b.get_y())));
			s2 = (0.5) * abs((p.get_x() * (b.get_y() - c.get_y())) + (b.get_x() * (c.get_y() - p.get_y())) + (c.get_x() * (p.get_y() - b.get_y())));
			s3 = (0.5) * abs((p.get_x() * (d.get_y() - c.get_y())) + (d.get_x() * (c.get_y() - p.get_y())) + (c.get_x() * (p.get_y() - d.get_y())));
			s4 = (0.5) * abs((a.get_x() * (d.get_y() - p.get_y())) + (d.get_x() * (p.get_y() - a.get_y())) + (p.get_x() * (a.get_y() - d.get_y())));
			s = n1 + n2;
			if (s == s1 + s2 + s3 + s4) {
				cout << "Name: " << i->get_name() << endl;
				cout << "x: " << i->get_address().get_x() << endl;
				cout << "y: " << i->get_address().get_y() << endl;
				cout << "-----------------" << endl;
			}

		}

	}
}
void tree::List_Brs() {
	string name;
	cout << "Enter the name." << endl;
	cin >> name;
	int index;
	pizza_shop_main* p;
	index = search_by_name_shop(name);
	if (index != -1) {
		p = Shops[index];
		for (auto i : p->branches) {
			cout << "Name: " << i->get_name() << "\nx: " << i->get_address().get_x() << "  y: " << i->get_address().get_y() << endl;
			cout << "---------" << endl;
		}
	}
	else {
		cout << "Name not found." << endl;
	}
}
void tree::Most_Brs() {
	vector<pizza_shop_main> my_vec;
	if (shops.size() == 0) {
		cout << "Add some pizza shop first." << endl;
		return;
	}
	for (int i = 0; i < shops.size(); i++) {
		if (shops[i]->is_main_shop == true) {
			my_vec.push_back(*(shops[i]));
		}
	}
	int n = my_vec.size();
	for (int i = 0; i < n - 1; ++i) {
		for (int j = 0; j < n - i - 1; ++j) {
			if (my_vec[j].branches.size() < my_vec[j + 1].branches.size()) {
				swap(my_vec[j], my_vec[j + 1]);
			}
		}
	}
	cout << "Name: " << my_vec[0].get_name() << endl;
	cout << "number of branches: " << my_vec[0].branches.size() << endl;

}
bool tree::is_full(point* target, pizza_shop_main* root, string name) {
	pizza_shop_main* my_p;
	bool flag_target = false;
	bool flag_name = false;
	my_p = nearestNeighbor(root, target, 0);
	if (my_p->get_address().get_x() == target->get_x() && my_p->get_address().get_y() == target->get_y()) {
		flag_target = true;
	}
	int index;
	index = search_by_name_shop(name);
	if (index != -1) {
		flag_name = true;
	}
	if (flag_target) {
		cout << "Location is full!!!" << endl;
		return true;
	}
	if (flag_name) {
		cout << "Name already exist." << endl;
		return true;
	}
	return false;

}
bool tree::is_empty() {
	if (shops.size() == 0) {
		return true;
	}
	return false;
}


tree::~tree()
{
}
