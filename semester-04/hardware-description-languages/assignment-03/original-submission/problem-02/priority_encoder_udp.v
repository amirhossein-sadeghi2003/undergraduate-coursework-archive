primitive bit_1_out(w1, a1, a2, a3, a4, e);
	input a1, a2, a3, a4, e;
	output w1;
	table
		//a1 a2 a3 a4 e: w1
		? ? ? ? 0: 0;
		0 0 0 1 1: 1;
		0 0 1 ? 1: 1;
		0 1 0 0 1: 0;
		0 1 0 1 1: 1;
		0 1 1 ? 1: 1;
		1 0 0 0 1: 0;
		1 0 0 1 1: 1;
		1 0 1 ? 1: 1;
		1 1 0 0 1: 0;
		1 1 0 1 1: 1;
		1 1 1 ? 1: 1;
	endtable
endprimitive



primitive bit_0_out(w0, a1, a2, a3, a4, e);
	input a1, a2, a3, a4, e;
	output w0;
	table
		//a1 a2 a3 a4 e: w0
		? ? ? ? 0: 0;
		0 0 0 1 1: 1;
		0 0 1 0 1: 0;
		0 0 1 1 1: 1;
		0 1 0 ? 1: 1;
		0 1 1 0 1: 0;
		0 1 1 1 1: 1;
		1 0 ? 0 1: 0;
		1 0 ? 1 1: 1;
		1 1 0 ? 1: 1;
		1 1 1 0 1: 0;
		1 1 1 1 1: 1;
	endtable
endprimitive
