for /f "tokens=*" %%a in ('dir /ad /b') do git --git-dir=%%a/.git --work-tree=%%a status