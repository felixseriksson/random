if exist %1 (
echo. && echo. && echo ---------------------------------------------------- && echo. && echo That name is occupied, please retry with another. && echo. && echo ----------------------------------------------------
exit /b
)

mkdir %1
cd %1

mkdir .vscode
cd .vscode

(
echo {
echo     "configurations": [
echo         {
echo             "name": "Win32",
echo             "includePath": [
echo                 "${workspaceFolder}/**"
echo             ],
echo             "defines": [
echo                 "_DEBUG",
echo                 "UNICODE",
echo                 "_UNICODE"
echo             ],
echo             "compilerPath": "C:\\MinGW\\bin\\gcc.exe",
echo             "cStandard": "c11",
echo             "cppStandard": "c++17",
echo             "intelliSenseMode": "clang-x86"
echo         }
echo     ],
echo     "version": 4
echo }
) > c_cpp_properties.json

(
echo {
echo     "version": "2.0.0",
echo     "tasks": [
echo         {
echo             "label": "echo",
echo             "type": "shell",
echo             "command": "g++",
echo             "args": [
echo                 "-g",
echo                 "main.cpp"
echo             ],
echo             "group": {
echo                 "kind": "build",
echo                 "isDefault": true
echo             }
echo         },
echo         {
echo             "type": "shell",
echo             "label": "g++.exe build active file",
echo             "command": "C:\\MinGW\\bin\\g++.exe",
echo             "args": [
echo                 "-g",
echo                 "${file}",
echo                 "-o",
echo                 "${fileDirname}\\${fileBasenameNoExtension}.exe"
echo             ],
echo             "options": {
echo                 "cwd": "C:\\MinGW\\bin"
echo             }
echo         }
echo     ]
echo }
) > tasks.json

(
echo {
echo     // Use IntelliSense to learn about possible attributes.
echo     // Hover to view descriptions of existing attributes.
echo     // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
echo     "version": "0.2.0",
echo     "configurations": [
echo         {
echo             "name": "g++.exe - Build and debug active file",
echo             "type": "cppdbg",
echo             "request": "launch",
echo             "program": "${workspaceFolder}\\a.exe",
echo             "args": [],
echo             "stopAtEntry": false,
echo             "cwd": "${workspaceFolder}",
echo             "environment": [],
echo             "externalConsole": true,
echo             "MIMode": "gdb",
echo             "miDebuggerPath": "C:\\MinGW\\bin\\gdb.exe",
echo             "setupCommands": [
echo                 {
echo                     "description": "Enable pretty-printing for gdb",
echo                     "text": "-enable-pretty-printing",
echo                     "ignoreFailures": true
echo                 }
echo             ],
echo             "preLaunchTask": "echo"
echo         }
echo     ]
echo }
) > launch.json

cd..

(
echo #include ^<bits^/stdc^+^+^.h^>
echo using namespace std^;
echo typedef long long ll^;
echo ^#define rep^(i^,a^,b^) for ^(ll i ^= a^; i^<ll^(b^)^; i^+^+^)
echo ^/^/compile with g^+^+^/cc ^-g ^-Wall ^-Wconversion ^-fsanitize^=address^,
echo ^/^/undefined ^<filename^.cpp^>
echo int main^(^) ^{
echo     ios^:^:sync^_with^_stdio^(false^)^;
echo     cin^.tie^(NULL^)^; cout.tie^(NULL^)^;
echo     cout ^<^< setprecision^(10^)^;
echo.
echo     StartTypingHere
echo.
echo ^}
) > main.cpp

cd..

echo. && echo. && echo -------------------------------------------------------------------------------- && echo. && echo Initiated directory containing necessary files for C++ program called %1. && echo. && echo --------------------------------------------------------------------------------