
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
						i = 34;
					end
			end
			//$display("Log: %d", answer);
	end
endmodule
