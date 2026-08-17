module gate_and_with_nor(in1, in2, out);
	input in1, in2;
	output out;
	gate_not_with_nor g1(in1, in1_bar);
	gate_not_with_nor g2(in2, in2_bar);
	nor g3(out, in1_bar, in2_bar);
endmodule