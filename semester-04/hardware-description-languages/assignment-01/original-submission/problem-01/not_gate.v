module gate_not_with_nor(in, out);
	input in;
	output out;
	nor(out, in, in);
endmodule