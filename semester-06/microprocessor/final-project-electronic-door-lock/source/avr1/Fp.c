/*******************************************************
This program was created by the
CodeWizardAVR V3.14 Advanced
Automatic Program Generator
© Copyright 1998-2014 Pavel Haiduc, HP InfoTech s.r.l.
http://www.hpinfotech.com

Project : 
Version : 
Date    : 5/31/2024
Author  : 
Company : 
Comments: 


Chip type               : ATmega32
Program type            : Application
AVR Core Clock frequency: 8.000000 MHz
Memory model            : Small
External RAM size       : 0
Data Stack size         : 512
*******************************************************/

#include <mega32.h>
#include <delay.h>
#include <stdio.h>
// Alphanumeric LCD functions
#include <alcd.h>

// Declare your global variables here
char i, state, result, counter = 0;
int x = -1, flag = 0, index_array = 1;
int match_main_pass = 1;
int match_main_pass1 = 1;
int match_main_pass2 = 1;
char shift[4] = {0xFE, 0xFD, 0xFB, 0xF7};
char user_pass[4] = {'', '', '', ''};
char main_pass2[4] = {'', '', '' , ''};
char main_pass1[4] = {'', '', '' , ''};
char main_pass[4] = {'0', '0', '0', '0'};
char key[16] = {'7', '8', '9', '/', '4', '5', '6', '*', '1', '2', '3', '-', '', '0', '=', '+'};

void check_password(void){
     result = 1;
     for(i = 0; i <= 3; i++){
        if(main_pass[i] != user_pass[i]){
            result = 0;
        } 
     } 
     if(result == 0){
        int entered_if = 0;
        for(i = 0; i <= 3; i++){
            if(main_pass1[i] != user_pass[i]){
                result = 0;
                entered_if = 1;
            } 
        }
        if(!entered_if){
            result = 1;
        }
     }
     if(result == 0){
        int entered_if_1 = 0; 
        for(i = 0; i <= 3; i++){
            if(main_pass2[i] != user_pass[i]){
                result = 0; 
                entered_if_1 = 1;
            } 
        }
        if(!entered_if_1){
            result = 1;
        }
     }  
     if(result == 1){
        lcd_clear();
        lcd_puts("pass is right");
        counter = 0;
        PORTD.2 = 1;
        delay_ms(200);
        PORTD.2 = 0; 
        lcd_clear();
        if(flag == 0){
            lcd_puts("Enter password: ");
         }
     } 
     else{
        lcd_clear();
        lcd_puts("pass is wrong");
        counter++; 
        PORTD.3 = 1;
        delay_ms(200);
        PORTD.3 = 0;
        if(counter == 3)
        {
            for( i = 0; i < 7; i++){
                PORTD.4 = 1;
                delay_ms(20);
                PORTD.4 = 0;
                delay_ms(20);
                PORTC.0 = 1;
                delay_ms(20);
                PORTC.0 = 0;
                delay_ms(20);
            } 
            counter = 0;    
        }
        
        lcd_clear();
        if(flag == 0){
            lcd_puts("Enter password:");
            lcd_gotoxy(0, 1);
        }
        else if(flag == 1){
            lcd_puts("Enter c pass:");
            lcd_gotoxy(0, 1);
        }    
            
     }
}

