#pragma once
class point
{
private:
	int x, y;

public:
	point();
	point(int, int);
	int get_x();
	void set_x(int);
	int get_y();
	void set_y(int);
	~point();
};

