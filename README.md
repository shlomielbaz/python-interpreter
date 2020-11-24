# Python Interpreter

This is my attempt to create a programing language iterpreter, the language called ALPL and the interpreter implemented in Python.
The program should get a script with extension "alpl" as a command-line argument and excute it,

In this stage the ALPL language contains 6 commands, the following is a description and rules of the language:
* The language only deals with positive or negative integer numbers
* There are ten registers numbered R0 - R9, each register can hold an integer number
* All the language tokens are in UPPERCASE
* Each line includes exactly one command or label, there are no multiline commands
* A label is an alphanumeric token followed by a colon (the token can’t be a command or a register name)
* When the program reaches the end of file it is ended
* List of commands:

| Name | Syntax | Description | Example |
|:--- |:---|:---|:---|
| LET| LET Rx := EXPRESSION1|Set a register to hold an expression result.| LET R4 := R5 * 12|
| IF| IF Rx OPERATOR2 Ry LABEL| Compare between two registers, If the expression is true jump to LABEL otherwise continue|IF R2 < R5 LABEL0|
| JUMP | JUMP LABEL | Jump to a label (no return)| JUMP LABEL12|
| CALL  | CALL LABEL | Call to a label, same as JUMP but can return | CALL DIV0|
| RETURN | RETURN | Return to the line after the last call| RETURN |
| PRINT| PRINT Rx| Print the value of a register | PRINT R7|

<ol>
  <li>
    The LET expression is composed of:
    <ul>
      <li>Left operand : register or integer</li>
      <li>Operator : + or * (plus or multiply) - optional</li>
      <li>Right operand: register or integer - required if operator exists</li>
    </ul>
  </li>
  <li>The IF operator can be : =, <, > (equal to, less than, greater than)</li>
</ol>
  
  
| Example program (count to 10): | Example program (print 2020): |
|:--- |:---|
| LET R0 := 0 | LET R5 := 2020 |
| LET R1 := 10 | CALL PRINTR5 |
| LOOP: JUMP END | IF R0 = R1 END PRINTR5: |
| LET R0 := R0 + 1 | PRINT R5 |
| JUMP LOOP | RETURN |
| END: | END: |

#### The solution includes the following scripts:
* `main.py` - the entry point and create the execution plan
* `lexer.py` - where we parse the source code and create execution tokens
* `statements.py` - where we initial the execution objects
* `executer.py` - where we execute the execution plan line by line
* `tracer.py` - where we set the tracer mode

#### Run scripts:
```python main.py FILE_NAME (ALPL code file)```


### shlomi.elbaz@outlook.com