void read_keypad(void){
    
    for( i = 0; i <= 3; i++)
      {
        PORTB = shift[i];
        if(PINB.4 == 0)
        {   
            delay_ms(15);
            if(PINB.4 == 0)
            x = 0;
        } 
        if(PINB.5 == 0)
        {
            delay_ms(15);
            if(PINB.5 == 0)
            x = 1;
        }
        if(PINB.6 == 0)
        {
            delay_ms(15);
            if(PINB.6 == 0)
            x = 2;
        }
        if(PINB.7 == 0)
        {
           delay_ms(15);
            if(PINB.7 == 0)
            x = 3;
        }  
        
        if( x != -1)
        {   
            if( i == 3 && PINB.4 == 0){
                lcd_clear();
                lcd_puts("Enter password: ");
                flag = 0;
                state = 0;
            }  
            else if(i == 3 && PINB.7 == 0){
                if(index_array <= 2){
                    lcd_clear();
                    flag = 1;
                    lcd_puts("Enter c pass:");
                    lcd_gotoxy(0, 1);
                }
                else{
                    lcd_clear();
                    lcd_puts("no space.");
                    delay_ms(200);
                    lcd_clear();
                    lcd_puts("Enter password:");
                    lcd_gotoxy(0, 1);
                }
            }
            else if(i == 0 && PINB.7 == 0){
                flag = 3;
                lcd_clear();
                lcd_puts("Enter first pass"); 
                
            
            
            }
            else{                         
                lcd_putchar('*');  
                user_pass[state++] = key[i * 4 + x];
                
                if(state == 4){
                    if(flag == 0){
                        check_password();
                        state = 0;
                    } 
                    else if(flag == 1){
                            
                        check_password();
                        if(result == 1){
                        lcd_puts("Enter new pass:");
                        lcd_gotoxy(0, 1);   
                        flag = 2;                  
                        //x = -1;
                        //read_keypad();
                        }
                    
                        state = 0;
                    }
                    else if(flag == 2){
                        if(index_array == 1){
                            for(i = 0; i < 4; i++){
                                main_pass1[i] = user_pass[i];
                            }      
                            index_array++;
                            state = 0; 
                            lcd_clear();
                            lcd_puts("new pass added.");
                            delay_ms(200);
                            lcd_clear();
                            flag = 0; 
                            lcd_puts("Enter password:");
                            lcd_gotoxy(0, 1);
                            state = 0;   
                        } 
                        else if(index_array == 2){
                            for(i = 0; i < 4; i++){
                                main_pass2[i] = user_pass[i];
                            }   
                            index_array++;
                            state = 0;
                            lcd_clear();
                            lcd_puts("new pass added.");
                            delay_ms(200);
                            lcd_clear();
                            flag = 0; 
                            lcd_puts("Enter password:");
                            lcd_gotoxy(0, 1); 
                            state = 0;
                        }
                        
                    }
                    else if(flag == 3){
                        
                        match_main_pass = 1;
                        match_main_pass1 = 1;
                        match_main_pass2 = 1;
                        
                        for(i = 0; i < 4; i++){
                            if(main_pass[i] != user_pass[i])
                                match_main_pass = 0; 
                        }      
                        for(i = 0; i < 4; i++){
                            if(main_pass1[i] != user_pass[i])
                                match_main_pass1 = 0;

                        }      
                        for(i = 0; i < 4; i++){
                            if(main_pass2[i] != user_pass[i])
                                match_main_pass2 = 0; 
                        }     
                        if(!match_main_pass && !match_main_pass1 && !match_main_pass2){
                            lcd_clear();
                            lcd_puts("No matching");
                            delay_ms(200);
                            lcd_clear();
                            lcd_puts("Enter first pass");
                            lcd_gotoxy(0, 1); 
                            state = 0;
                        }
                        else{
                            lcd_clear();
                            lcd_puts("Enter sec pass:");
                            lcd_gotoxy(0, 1);
                            flag = 4;
                            state = 0;
                        
                        }    
                    
                    }
                    else if(flag == 4){
                        if(match_main_pass){
                            for(i = 0; i < 4; i++){
                                main_pass[i] = user_pass[i];
                            }
                        }
                        else if(match_main_pass1){
                            for(i = 0; i < 4; i++){
                                main_pass1[i] = user_pass[i];
                            }
                        }  
                        else if(match_main_pass2){
                            for(i = 0; i < 4; i++){
                                main_pass2[i] = user_pass[i];
                            }
                        }
                        flag = 0;
                        lcd_clear();
                        lcd_puts("Enter password:"); 
                        lcd_gotoxy(0, 1);   
                        state = 0;
                    }

                }
            }
            x = -1;
        }
      }
}

