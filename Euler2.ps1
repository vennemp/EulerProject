function Fibonacci ($limit)
{
$sum = 0
$current = $previous = 1
while ($current -lt $limit)
    {
    $current,$previous = ($current+$previous),$current
    if ($current % 2 -eq 0)
    {$sum += $current}
}
return $sum
}
Fibonacci 4000000
