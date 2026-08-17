module find_bit_1(b, clk, out1, out2);
	input b, clk;
	output reg out1, out2;
	reg state, next_state;
	integer counter = 0;
	//state register
	always@ (posedge clk)
		begin
			#0 state = next_state;
		end
	//next state logic
	always@ (posedge clk)
		begin
			next_state = b;
			if(b == 1'b1)
				counter = counter + 1;
			else if (b == 1'b0)
				counter = 0;
		end
	//output logic
	always@ (counter)
		begin
			if(counter == 2)
				out1 = 1'b1;
				#100 out1 = 1'b0;
			if(counter < 4)
				out2 = 1'b1;
			else if(counter >= 4)
				out2 = 1'b0;
		end
endmodule
