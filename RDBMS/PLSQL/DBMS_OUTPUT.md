SET SERVEROUTPUT ON SIZE X;
SET SERVEROUTPUT calls the DBMSOUTPUT_ENABLE procedure with a default buffer size of 20k bytes and sets an internal flag in the CLP or CLPPlus. X is used to exceed the default

DBMS_OUTPUT.PUT_LINE() to print to output