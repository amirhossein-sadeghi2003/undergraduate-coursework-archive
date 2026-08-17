module ripple_adder(in1, in2, cin, sum, cout);
	input [7:0] in1;
	input [7:0] in2;
	input cin;
	output [7:0] sum;
	output cout;	
	wire [7:0] c;
	full_adder fa0(in1[0], in2[0], cin, sum[0], c[0]);
	generate
		genvar q;
		for (q = 1; q <= 6; q = q + 1)
			full_adder fa(in1[q], in2[q], c[q - 1], sum[q], c[q]);
	endgenerate
	full_adder fa7(in1[7], in2[7], c[6], sum[7], cout);

endmodule
module full_adder(in1, in2, cin, s, cout);
 	input in1, in2, cin;
	output s, cout; 
  	wire r1, r2;
  	xor#(8, 4) (x1, in1, in2);
  	xor#(8, 4) (s, x1, cin);
  	and#(5, 3) (r1, x1, cin);
  	and#(5, 3) (r2, in1, in2);
  	or#(6, 3) (cout, r1, r2);
endmodule
module test;
	reg [7:0] in1, in2;
	reg cin;
	wire [7:0] sum;
	wire cout;
	ripple_adder(in1, in2, cin, sum, cout);
	initial 
		begin
			#100 {in1, in2, cin} = 2'b10001010110001010;
		end
endmodule