module compare_16_bit(in1, in2, x, Y, Z);
	input [15:0] in1, in2;
	output x, y, z;
	wire X0, X1, X2, X3;
	wire Y0, Y1, Y2, Y3;
	wire Z0, Z1, Z2, Z3;
	compare_4_bit c3(in1[15:12], in2[15:12], X3, Y3, Z3);
	compare_4_bit c2(in1[11:8], in2[11:8], X2, Y2, Z2);
	compare_4_bit c1(in1[7:4], in2[7:4], X1, Y1, Z1);
	compare_4_bit c0(in1[3:0], in2[3:0], X0, Y0, Z0);
	assign x = X3 | ( ~X3 & Z3 & X2) | (~X3 & ~X2 & Z3 & Z2 & X1) | (~X3 & ~X2 & ~X1 & Z3 & Z2 &  Z1 & X0);
	assign y = Y3 | ( ~Y3 & Z3 & Y2) | (~Y3 & ~Y2 & Z3 & Z2 & Y1) | (~Y3 & ~Y2 & ~Y1 & Z3 & Z2 &  Z1 & Y0);
	assign z = Z3 & Z2 & Z1 & Z0; 
endmodule
