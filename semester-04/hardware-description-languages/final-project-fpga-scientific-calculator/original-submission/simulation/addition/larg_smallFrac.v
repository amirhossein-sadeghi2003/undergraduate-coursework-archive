module larg_smallFrac(largFrac, smallFrac, signLarg, in1, in2);
	
	output [25 : 0] largFrac, smallFrac;
	input [22 : 0] in1, in2;
	input signLarg;
	
	swap s(largFrac[23 : 1], smallFrac[23 : 1], in1, in2, signLarg);
	defparam s.length = 23;
	
	assign largFrac[25 : 24] = 2'b01;
	assign smallFrac[25 : 24] = 2'b01;
	assign largFrac[0] = 1'b0;
	assign smallFrac[0] = 1'b0;
	
endmodule