module flip_flop_jk(j, k, clk, q, qbar);
	input j, k, clk;
	output q, qbar;
	wire r, s;
	nor g1(q, r, qbar);
	nor g2(qbar, q, s);
	and g3(s, j, qbar, clk);
	and g4(r, q, k, clk);
endmodule
