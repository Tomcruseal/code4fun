library IEEE
use IEEE.std_logic_1164.all
entity M35Det is 
	port(N:in STD_LOGIC_Vector(5 downto 0);
		Ms,M5:out STD_LOGIC;)
end M35Det;
architecture M35Det_arch of M35Det is
function CONV_INTEGER(x:STD_LOGIC_Vector) return INTEGER is
variable RESULT :=INTEGER;
begin
RESULT:=0
for i in x's range loop
	RESULT:=RESULT*2;
	case x(i) is
		when '0'|'L'=>null;
		when '1'|'H'=>RESULT:=RESULT+1;
		when others=>null;
		end case;
	end loop;
return RESULT;
end CONV_INTEGER;
begin
process(N)
variable NI:INTEGER;
begin
NI:=CONV_INTEGER(N);
if NI mod 3 then M3 <='1';
else M3<='0';
end if;
if NI mod 5 then M5 <='1';
else M5<='0';
end if;
end process;
end M35Det_arch;
	
