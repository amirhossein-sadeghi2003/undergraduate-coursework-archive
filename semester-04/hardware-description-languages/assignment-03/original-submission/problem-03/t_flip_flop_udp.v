primitive t_flip_flop(q, t, clk, set, reset);
	output q;
	reg q;
	input t, clk, set, reset;
	table
		//t clk set reset: q: q+
		? ? 1 ?: ?: 1;
		? ? 0 1: ?: 0;
		0 (01) 0 0: ?: -;
		1 (01) 0 0: 0: 1;
		1 (01) 0 0: 1: 0;
		(??) ? 0 0: ?: -;
		? (10) 0 0: ?: -;
	endtable
endprimitive

