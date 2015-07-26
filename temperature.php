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
	


	
	
	$LivingRoom = mysql_query("SELECT * FROM tempMeas  WHERE id = 4 LIMIT 0, 10000");
	$MasterBedroom = mysql_query("SELECT * FROM tempMeas  WHERE id = 4 LIMIT 0, 10000");
	
	$outRoom = mysql_query("SELECT * FROM tempMeas WHERE id = 3 LIMIT 7000, 10000");
	

	
	
	while($lRData=mysql_fetch_array($LivingRoom)){
		$lR[] = array($lRData['time'],(float)$lRData['temp']); 
	} 
	while($mBData=mysql_fetch_array($MasterBedroom)){
		$mB[] = array(($mBData['time']),(float)$mBData['bat']); 
	}
	while($outData=mysql_fetch_array($outRoom)){
		$out[] = array(($outData['time']),(float)$outData['temp']); 
		#echo $outData['temp'];
		#echo "<br>";
	}

	#exit(0);
	

?>

<html>
	<head>
		<title>Riddler web client</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<!--  meta http-equiv="X-UA-Compatible" content="chrome=1" -->
		<script type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.7.1/jquery.min.js"></script>
		<script type="text/javascript">
			jQuery.noConflict();
		</script>
		<script type="text/javascript">
		var example = 'line-basic',
			theme = 'default';
		</script>

		<script type="text/javascript">
		
		function openNewWindow(value) {
		 popupWin = window.open('http://riddler.lab.es.aau.dk/plots/bar.php?testNavId=<?echo $testNavId;?>&testNavRate='+Math.floor(value),
		 'open_window',
		 'menubar, toolbar, location, directories, status, scrollbars, resizable, dependent, left=0, top=0')
		 }
		
			(function($){ // encapsulate jQuery

				var chart;
				$(document).ready(function() {
					chart = new Highcharts.Chart({
						chart: {
							renderTo: 'container',
							type: 'spline',
							zoomType: 'x',
							events: {
							click: function(event) {
								 openNewWindow(event.xAxis[0].value); 
								}
							} 
						},
						title: {
							text: 'Temperature'
						},
						subtitle: {
							text: 'Location'
						},
						xAxis: {
						
							gridLineWidth: 0.3,
							title: {
								text: 'Samples'
							},
						},
						yAxis: {
						
							title: {
								text: 'Temperature [c]'
							},
							labels: {
								formatter: function() {
									return this.value
								}
							}
						},
						tooltip: {
							crosshairs: true,
							shared: true
						},
						plotOptions: {
							spline: {
								marker: {
									radius: 4,
									lineColor: '#666666',
									lineWidth: 1
								}
							}
						},
						series: [{
							name: 'Living Room',
							marker: {
								symbol: 'square'
							},
							data: <? echo json_encode($lR);?>

						}, {
							name: 'Master Bedroom',
							marker: {
								symbol: 'diamond'
							},
							data: <? echo json_encode($mB);?>
						}, {
							name: 'Out',
							marker: {
								symbol: 'diamond'
							},
							data: <? echo json_encode($out);?>
						}
						]
					});
				});
				
			})(jQuery);
		</script>

	</head>
	
	<body>
	
		<div id="container" style="min-width: 100%; height: 100%; margin: 0 auto"></div>
		<script src="http://code.highcharts.com/highcharts.js"></script>
		<script src="http://code.highcharts.com/modules/exporting.js"></script>
		
		
	</body>

</html>

