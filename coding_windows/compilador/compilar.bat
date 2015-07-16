rd /s /q dist && rd /s /q build

if not exist print_textos.py (
    copy ..\print_textos.py .
)

python setup.py py2exe 
