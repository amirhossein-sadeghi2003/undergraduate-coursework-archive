`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date:    23:13:49 06/30/2023 
// Design Name: 
// Module Name:    top 
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
module top(clk,part,operation,out);

	input clk;
	input [1:0] part;//dip switch
	input [2:0] operation;//dip switch
	output reg [7 : 0]out;//8 LEDs
	wire [31:0] out_merge;
	wire [63:0] Max;

	
	memory m1(clk,Max);//memorty has 2 row
	merge merge_inst(.out(out_merge), .in1(Max[31:0]), .in2(Max[63:32]), .operation(operation));
	
	always@(part or operation)
	begin
		case(part)
			0: out = out_merge[7 : 0]; 
			1: out = out_merge[15 : 8]; 
			2: out = out_merge[23 : 16]; 
			3: out = out_merge[31 : 24]; 
			default: out = 8'b0;
		endcase
	end

endmodule
/*
	output reg [7 : 0]out;
	input [1 : 0]part;
	input [2 : 0] operation;
	
	reg [31 : 0] in1, in2;
	wire [31 : 0] outMerge;
	
	merge m(outMerge, in1, in2, operation);
	

	end*/