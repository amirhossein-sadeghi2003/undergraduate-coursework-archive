module gate_xor_with_nor(in1, in2, out);
	input in1, in2;
	output out;
	gate_not_with_nor g1(in1, inbar1);
	gate_not_with_nor g2(in2, inbar2);
	gate_and_with_nor g3(inbar1, in2, x);
	gate_and_with_nor g4(inbar2, in1, y);
	nor g5(outbar, x, y);
	gate_not_with_nor g6(outbar, out);
endmodule
	