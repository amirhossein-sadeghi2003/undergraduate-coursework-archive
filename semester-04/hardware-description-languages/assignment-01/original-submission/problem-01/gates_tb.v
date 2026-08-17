module top_module();
	reg x, y;
	wire result_and, result_xor, result_not_y;
	gate_xor_with_nor(x, y, result_xor);
	gate_and_with_nor(x, y, result_and);
	gate_not_with_nor(y, result_not_y);
	initial
		begin
			#200 {x, y} = 2'b00;
			#200 {x, y} = 2'b01;
			#200 {x, y} = 2'b10;
			#200 {x, y} = 2'b11;
		end
endmodule