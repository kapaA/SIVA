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
	
	$timeDur =  ((($lRData[seq]*15)/60) / 24);
	
	echo "{$lRData[room]} {$lRData[temp]} {$lRData[date]} {$timeDur}<br>";

	}
?>