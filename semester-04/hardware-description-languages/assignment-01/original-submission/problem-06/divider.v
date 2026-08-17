module divider(adad, maghsoom_e, baghi, javab);
	input [7:0] adad;
	input [7:0] maghsoom_e;
	output reg [3:0] baghi;
	output reg [7:0] javab;
	integer k, t;
	always@ (adad or maghsoom_e)
		begin
			if( 0 < maghsoom_e &&  maghsoom_e < 9)
				begin
					k = 0;
					t = adad;
					while(t > maghsoom_e)
						begin
							t = t - maghsoom_e;
							k = k + 1;
						end
					javab = k;
					baghi = t;
				end
			else $display("Invalid!!!!");
		end
endmodule
