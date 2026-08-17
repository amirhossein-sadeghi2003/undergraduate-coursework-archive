
module log(answer, a, b);
	input [31:0] a, b;
	output reg [31:0] answer;

	reg [31:0] temp;
	integer i;

always@(a or b)
	begin
		temp = b;
		for(i = 0; i < 33; i = i + 1)
			begin
				if(temp <= a)
					begin
						temp = temp * b;
					end	
				else
					begin
						answer = i;
						i = 100;
					end
			end
	end
endmodule


/*
module log(answer, a, b, enable);
	input [9:0] a, b;
	output reg [9:0] answer;
	input enable;

	reg [9:0] temp;
	integer i;

	always@(a or b or enable)
		begin
		if(enable)
			answer = 0;
		begin
			temp = a;
			for(i = 0; i < 16; i = i + 1)
				begin
					if(temp >= b)
						begin
							temp = temp / b;
							answer = answer + 1;
						end
					else
						begin
							i = 100;
						end
				end
		end
		end
endmodule
*/