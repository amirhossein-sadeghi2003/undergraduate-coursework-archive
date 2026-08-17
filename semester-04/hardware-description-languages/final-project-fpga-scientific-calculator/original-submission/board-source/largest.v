module largest(out, num1, num2);

	parameter length = 1;
	
	output reg out;
	input [length - 1 : 0] num1, num2;
	
	always@(num1 or num2)
		begin
			if(num1 > num2)
				out = 0;
			else
				out = 1;
		end
	
endmodule