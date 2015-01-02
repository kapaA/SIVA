<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="shortcut icon" type="image/ico" href="http://www.datatables.net/favicon.ico">
	<meta name="viewport" content="initial-scale=1.0, maximum-scale=2.0">

	<title>Siva Logistics</title>
	<link rel="stylesheet" type="text/css" href="media/css/jquery.dataTables.css">
	<link rel="stylesheet" type="text/css" href="resources/syntax/shCore.css">
	<link rel="stylesheet" type="text/css" href="resources/demo.css">
	<style type="text/css" class="init">

	</style>
	<script type="text/javascript" language="javascript" src="media/js/jquery.js"></script>
	<script type="text/javascript" language="javascript" src="media/js/jquery.dataTables.js"></script>
	<script type="text/javascript" language="javascript" src="resources/syntax/shCore.js"></script>
	<script type="text/javascript" language="javascript" src="resources/demo.js"></script>
	<script type="text/javascript" language="javascript" class="init">

$(document).ready(function() {
	$('#example').dataTable();
} );

	</script>
</head>

<body class="dt-example">
	<div class="container">
		<section>
			<h1>Siva: <span>Logistics</span></h1>

			<table id="example" class="display" cellspacing="0" width="100%">
				<thead>
					<tr>
						<th>Name</th>
						<th>Quantity</th>
		                                <th>Expiry Date</th>
						<th>Main Category</th>
						<th>Sub Category</th>
						<th>Barcode</th>
					</tr>
				</thead>

				<tfoot>
					<tr>
						<th>Name</th>
						<th>Quantity</th>
		                                <th>Expiry Date</th>
						<th>Main Category</th>
						<th>Sub Category</th>
						<th>Barcode</th>
					</tr>
				</tfoot>

				<tbody>
					<?php
                                        

$db = mysqli_connect("localhost","root","draco","siva");

if (mysqli_connect_errno()) {
    echo 'Could not connect to mysql';
    exit;
}
$result = mysqli_query($db,"SELECT * FROM ean13Barcodes");



while($row = mysqli_fetch_array($result)) {
  echo "<tr>";
  echo "<td> <a href=\"google.com\"> </a>" . $row['name'] . "</td>";
  echo "<td>" . $row['quantity'] . "</td>";
  echo "<td>" . $row['expiryDate'] . "</td>"; 
  echo "<td>" . $row['mainCategory'] . "</td>";
  echo "<td>" . $row['subCategory'] . "</td>";
  echo "<td>" . $row['barcode'] . "</td>";
  //echo "<td>" . $row['id'] . "</td>";
  
   

  echo "</tr>";
}




					
					
					

?>
					
				</tbody>
			</table>

			
		</section>
	</div>

</body>
</html>
