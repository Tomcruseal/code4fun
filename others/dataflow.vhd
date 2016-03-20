architecture full_adder2_arch of full_adder is
signal X_xor_Y,X_CIN,Y_CIN,X_Y:STD_LOGIC;
begin
	X_xor_Y <= X xor Y;
	X_CIN <=X and CIN;
	Y_CIN <=Y and CIN;
	X_Y <= X and Y;
	S <=X_xor_Y xor CIN;
	COUT <=X_CIN or Y_CIN or X_Y;
end full_adder2_arch;