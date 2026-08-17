module significandAdder(out, frac1, frac2);
	
	output reg [25 : 0] out = 0;
	input [25 : 0] frac1, frac2;
	
	always@(frac1 or frac2)
		begin
			out = frac1 + frac2;
		end

endmodule