void insert_password(void){
    check_password();
    if(result == 1){
        lcd_puts("Enter new pass:");
        lcd_gotoxy(0, 1);
        read_keypad();
    }
}


void main(void)
{
// Declare your local variables here

// Input/Output Ports initialization
// Port A initialization
// Function: Bit7=In Bit6=In Bit5=In Bit4=In Bit3=In Bit2=In Bit1=In Bit0=In 
DDRA=(0<<DDA7) | (0<<DDA6) | (0<<DDA5) | (0<<DDA4) | (0<<DDA3) | (0<<DDA2) | (0<<DDA1) | (0<<DDA0);
// State: Bit7=T Bit6=T Bit5=T Bit4=T Bit3=T Bit2=T Bit1=T Bit0=T 
PORTA=(0<<PORTA7) | (0<<PORTA6) | (0<<PORTA5) | (0<<PORTA4) | (0<<PORTA3) | (0<<PORTA2) | (0<<PORTA1) | (0<<PORTA0);

// Port B initialization
// Function: Bit7=In Bit6=In Bit5=In Bit4=In Bit3=Out Bit2=Out Bit1=Out Bit0=Out 
DDRB=(0<<DDB7) | (0<<DDB6) | (0<<DDB5) | (0<<DDB4) | (1<<DDB3) | (1<<DDB2) | (1<<DDB1) | (1<<DDB0);
// State: Bit7=P Bit6=P Bit5=P Bit4=P Bit3=0 Bit2=0 Bit1=0 Bit0=0 
PORTB=(1<<PORTB7) | (1<<PORTB6) | (1<<PORTB5) | (1<<PORTB4) | (0<<PORTB3) | (0<<PORTB2) | (0<<PORTB1) | (0<<PORTB0);

// Port C initialization
// Function: Bit7=In Bit6=In Bit5=In Bit4=In Bit3=In Bit2=In Bit1=In Bit0=In 
DDRC=(0<<DDC7) | (0<<DDC6) | (0<<DDC5) | (0<<DDC4) | (0<<DDC3) | (0<<DDC2) | (0<<DDC1) | (1<<DDC0);
// State: Bit7=T Bit6=T Bit5=T Bit4=T Bit3=T Bit2=T Bit1=T Bit0=T 
PORTC=(0<<PORTC7) | (0<<PORTC6) | (0<<PORTC5) | (0<<PORTC4) | (0<<PORTC3) | (0<<PORTC2) | (0<<PORTC1) | (0<<PORTC0);

// Port D initialization
// Function: Bit7=In Bit6=In Bit5=In Bit4=In Bit3=In Bit2=In Bit1=In Bit0=In 
DDRD=(0<<DDD7) | (0<<DDD6) | (0<<DDD5) | (1<<DDD4) | (1<<DDD3) | (1<<DDD2) | (1<<DDD1) | (0<<DDD0);
// State: Bit7=T Bit6=T Bit5=T Bit4=T Bit3=T Bit2=T Bit1=T Bit0=T 
PORTD=(0<<PORTD7) | (0<<PORTD6) | (0<<PORTD5) | (0<<PORTD4) | (0<<PORTD3) | (0<<PORTD2) | (0<<PORTD1) | (0<<PORTD0);

// Timer/Counter 0 initialization
// Clock source: System Clock
// Clock value: Timer 0 Stopped
// Mode: Normal top=0xFF
// OC0 output: Disconnected
TCCR0=(0<<WGM00) | (0<<COM01) | (0<<COM00) | (0<<WGM01) | (0<<CS02) | (0<<CS01) | (0<<CS00);
TCNT0=0x00;
OCR0=0x00;

// Timer/Counter 1 initialization
// Clock source: System Clock
// Clock value: Timer1 Stopped
// Mode: Normal top=0xFFFF
// OC1A output: Disconnected
// OC1B output: Disconnected
// Noise Canceler: Off
// Input Capture on Falling Edge
// Timer1 Overflow Interrupt: Off
// Input Capture Interrupt: Off
// Compare A Match Interrupt: Off
// Compare B Match Interrupt: Off
TCCR1A=(0<<COM1A1) | (0<<COM1A0) | (0<<COM1B1) | (0<<COM1B0) | (0<<WGM11) | (0<<WGM10);
TCCR1B=(0<<ICNC1) | (0<<ICES1) | (0<<WGM13) | (0<<WGM12) | (0<<CS12) | (0<<CS11) | (0<<CS10);
TCNT1H=0x00;
TCNT1L=0x00;
ICR1H=0x00;
ICR1L=0x00;
OCR1AH=0x00;
OCR1AL=0x00;
OCR1BH=0x00;
OCR1BL=0x00;

// Timer/Counter 2 initialization
// Clock source: System Clock
// Clock value: Timer2 Stopped
// Mode: Normal top=0xFF
// OC2 output: Disconnected
ASSR=0<<AS2;
TCCR2=(0<<PWM2) | (0<<COM21) | (0<<COM20) | (0<<CTC2) | (0<<CS22) | (0<<CS21) | (0<<CS20);
TCNT2=0x00;
OCR2=0x00;

// Timer(s)/Counter(s) Interrupt(s) initialization
TIMSK=(0<<OCIE2) | (0<<TOIE2) | (0<<TICIE1) | (0<<OCIE1A) | (0<<OCIE1B) | (0<<TOIE1) | (0<<OCIE0) | (0<<TOIE0);

// External Interrupt(s) initialization
// INT0: Off
// INT1: Off
// INT2: Off
MCUCR=(0<<ISC11) | (0<<ISC10) | (0<<ISC01) | (0<<ISC00);
MCUCSR=(0<<ISC2);

// USART initialization
// USART disabled
UCSRB=(0<<RXCIE) | (0<<TXCIE) | (0<<UDRIE) | (0<<RXEN) | (0<<TXEN) | (0<<UCSZ2) | (0<<RXB8) | (0<<TXB8);

// Analog Comparator initialization
// Analog Comparator: Off
// The Analog Comparator's positive input is
// connected to the AIN0 pin
// The Analog Comparator's negative input is
// connected to the AIN1 pin
ACSR=(1<<ACD) | (0<<ACBG) | (0<<ACO) | (0<<ACI) | (0<<ACIE) | (0<<ACIC) | (0<<ACIS1) | (0<<ACIS0);
SFIOR=(0<<ACME);

// ADC initialization
// ADC disabled
ADCSRA=(0<<ADEN) | (0<<ADSC) | (0<<ADATE) | (0<<ADIF) | (0<<ADIE) | (0<<ADPS2) | (0<<ADPS1) | (0<<ADPS0);

// SPI initialization
// SPI disabled
SPCR=(0<<SPIE) | (0<<SPE) | (0<<DORD) | (0<<MSTR) | (0<<CPOL) | (0<<CPHA) | (0<<SPR1) | (0<<SPR0);

// TWI initialization
// TWI disabled
TWCR=(0<<TWEA) | (0<<TWSTA) | (0<<TWSTO) | (0<<TWEN) | (0<<TWIE);

// Alphanumeric LCD initialization
// Connections are specified in the
// Project|Configure|C Compiler|Libraries|Alphanumeric LCD menu:
// RS - PORTA Bit 0
// RD - PORTA Bit 1
// EN - PORTA Bit 2
// D4 - PORTA Bit 4
// D5 - PORTA Bit 5
// D6 - PORTA Bit 6
// D7 - PORTA Bit 7
// Characters/line: 16
lcd_init(16);

lcd_puts("Enter password:");

lcd_gotoxy(0, 1);
while (1)
      {  
       
        read_keypad();

      }
}