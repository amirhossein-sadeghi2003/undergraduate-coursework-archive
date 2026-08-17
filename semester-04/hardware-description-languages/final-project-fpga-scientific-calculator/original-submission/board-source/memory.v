`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    22:34:33 06/30/2023 
// Design Name: 
// Module Name:    memory 
// Project Name: 
// Target Devices: 
// Tool versions: 
// Description: 
//
// Dependencies: 
//
// Revision: 
// Revision 0.01 - File Created
// Additional Comments: 
//
//////////////////////////////////////////////////////////////////////////////////
module memory(clk, Max);

	input clk;
	output reg [63:0] Max;
	
	wire [31:0] dout;
	reg [1:0] addr_reg = 0, addr_next;
	integer flag = 0;

	blkROM inl(
	.clka (clk),
	// input wire clka
	.addra (addr_reg), // input wire [3:0] addra
	.douta (dout));// output wire [3:0] douta
	
	
	always @(posedge clk) begin
		addr_reg <= addr_next;
	end

	always @(*) begin
		if(addr_reg == 1)
			addr_next = addr_reg;
		else
			addr_next = addr_reg + 1;
	end

	always @(*) begin
		if(flag == 0)begin
			Max[31:0] = dout;
			flag = flag + 1;
		end
		else if(flag == 1) begin
			Max[63:32] = dout;
			flag = 3;
		end
	end

endmodule
