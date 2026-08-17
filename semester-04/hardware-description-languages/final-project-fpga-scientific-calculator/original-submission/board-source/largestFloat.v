module largestFloat(out, diffExp, signExp, in1, in2);
	
	output reg out;
	input [22 : 0] in1, in2;
	input [7 : 0] diffExp;
	input signExp;
	
	wire signFrac;
	
	largest l(signFrac, in1, in2);
	defparam l.length = 23;
	always@(diffExp or signFrac or signExp)
		begin
			if(diffExp == 0)
				out = signFrac;
			else
				out = signExp;
		end
	
endmodule