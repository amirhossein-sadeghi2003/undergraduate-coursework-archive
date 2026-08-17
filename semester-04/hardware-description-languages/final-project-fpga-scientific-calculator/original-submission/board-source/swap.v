module swap(out1, out2, in1, in2, select);

	parameter length = 1;
	
	output reg [length - 1 : 0] out1, out2;
	input [length - 1 : 0] in1, in2;
	input select;
	
	always@(select or in1 or in2)
	begin
		if(select)
		begin
			out1 = in2;
			out2 = in1;
		end
		else
		begin
			out1 = in1;
			out2 = in2;
		end
	end
	
endmodule