<?php

echo "WELCOME TO SIVA";

$db = mysqli_connect("localhost","root","draco","siva");

if (mysqli_connect_errno()) {
    echo 'Could not connect to mysql';
    exit;
}
$result = mysqli_query($db,"SELECT * FROM ean13Barcodes");

echo "<table border='1'>
<tr>
<th>ID</th>
<th>barcode</th>
<th>Name</th>
</tr>";

while($row = mysqli_fetch_array($result)) {
  echo "<tr>";
  echo "<td>" . $row['id'] . "</td>";
  echo "<td>" . $row['barcode'] . "</td>";
  echo "<td>" . $row['name'] . "</td>";
  echo "</tr>";
}

echo "</table>";


echo $result;
echo "OKs";

?>
