module test_factorial;
    integer k;
    function [15:0] factorial;
        input [3:0] number;
        reg [15:0] ans;
        begin
		ans = 1;
        	for (k = 1; k <= number; k = k + 1) 
    			begin
        			ans = ans * k;
    			end
    
		factorial = ans;
    	  end
    endfunction
    reg [3:0] number;
    reg [15:0] ans;    
	initial 
		begin
			#200 number = 3;
        		ans = factorial(number);
        		$display("answer = %d", ans);
    		end
	initial 
		begin
            	#300 number = 4;
        		ans = factorial(number);
        		$display("answer = %d", ans);
    		end
	initial 
		begin
        		#400 number = 5;
        		ans = factorial(n);
        		$display("answer = %d", ans);
    		end
endmodule