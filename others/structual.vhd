library IEEE;
use IEEE.std_logic_1164.all;
library unisim;
use unisim.vcomponents.all;

entity full_adder is
port(
	X,Y,CIN:in STD_LOGIC;
	S,COUT:out STD_LOGIC;
	);
end full_adder;

architecture full_adder_arch of full_adder is
signal X_xor_Y,X_CIN,Y_CIN,X_Y:STD_LOGIC;
component XOR2 port (|0,|1:in STD_LOGIC;O:out STD_LOGIC); end component;
component AND2 port(|0,|1:in STD_LOGIC;O:out STD_LOGIC); end component;
component OR3 port(|0,|1,|2:in STD_LOGIC;O:STD_LOGIC); end component;
begin
	U1:XOR2 port map(X,Y,X_xor_Y);
	U2:AND2 port map(X,CIN,X_CIN);
	U3:AND2 port map(Y,CIN,Y_CIN);
	U4:AND2 port map(X,Y,X_Y);
	U5:XOR2 port map(X_xor_Y,CIN,S);
	U6:OR3 port map(X_CIN,Y_CIN,X_Y);
end full_adder_arch