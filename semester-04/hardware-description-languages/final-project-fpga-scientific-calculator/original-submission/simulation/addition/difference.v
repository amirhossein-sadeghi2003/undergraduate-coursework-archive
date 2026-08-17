module difference(dif, sign, num1, num2);

	parameter length = 1;
	
	output reg sign;
	output reg [length - 1 : 0]dif;
	input [length - 1 : 0] num1, num2;
	
	always@(num1 or num2)
		begin
			if(num1 > num2)
				begin
					dif = num1 - num2;
					sign = 0;
				end
			else
				begin
					dif = num2 - num1;
					sign = 1;
				end
		end
	
endmodule