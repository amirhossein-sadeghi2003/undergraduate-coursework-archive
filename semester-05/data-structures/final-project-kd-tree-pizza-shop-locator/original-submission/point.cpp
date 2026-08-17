#include "point.h"
point::point()
{
}

point::point(int x, int y)
{
	this->x = x;
	this->y = y;
}

point::~point()
{
}

int point::get_x()
{
	return x;
}

void point::set_x(int x)
{
	this->x = x;
}

int point::get_y()
{
	return y;
}

void point::set_y(int y)
{
	this->y = y;
}

