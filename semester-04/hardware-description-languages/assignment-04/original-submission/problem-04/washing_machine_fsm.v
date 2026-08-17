module machine(start, enter_pipe_pomp, exit_pipe_water, motor, dryer, lock);
	input start, enter_pipe_pomp, exit_pipe_water, motor, dryer;
	output reg lock;
	reg [1:0] state;
	`define OFF 2'b00
	`define CLEAN 2'b01
	`define DRY 2'b10
	always@(start, enter_pipe_pomp, exit_pipe_water, motor, dryer)
		begin
			case(state)
				`OFF: if(start) state = `CLEAN;
				`CLEAN: if(exit_pipe_water) state = `DRY;
				`DRY: if(dryer == 1'b0) state = `OFF;
				default: state = `DRY;
			endcase
		end
	always@(state)
		begin
			if (state == `OFF) lock = 1'b0;
			if (state == `CLEAN) lock = 1'b1;
			if (state == `DRY) lock = 1'b1;
		end
endmodule
