module addition(out, in1, in2);
	
	output [31 : 0] out;
	input [31 : 0] in1, in2;
	
	wire signLarg;
	wire signExp;
	wire [7 : 0] diffExp;
	wire [25 : 0] largFrac, smallFrac;
	
	difference d(diffExp, signExp, in1[30 : 23], in2[30 : 23]);
	defparam d.length = 8;

	largestFloat lf(signLarg, diffExp, signExp, in1[22 : 0], in2[22 : 0]);
	
	larg_smallFrac lsf(largFrac, smallFrac, signLarg, in1[22 : 0], in2[22 : 0]);
	
	reg smallSection;
	reg [25 : 0] smallFracCopy;
	always@(smallFrac or diffExp)
		begin
			smallFracCopy = smallFrac << 26 - diffExp;
			if(smallFracCopy == 0)
				smallSection = 0;
			else
				smallSection = 1;
			smallFracCopy = smallFrac >> diffExp;
		end
		
	wire add_subBar;
	signComputation sc(out[31] , add_subBar, in1[31], in2[31], signLarg);
	
	wire [25 : 0] fracSub;
	significandSubtractor ss(fracSub, largFrac, smallFracCopy, smallSection);
	
	wire [25 : 0] fracAdd;
	significandAdder sa(fracAdd, largFrac, smallFracCopy);
	
	reg [25 : 0] frac;
	always@(fracAdd or fracSub or add_subBar)
		begin
			if(add_subBar)
				frac = fracAdd;
			else
				frac = fracSub;
		end
	
	wire [4 : 0] c;
	wire add_subBar_expComp;
	fracComputation fc(out[22 : 0], c, add_subBar_expComp, frac);

	reg [7 : 0] largestExp;
	always@(in1[30 : 23] or in2[30 : 23] or signExp)
		begin
			if(signExp == 0)
				largestExp = in1[30 : 23];
			else
				largestExp = in2[30 : 23];
			
		end
	
	expComputation ec(out[30 : 23], c, add_subBar_expComp, largestExp);
	
endmodule