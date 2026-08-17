module CORDIC(cosine, sine, angle);

  parameter width = 16;

  // Inputs
  reg [width-1:0] x_start = 16'b0100101111100101;
  reg [width-1:0] y_start = 0; 
  input signed [31:0] angle;

  // Outputs
  output signed  [width-1:0] sine, cosine;

  // Generate table of atan values
  wire signed [31:0] atan_table [0:30];
                          
  assign atan_table[00] = 'b00100000000000000000000000000000; // 45.000 degrees -> atan(2^0)
  assign atan_table[01] = 'b00010010111001000000010100011101; // 26.565 degrees -> atan(2^-1)
  assign atan_table[02] = 'b00001001111110110011100001011011; // 14.036 degrees -> atan(2^-2)
  assign atan_table[03] = 'b00000101000100010001000111010100; // atan(2^-3)
  assign atan_table[04] = 'b00000010100010110000110101000011;
  assign atan_table[05] = 'b00000001010001011101011111100001;
  assign atan_table[06] = 'b00000000101000101111011000011110;
  assign atan_table[07] = 'b00000000010100010111110001010101;
  assign atan_table[08] = 'b00000000001010001011111001010011;
  assign atan_table[09] = 'b00000000000101000101111100101110;
  assign atan_table[10] = 'b00000000000010100010111110011000;
  assign atan_table[11] = 'b00000000000001010001011111001100;
  assign atan_table[12] = 'b00000000000000101000101111100110;
  assign atan_table[13] = 'b00000000000000010100010111110011;
  assign atan_table[14] = 'b00000000000000001010001011111001;
  assign atan_table[15] = 'b00000000000000000101000101111100;
  assign atan_table[16] = 'b00000000000000000010100010111110;
  assign atan_table[17] = 'b00000000000000000001010001011111;
  assign atan_table[18] = 'b00000000000000000000101000101111;
  assign atan_table[19] = 'b00000000000000000000010100010111;
  assign atan_table[20] = 'b00000000000000000000001010001011;
  assign atan_table[21] = 'b00000000000000000000000101000101;
  assign atan_table[22] = 'b00000000000000000000000010100010;
  assign atan_table[23] = 'b00000000000000000000000001010001;
  assign atan_table[24] = 'b00000000000000000000000000101000;
  assign atan_table[25] = 'b00000000000000000000000000010100;
  assign atan_table[26] = 'b00000000000000000000000000001010;
  assign atan_table[27] = 'b00000000000000000000000000000101;
  assign atan_table[28] = 'b00000000000000000000000000000010;
  assign atan_table[29] = 'b00000000000000000000000000000001;
  assign atan_table[30] = 'b00000000000000000000000000000000;
  
  
  parameter An = 16'b0100101111100101;
  reg signed [width:0] x [0:width-1];
  reg signed [width:0] y [0:width-1];
  reg signed    [31:0] z [0:width-1];


  // make sure rotation angle is in -pi/2 to pi/2 range
  wire [1:0] quadrant;
  assign quadrant = angle[31:30];

  always @(angle)
  begin // make sure the rotation angle is in the -pi/2 to pi/2 range
    case(quadrant)
      2'b00,
      2'b11: // no changes needed for these quadrants
      begin
        x[0] <= x_start;
        y[0] <= y_start;
        z[0] <= angle;
      end

      2'b01:
      begin
        x[0] <= -y_start;
        y[0] <= x_start;
        z[0] <= {2'b00,angle[29:0]}; // subtract pi/2 for angle in this quadrant
      end

      2'b10:
      begin
        x[0] <= y_start;
        y[0] <= -x_start;
        z[0] <= {2'b11,angle[29:0]}; // add pi/2 to angles in this quadrant
      end
    endcase
	x_start = An;     // Xout = 32000*cos(angle)
    y_start = 0;      // Yout = 32000*sin(angle)
  end


  // run through iterations
  genvar i;

  generate
  for (i=0; i < (width-1); i=i+1)
  begin: xyz
    wire z_sign;
    wire signed [width:0] x_shr, y_shr;

    assign x_shr = x[i] >>> i; // signed shift right
    assign y_shr = y[i] >>> i;

    //the sign of the current rotation angle
    assign z_sign = z[i][31];

    always @(x_shr or y_shr)
    begin
      // add/subtract shifted data
      x[i+1] <= z_sign ? x[i] + y_shr : x[i] - y_shr;
      y[i+1] <= z_sign ? y[i] - x_shr : y[i] + x_shr;
      z[i+1] <= z_sign ? z[i] + atan_table[i] : z[i] - atan_table[i];
    end
  end
  endgenerate

  // assign output
  assign cosine = x[width-1];
  assign sine = y[width-1];

endmodule


/*//CORDIC Testbench for sine and cosine for Final Project 

//Claire Barnes

module CORDIC_TESTBENCH;

  localparam width = 16; //width of x and y

  // Inputs
  //reg [width-1:0] Xin, Yin;
  reg [31:0] angle;
  //reg signed [63:0] i;

  wire [width-1:0] COSout, SINout;

  //localparam An = 32000/1.647;
	
  initial begin

   // Test 1                                        
    angle = 'b00000000000000000000000000000000;

#100;
    // Test 2
    // #10000
    angle = 'b01000000000000000000000000000000; // 90 deg
#100;
    // Test 3
    // #10000
    angle = 'b00110101010101010101010101010101; // 75 deg

	
	#100;
	angle = 'b01101010101010101011000000000000; // 150 deg

	#100;
	angle = 'b00101010101010101010101010101010;//60
	#100;
	angle = 'b01010101010101010101010101010101; // 120 deg
	#100;
	angle = 'b00010101010101010101000000000000;//30 deg
	


  end

  CORDIC TEST_RUN(COSout, SINout, angle);

  // Monitor the output
  initial
  $monitor($time, , COSout, , SINout, , angle);

endmodule*/



