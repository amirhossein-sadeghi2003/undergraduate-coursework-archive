module signComputation(signOut , add_subBar, sign1, sign2, largestNum);

	output reg signOut, add_subBar;
	input sign1, sign2, largestNum;
	
	always@(sign1 or sign2 or largestNum)
		begin
			signOut = (largestNum) ? sign2 : sign1;
			add_subBar = (sign1 == sign2) ? 1 : 0 ;
		end

endmodule