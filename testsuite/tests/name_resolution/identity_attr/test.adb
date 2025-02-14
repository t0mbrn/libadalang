with Ada.Exceptions; use Ada.Exceptions;
with Ada.Task_Identification; use Ada.Task_Identification;

procedure Test is
   task T;
   task body T is
   begin
      null;
   end T;

   task type TT;
   task body TT is
   begin
      null;
   end TT;

   X : TT;
   X_Array : array (1 .. 10) of T;
begin
   if T'Identity = X'Identity then
      null;
   end if;
   pragma Test_Statement_UID;

   if Constraint_Error'Identity = Constraint_Error'Identity then
      null;
   end if;
   pragma Test_Statement_UID;

   --  Should also work on ForLoopVarDecl
   for I of X_Array loop
      if I'Identity = Ada.Task_Identification.Current_Task then
         null;
      end if;
      pragma Test_Statement_UID;
   end loop;
end Test;
