$sum=0 #defines sum
1..1000 | %{if ($_%3 -eq 0 -or $_%5 -eq 0){$sum+=$_}} #iterates thru all integers 1-1000 and adds them if they are divisible by either 3 or 5
