module compare_4_bit(in1, in2, x, y, z);
	input [3:0] in1, in2;
	output x, y, z;
	assign x = (in1 > in2)? 1:0;
	assign y = (in1 < in2)? 1:0;
	assign z = (in1 == in2)? 1:0;
endmodule
