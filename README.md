# sie-508_hw5

To test missing inventory file, uncomment os.remove(filename) on line 17 of basic_backend.py

To test empty inventory file, comment out items.append(row) on line 23 of basic_backend.py

All other methods run read_inv() which will fail if there is an error.
This seemed like the most efficient way to capture all possible errors.


