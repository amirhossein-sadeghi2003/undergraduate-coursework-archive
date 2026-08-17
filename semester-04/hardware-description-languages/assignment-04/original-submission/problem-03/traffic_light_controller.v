module traffic_light(y1, y2, full_bozorgrah, full_masir, green_bozorgrah, yellow_bozorgrah, red_bozorgrah, green_masir, yellow_masir, red_masir);
  input y1 ,y2, full_bozorgrah, full_masir;
  output reg green_bozorgrah, yellow_bozorgrah, red_bozorgrah, green_masir, yellow_masir, red_masir;
  reg [5:0] state;
 `define YR 'b010100
 `define RG 'b100001
 `define GR 'b001100
 `define RY 'b100010
  always@ (full_bozorgrah or full_masir)     begin 
      case(state)
        `GR: if(full_masir) state = `YR;
        `YR: if(full_masir) state = `RG;
        `RG: if(full_bozorgrah) state = `RY;
        `RY: if(full_bozorgrah) state = `GR;
        default: state = `GR;
      endcase
    end
  always@ (state)
    begin
      if (state == `GR)
        begin
          green_bozorgrah = 1;
          yellow_bozorgrah = 0;
          red_bozorgrah = 0;
          green_masir = 0;
          yellow_masir = 0;
          red_masir = 1;
        end
      if (state == `RY)
        begin
          green_bozorgrah = 0;
          yellow_bozorgrah = 0;
          red_bozorgrah = 1;
          green_masir = 0;
          yellow_masir = 1;
          red_masir = 0;
          #y2 state = `GR;  
        end
      if (state == `YR)
        begin
          green_bozorgrah = 0;
          yellow_bozorgrah = 1;
          red_bozorgrah = 0;
          green_masir = 0;
          yellow_masir = 0;
          red_masir = 1;
          #y1 state = `RG;
        end
      if (state == `RG)
        begin
          green_bozorgrah = 0;
          yellow_bozorgrah = 0;
          red_bozorgrah = 1;
          green_masir = 1;
          yellow_masir = 0;
          red_masir = 0;
        end
    end
endmodule