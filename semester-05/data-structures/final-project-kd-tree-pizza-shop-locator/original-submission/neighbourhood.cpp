#include "neighbourhood.h"



neighbourhood::neighbourhood()
{
}

neighbourhood::neighbourhood(string name, point a, point b, point c, point d)
{
	this->name = name;
	this->a = a;
	this->b = b;
	this->c = c;
	this->d = d;
}

string neighbourhood::get_name()
{
	return name;
}

void neighbourhood::set_name(string name) {
	this->name = name;
}
void neighbourhood::set_points(point a, point b, point c, point d) {
	this->a = a;
	this->b = b;
	this->c = c;
	this->d = d;
}
point neighbourhood::get_point_a() {
	return a;

}
point neighbourhood::get_point_b() {
	return b;

}
point neighbourhood::get_point_c() {
	return c;

}
point neighbourhood::get_point_d() {
	return d;

}

neighbourhood::~neighbourhood()
{
}
