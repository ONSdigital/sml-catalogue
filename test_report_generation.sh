echo "Generating Reports"

set -e

echo "Creating report directory"
cd features/test_reports
date=$(date '+%Y_%m_%d_%H_%M_%S')

echo $date
mkdir $date

echo "cd to directory"
cd $date

echo Create reports
behave --junit

echo "Create overview report"
junit2html ./reports/ --merge reports/report.xml
junit2html ./reports/report.xml reports/report.html

echo "Remove junk files"
cd ./reports
find . -name "*.xml" -type f|xargs rm -f

echo Push to branch
git add .
git commit -m "Test report update"
git push