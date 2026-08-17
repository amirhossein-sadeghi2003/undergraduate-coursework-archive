module shift_register(clk, load, data, clear, shift, dir, out);
	input clk, load, clear, shift, dir;
	input [7:0] data;
	output reg [7:0] out;
	integer j, t;
	always@(negedge clk)
		begin
			if (clear == 1)
				out = 0;
			else if (load == 1)
				out = data;
			else if (shift == 1) 
				begin
					if(dir == 0)
						begin
							t = out[7];
							for(j = 7; j > 0 ; j = j - 1)
							out[j] = out[j - 1];
							out[0] = t;
						end
			else if(dir == 1)
			begin
				t = out[0];
				for(j = 0; j < 7 ; j = j + 1)
					out[j] = out[j + 1];						
					out[7] = t;
				end
			end
		end 
endmodule 