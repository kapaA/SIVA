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
	


	
	
	$LivingRoom = mysql_query("SELECT * FROM tempMeas  WHERE id = 1 LIMIT 3000, 10000");
	
	$MasterBedroom = mysql_query("SELECT * FROM tempMeas  WHERE id = 2 LIMIT 0, 900");
	$outRoom = mysql_query("SELECT * FROM tempMeas WHERE id = 3 LIMIT 0, 10000");
	

	
	
	while($lRData=mysql_fetch_array($LivingRoom)){
		$lR[] = array($lRData['time'],(float)$lRData['temp']); 
	} 
	while($mBData=mysql_fetch_array($MasterBedroom)){
		$mB[] = array(($mBData['time']),(float)$mBData['temp']); 
	}
	while($outData=mysql_fetch_array($outRoom)){
		$out[] = array(($outData['step']),(float)$outData['temp']); 
		#echo $outData['step']; echo " "; echo $outData['temp'];
		#echo "<br>";
	}

	#exit(0);
	

?>
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
		<title>Highstock Example</title>

		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
		<style type="text/css">
${demo.css}
		</style>
		<script type="text/javascript">
$(function () {
    $.getJSON('http://www.highcharts.com/samples/data/jsonp.php?filename=aapl-c.json&callback=?', function (data) {

        // Create the chart
        $('#container').highcharts('StockChart', {

            rangeSelector: {
                selected: 1
            },

            title: {
                text: 'AAPL Stock Price'
            },

            series: [{
                name: 'AAPL Stock Price',
                data: <? echo json_encode($out);?>,
                type: 'spline',
                tooltip: {
                    valueDecimals: 2
                }
            }]
        });
    });
});
		</script>
	</head>
	<body>
<script src="../../js/highstock.js"></script>
<script src="../../js/modules/exporting.js"></script>


<div id="container" style="height: 400px"></div>
	</body>
</html>
