module test;
	
	wire [31 : 0]out; 
	reg [2 : 0] operation;
	reg [31:0]in1, in2;
	integer i;
	
	merge m (out, in1, in2, operation);
	
	initial
	begin
		
		in1 <= 32'b00111111100000000000000000001000; // 1.00000095367431640625 // 8 // 89.29687567
		in2 <= 32'b01000000000000000000000000000100; // 2.00000095367431640625 // 4 // 90.00000033527613;
		for(i = 0; i < 8; i = i + 1)
		begin
			#100;
			operation = i;
			$monitor("%d- : binary: %b,   decimal:%d    hex: %h",i,out, out, out);
		end
		
	end
endmodule

/*
add: 1.00000095367431640625 + 2.00000095367431640625 = 3.0000019073486328125 ---> floating point ---> h'40400008 ---> 3.0000019073486328125

sub: 1.00000095367431640625 - 2.00000095367431640625 = -1  ---> floating point ---> h'BF800000 ---> -1

multiply 1.00000095367431640625 * 2.00000095367431640625 = 2.000002861 ---> floating point ---> h'4000000C ---> 2.00000286102294921875

division: 2.00000095367431640625 / 1.00000095367431640625 = 1.999999046 ---> floating point ---> h'3FFFFFF8 ---> 1.99999904632568359375

power: 1000 ** 100 = 1000000000000 = 8 ** 4 = 4096 

log: 1065353224  1073741828 = 0

SIN(89.29687567) = 0.999924702  --> 31993 / 32000 = 0.99978125

COS(89.29687567) = 0.01227152659 --> 390 / 32000 = 0.0121875
*/

















/*
module merge(out, in1, in2, operation);
	
	output reg [31 : 0] out;
	input [31 : 0] in1;
	input [31 : 0] in2;
	input [2 : 0] operation;
*/



/*module top(out, part, operation);
	
	output reg [7 : 0]out;
	input [1 : 0]part;
	input [2 : 0] operation;
	
	//reg [31 : 0] in1, in2;
	wire [31 : 0] outMerge;
	
	merge m(outMerge, operation);
	
	always@(part or operation)
	begin
		//in1 = 32'b00111111100000000000000000001000; // 1.00000095367431640625 // 8 // 89.296
		//in2 = 32'b01000000000000000000000000000100; //2.00000095367431640625 // 4 // 90.00000033527613;
		case(part)
			0: out = outMerge[7 : 0]; 
			1: out = outMerge[15 : 8]; 
			2: out = outMerge[23 : 16]; 
			3: out = outMerge[31 : 24]; 
		endcase
	end

endmodule*/