module log;
   integer k;
   integer temp;
   reg [15:0] t;
   reg [2:0] base_log;
   reg [4:0] ans;
   task log_int;
   	output reg [4:0] log;
   	begin
  		k = 0;
  		temp = t;
  		while( temp >= base_log) 
    			begin
				temp = temp / base_log;
				k = k + 1;
    			end
  		log = k;
  	end
   endtask  
   initial 
       begin
   	 	#150 t = 16'b1000000000000000; base_log = 3'b010;
       	log_int(ans);
       	$display("log(%d) base_log %d = %d", t, base_log, ans);
       	#150 t = 16'b0000000000001110; base_log = 3'b010;
       	log_int(ans);
       	$display("log(%d) base_log %d = %d", x, base_log, ans);
       	#150 t = 16'b0000000000000001; base_log = 3'b010;
       	log_int(ans);
       	$display("log(%d) base %d = %d", t, base_log, ans);    
       	#150 t = 16'b000000001000000; base_log = 3'b100;
       	log_int(ans);
       	$display("log(%d) base_log %d = %d", t, base_log, ans);
       	#150 t = 16'b1111111111111111; base_log = 3'b100; 
       	log_int(ans);
       	$display("log(%d) base_log %d = %d", t, base_log, ans); 
       	#200;
       end
endmodule
