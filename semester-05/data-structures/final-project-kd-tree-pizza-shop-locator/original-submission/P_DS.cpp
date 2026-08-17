#include "point.h"
#include "pizza_shop_main.h"
#include <iostream>
#include <string.h>
#include <vector>
#include "pizza_shop_branch.h"
#include "tree.h"
using namespace std;



int main()
{
	int choice;
	tree t;
	while (true)
	{
		cout << "Enter the row number to choose: " << endl;
		cout << endl;
		cout << "1.ADD_N" << endl;
		cout << endl;
		cout << "2.ADD_P" << endl;
		cout << endl;
		cout << "3.ADD_Br" << endl;
		cout << endl;
		cout << "4.Del_Br" << endl;
		cout << endl;
		cout << "5.List_P" << endl;
		cout << endl;
		cout << "6.List_Brs" << endl;
		cout << endl;
		cout << "7.Near_P" << endl;
		cout << endl;
		cout << "8.Near_Br" << endl;
		cout << endl;
		cout << "9.Avail_P" << endl;
		cout << endl;
		cout << "10.Most_Brs" << endl;
		cout << endl;
		cin >> choice;
		if (t.is_empty() && choice != 1 && choice != 2 && choice != 3)
		{
			cout << "There is no pizaa shop.You should add some shops first." << endl;
			continue;
		}
		switch (choice)
		{
		case 1:
			t.ADD_N();
			break;
		case 2:
			t.ADD_P();
			break;
		case 3:
			t.ADD_Br();
			break;
		case 4:
			t.Del_Br();
			break;
		case 5:
			t.List_P();
			break;
		case 6:
			t.List_Brs();
			break;

		case 7:
			t.Near_P();
			break;
		case 8:
			t.Near_Br();
			break;
		case 9:
			t.Avail_P();
			break;
		case 10:
			t.Most_Brs();
			break;

		default:
			break;
		}


	}

}
