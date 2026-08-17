module expComputation(out, c, add_subBar, largestExp);

	output reg [7 : 0] out;
	input [4 : 0] c;
	input add_subBar;
	input [7 : 0] largestExp;
	
	always@(c or add_subBar or largestExp)
		begin
			if(add_subBar)
				out = largestExp + c;
			else
				out = largestExp - c;
		end
endmodule