module merge(out, in1, in2, operation);
	
	output reg [31 : 0] out;
	input [31 : 0] in1;
	input [31 : 0] in2;
	input [2 : 0] operation;
	
	wire [31 : 0] out0, out1, out2, out3, out4, out5, out6, out7;

	addition add(out0, in1, in2);
	subtraction sub(out1, in1, in2);
	multiply mul(out2, in1, in2);
	divide div(out3, in1, in2);
	power pow(out4, in1, in2);
	log l(out5, in1, in2);
	CORDIC cor(out7, out6, in1);
	
	always@(in1 or in2 or operation)
		begin
			case(operation)
				0:
					out = out0;
				1:
					out = out1;
				2:
					out = out2;
				3:
					out = out3;
				4:
					out = out4;
				5:
					out = out5;
				6:
				begin
					out = out6;
					out[31 : 16] = 0;
				end
				7:
				begin
					out = out7;
					out[31 : 16] = 0;
				end
			endcase
		end	
endmodule


/*
module merge(final_out, in1, in2, operation,part);
	
	reg [31 : 0] out;
	input [31 : 0] in1;
	input [31 : 0] in2;
	input [2 : 0] operation;
	
	wire [31 : 0] out0, out1, out2, out3, out4, out5, out6, out7;
	output reg [7:0] final_out;// 8 LED
	input  [1:0] part; // dip switch

	addition add(out0, in1, in2);
	subtraction sub(out1, in1, in2);
	multiply mul(out2, in1, in2);
	divide div(out3, in1, in2);
	power pow(out4, in1, in2);
	log l(out5, in1, in2);
	CORDIC cor(out7, out6, in1);
	
	always@(in1 or in2 or operation)
		begin
			case(operation)
				0:
					out = out0;
				1:
					out = out1;
				2:
					out = out2;
				3:
					out = out3;
				4:
					out = out4;
				5:
					out = out5;
				6:
				begin
					out = out6;
					out[31 : 16] = 0;
				end
				7:
				begin
					out = out7;
					out[31 : 16] = 0;
				end
			endcase
		end	
	always@(part)
	begin
			$display("out: %b", out);
			$display("part: %b", part);
			
			case(part)
			0: final_out = out[7 : 0]; 
			1: final_out = out[15 : 8]; 
			2: final_out = out[23 : 16]; 
			3: final_out = out[31 : 24]; 
		endcase
	end
endmodule
*/
