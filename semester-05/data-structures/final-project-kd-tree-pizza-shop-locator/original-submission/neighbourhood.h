#pragma once
#include "point.h"
#include <string.h>
#include <iostream>
using namespace std;
class neighbourhood
{
private:
	point a, b, c, d;
	string name;
public:
	neighbourhood();
	neighbourhood(string, point, point, point, point);
	string get_name();
	void set_name(string);
	void set_points(point, point, point, point);
	point get_point_a();
	point get_point_b();
	point get_point_c();
	point get_point_d();
	~neighbourhood();
};

