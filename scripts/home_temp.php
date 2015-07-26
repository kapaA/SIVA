<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<link rel="shortcut icon" type="image/ico" href="http://www.datatables.net/favicon.ico">
	<meta name="viewport" content="initial-scale=1.0, maximum-scale=2.0">

	<title>Home Temperature</title>
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
	
	<style type="text/css">
.auto-style1 {
	text-align: center;
}
</style>


</head>

<body class="dt-example">
	<div class="container">
		<section>
			<h1>Siva: <span>Home Temperature</span></h1>

			<table id="example" class="display" cellspacing="0" width="100%">
				<thead>
					<tr>
						<th>Location</th>
						<th>Temperature</th>
						<th>Days Online</th>
						<th>Battery status</th>
					</tr>
				</thead>

				<tfoot>
					<tr>
						<th>Location</th>
						<th>Temperature</th>
						<th>Days Online</th>
						<th>Battery status</th>
					</tr>
				</tfoot>

				<tbody>



<?php
	session_start();
	//Start session
	
	//Include database connection details
	require_once('config.php');
	
	//Array to store validation errors
	$errmsg_arr = array();
	
	//Validation error flag
	$errflag = false;
	
	//Connect to mysql server
	$link = mysql_connect(DB_HOST, DB_USER, DB_PASSWORD);
	if(!$link) {
		die('Failed to connect to server: ' . mysql_error());
	}
	
	//Select database
	$db = mysql_select_db(DB_DATABASE);
	if(!$db) {
		die("Unable to select database");
	}

	$livingRoom = mysql_query("SELECT * FROM temperature");
	
	
	
	while($lRData=mysql_fetch_array($livingRoom)){
	
	$timeDur =  round((($lRData[seq]*8)/60/60) / 24);
	$bat = $lRData[bat]/10.0;
	
	
	echo "	<tr>\n"; 
	echo "		<td class=\"auto-style1\">{$lRData[room]}</td>\n"; 
	echo "		<td class=\"auto-style1\">{$lRData[temp]}&#8451; </td>\n"; 
	echo "		<td class=\"auto-style1\">{$timeDur}</td>\n"; 
	echo "		<td class=\"auto-style1\">{$bat}V</td>\n"; 
	echo "	</tr>\n"; 
	

	
	}
	
	echo "</table>\n"; 
	echo "\n";
?>

				</tbody>
			</table>

			
		</section>
	</div>

</body>
</html>