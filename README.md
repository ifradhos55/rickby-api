


#!/bin/bash

# Create department directories
mkdir /Engineering /Sales /IS

# Create groups
groupadd engineering
groupadd sales
groupadd is

# Create users for Engineering
useradd -m -s /bin/bash -g engineering eng_admin
useradd -m -s /bin/bash -g engineering eng_user1
useradd -m -s /bin/bash -g engineering eng_user2

# Create users for Sales
useradd -m -s /bin/bash -g sales sales_admin
useradd -m -s /bin/bash -g sales sales_user1
useradd -m -s /bin/bash -g sales sales_user2

# Create users for IS
useradd -m -s /bin/bash -g is is_admin
useradd -m -s /bin/bash -g is is_user1
useradd -m -s /bin/bash -g is is_user2

# Set ownership and permissions for Engineering
chown eng_admin:engineering /Engineering
chmod 2770 /Engineering

# Set ownership and permissions for Sales
chown sales_admin:sales /Sales
chmod 2770 /Sales

# Set ownership and permissions for IS
chown is_admin:is /IS
chmod 2770 /IS

# Create confidential file for Engineering
echo "This file contains confidential information for the department." > /Engineering/confidential.txt
chown eng_admin:engineering /Engineering/confidential.txt
chmod 640 /Engineering/confidential.txt

# Create confidential file for Sales
echo "This file contains confidential information for the department." > /Sales/confidential.txt
chown sales_admin:sales /Sales/confidential.txt
chmod 640 /Sales/confidential.txt

# Create confidential file for IS
echo "This file contains confidential information for the department." > /IS/confidential.txt
chown is_admin:is /IS/confidential.txt
chmod 640 /IS/confidential.txt

# Verification commands
echo "Verifying users and groups..."
getent passwd eng_admin
getent group engineering
id eng_user1

echo "Verifying directory permissions..."
ls -ld /Engineering /Sales /IS

echo "Verifying confidential files..."
ls -l /Engineering/confidential.txt
ls -l /Sales/confidential.txt
ls -l /IS/confidential.txt


**************

# Question 1: Create directories
mkdir ../Exam
mkdir ../Exam/business
mkdir ../Exam/tunes
mkdir ../Exam/book
mkdir ../Exam/temp

# Question 2: Create files
touch ../Exam/tunes/music.mp3
touch ../Exam/tunes/tunes.wav
touch ../Exam/book/sueletters.txt
touch ../Exam/book/list.txt

# Question 3: Copy and move files
cp ../Exam/book/sueletters.txt ../Exam/business/
cp ../Exam/book/list.txt ../Exam/business/
mv ../Exam/tunes/*.mp3 ../Exam/business/
mv ../Exam/tunes/*.wav ../Exam/business/

# Question 4: Copy and remove files
cp ../Exam/business/* ../Exam/temp/
rm ../Exam/temp/*.txt

# Question 5: Rename a file
mv ../Exam/temp/music.mp3 ../Exam/temp/sue.mp3

# Question 6: Move a directory
mv ../Exam/business ../Exam/book/

# Question 7: Use grep to find lines
grep 'false$' /etc/passwd

# Question 8: Bash script to archive a file
#!/bin/bash

# Prompt for the file name
echo "Enter the name of the file:"
read filename

# Check if the file exists
if [ ! -f "$filename" ]; then
    echo "no such file $filename, end of line"
    exit 3
fi

# Get the current date
current_date=$(date +%F)

# Create the archive file name
archive_name="${filename}-${current_date}.tar.gz"

# Create the compressed tar archive
tar -czf "$archive_name" "$filename"

# Print a success message
echo "Job complete"
