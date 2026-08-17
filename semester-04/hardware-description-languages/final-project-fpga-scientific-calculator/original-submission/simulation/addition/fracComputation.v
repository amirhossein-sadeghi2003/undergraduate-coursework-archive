module fracComputation(out, c, add_subBar, frac);

	output reg [22 : 0]out;
	output reg [4 : 0]c;
	output reg add_subBar;
	input [25 : 0] frac;

	reg [25 : 0] fracCopy;
	
	reg [4 : 0] i, indexFrac;
	
	always@(frac)
		begin	
			fracCopy = frac;
			
			for(i = 25; ~(i > 25); i = i - 1)
				begin
					if(frac[i] == 1)
						begin
							indexFrac = i;
							i = -1;
						end
					fracCopy = fracCopy << 1;
				end
			if(indexFrac == 25)
				begin
					add_subBar = 1;
					c = 1;
				end
			else
				begin
					add_subBar = 0;
					c = 24 - indexFrac;
				end
			out[22 : 0] = fracCopy[25 : 3];
		end
endmodule