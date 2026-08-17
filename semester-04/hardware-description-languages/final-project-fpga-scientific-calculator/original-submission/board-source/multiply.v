module multiply (result, in1, in2);

input [31:0] in1, in2;
output reg [31:0] result;

reg [47:0] temp; 

always@(in1 or in2)
begin
	result[31] =  in1[31] ^ in2[31];
	result[30:23] = in1[30:23] + in2[30:23] - 127;
	temp = (24'h800000 + in1[22:0]) * ( 24'h800000 + in2[22:0]); 

	if ( temp[47] == 1)
	begin
		result[22:0] = temp[46:24];
		result[30:23] = result[30:23] + 1;
	end
	else
		result[22:0] = temp[45:23];
end

endmodule 

