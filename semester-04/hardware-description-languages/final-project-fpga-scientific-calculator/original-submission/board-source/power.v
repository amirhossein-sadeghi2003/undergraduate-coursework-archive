module power(answer, a, b);
	input [3:0] a, b;

	output reg [59:0] answer;
	
	integer i;
	integer counter = 0;
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
							i = 100;
						end
				end
		end
endmodule
