module top_module();
	reg [4:0] a, b;
	reg [1:0] s;
	wire [5:0] out; 
	alu alu_1(a, b, s, out);
	initial
		begin
			#200 {a,b,s} =  12'b011010110000;
			#200 {a,b,s} =  12'b010100110001; 
			#200 {a,b,s} =  12'b010101010010; 
			#200 {a,b,s} =  12'b011001010011; 
		end
endmodule 