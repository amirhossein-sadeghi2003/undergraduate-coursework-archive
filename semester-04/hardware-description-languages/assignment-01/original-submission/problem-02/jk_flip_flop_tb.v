module top_module();
	reg j, k, clk;
	wire q, qbar; 
	flip_flop_jk flip_flop_1(j, k, clk, q, qbar);
	initial
		begin
			#200 {j, k, clk} = 3'b000;
			#200 {j, k, clk} = 3'b001;
			#200 {j, k, clk} = 3'b100;
			#200 {j, k, clk} = 3'b101;
			#200 {j, k, clk} = 3'b010;
			#200 {j, k, clk} = 3'b011;
			#200 {j, k, clk} = 3'b110;		
			#200 {j, k, clk} = 3'b111;
		end
endmodule
