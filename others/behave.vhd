architecture full_adder3_arch of full_adder is
begin
	process(X,Y,CIN)
		variable X_xor_Y,X_CIN,Y_CIN,X_Y:STD_LOGIC;
	begin
		X_xor_Y := X xor Y;
		X_CIN :=X and CIN;
		Y_CIN := Y and CIN;
		X_Y := X and Y;
		S <=X_xor_Y xor CIN;
		COUT <=X_CIN xor Y_CIN xor X_Y;
	end process;
end full_adder3_arch;
