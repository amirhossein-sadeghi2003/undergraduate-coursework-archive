module alu(a, b, s, out);
	input [4:0] a, b;
	input [1:0] s;
	output reg [5:0] out;
	always@(a or b or s)
		begin	
			if( s == 2'b00)
				out = a;
			else if ( s == 2'b01)
				out = a + b;
			else if ( s == 2'b10)
				out = a - b;
			else if ( s == 2'b11)
				out = a + 1;
			else 
				$display("Invalid!!");
		end
endmodule
