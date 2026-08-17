module power(answer, a, b);
	input [3:0] a;
	input [2:0] b;
	output reg [31:0] answer;
	
	integer i;
	always@(a or b)
		begin	
			answer = 1;
			for(i = 0; i < 16; i = i + 1)
				begin
		     			if(i < b)
						begin
							answer = answer * a;
						end
					else
						begin
							i = 17;
						end
				end
			//$display("Power: %d", answer);
		end
	
endmodule
