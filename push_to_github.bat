@echo off
echo.
echo ========================================
echo Checking Git Status...
echo ========================================

:: Ensure the remote origin is set correctly
git remote remove origin 2>nul
git remote add origin https://github.com/akashgarg98/Movie_agent

:: Show current remote
echo Your GitHub destination is:
git remote -v

echo.
echo ========================================
echo Preparing Files...
echo ========================================

:: Try to remove README.md from tracking (it's okay if this fails)
git rm --cached README.md 2>nul

:: Add the modified files
git add .gitignore whats_in_there.md push_to_github.bat

:: Commit the changes
git commit -m "Update gitignore, add explanation, and push script"

echo.
echo ========================================
echo Pushing to GitHub...
echo ========================================

:: Push to GitHub
git push origin main
if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [TRYING ALTERNATIVE BRANCH...]
    git push origin master
)

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo [ERROR] Push failed! 
    echo 1. Check if you have internet.
    echo 2. Check if you are logged into Git.
    echo 3. Check if the repository exists on GitHub.
) else (
    echo.
    echo ========================================
    echo SUCCESS! Your code has been pushed.
    echo ========================================
)

pause
