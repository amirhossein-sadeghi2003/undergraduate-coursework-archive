module divide (result, in1, in2);

input [31:0] in1, in2;
output reg [31:0] result;

reg [24:0] num2 = 0;
reg [23:0] num1, temp; 
integer i;
integer j;

always@(in1 or in2)
begin
	result[31] =  in1[31] ^ in2[31];
	result[30:23] = in2[30:23] - in1[30:23] + 127;
	

	num2 [23:0] = 24'h800000 + in2[22:0];
	num1 = 24'h800000 + in1[22:0];

	for (i = 23; i >= 0; i = i-1)
	begin
		
		temp[i] = (num2 >= num1);
		for (j=0; j<23 ; j = j + 1)
		begin
			if (num2 > num1)
			begin
				num2 = num2 - num1;
			end
			else
			begin
				num2 = num2 * 2;
				j = 24;
			end
		end
		//num2 = (num2 % num1) * 2;
		/*temp[i] = num2 / num1;
		/*num2[23:1] = num2[22:0];
		num2[0] = 0;*/
		//num2 = (num2 % num1) << 1;*/
	end
	//$display("temp: %b", temp); 
	if ( temp[23] == 1)
		result[22:0] = temp[22:0];
		
	else
	begin
		result[22:1] = temp[21:0];
		result[0] = 0'b0;
		result[30:23] = result[30:23] - 1;
	end
	num2 =0;
	num1 =0;
	temp = 0;
	//$display("%b", result);

end
endmodule 


/*module test_divide;

reg [31:0] in1, in2;
wire [31:0] result;
	divide my_div (result, in1, in2);
	
initial
begin
	
	#100 in1 <= 32'h3FA00000; // 1.25
	in2 <= 32'h40B00000;  // 5.5
	//#500 $display("%b", result); // 4.4
	
	#100 in1 <= 32'h3FA1EECC; // 1.2651 
	in2 <= 32'hC6B4E400; // -23154
	//#500 $display("%b", result); // -18,302.110505099
	
	#100 in1 <= 32'hC0780000; // -3.875 
	in2 <= 32'hC6B4E400; // -23154
	//#500 $display("%b", result); // 5,975.2258
	
			
	#100 in1 <= 32'h3E000000; // 0.125 
	in2 <= 32'h40666666; // 3.6
	//#500 $display("%b", result); //28.8
	
	#100 in1 <= 32'h40400000; // 3 
	in2 <= 32'h41000000; // 8
	//#500 $display("%b", result); //2.6666
	
end
endmodule 
*/