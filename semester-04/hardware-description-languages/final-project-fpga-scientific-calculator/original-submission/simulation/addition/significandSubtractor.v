module significandSubtractor(out, frac1, frac2, smallFrac);
	
	output reg [25 : 0] out = 0;
	input [25 : 0] frac1, frac2;
	input smallFrac;
	
	always@(frac1 or frac2 or smallFrac)
		begin
			out = frac1 - frac2 - smallFrac;
		end

endmodule