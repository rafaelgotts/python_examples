@REM Exemplos code page
@REM call_print.bat

@CLS
@PROMPT $

@ECHO EXEMPLO COM CODEPAGE PADRAO "850"
@print_textos.py


@ECHO.
@CHCP 1252 > NUL
@ECHO.

@ECHO EXEMPLO COM CODEPAGE LATIN1 "1252"
@print_textos.py

@PROMPT