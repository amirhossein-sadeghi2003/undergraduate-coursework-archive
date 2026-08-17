primitive my_primitive(out, a, b, c, d);
	input a, b, c, d;
	output out;
	table
		//a b c d: out
		1 1 0 ?: 1;
		1 0 1 ?: 1;
		? ? 0 ?: 1;
		? ? ? 0: 1;
		0 0 1 1: 0;
		0 1 1 1: 0;
		1 1 1 1: 0;
	endtable
endprimitive
