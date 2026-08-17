module subtraction(out, in1, in2);

	output [31 : 0] out;
	input [31 : 0] in1;
	input [31 : 0] in2;
	
	reg [31 : 0] copyIn2;
	
	always@(in2)
		begin
			copyIn2 = in2;
			copyIn2[31] = ~copyIn2[31];
		end
	
	addition add(out, in1, copyIn2);
	
endmodule