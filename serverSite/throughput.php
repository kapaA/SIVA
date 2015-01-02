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
	
	
	$testNavId= $_GET['testNavId'];


	$aDataRequest = mysql_query("SELECT * FROM tempMeas WHERE id = '$testNavId' ORDER BY step");
	
	$testInfoRequest = mysql_query("SELECT * FROM temperature WHERE id = '$testNavId'");
	
	while($testInfo=mysql_fetch_array($testInfoRequest)){
		$testName = $testInfo['room'];
		
	} 
	while($bData=mysql_fetch_array($aDataRequest)){
		$aNC[] = array(gmdate($bData['step']),(float)$bData['data']); 
		$aWoNC[] = array(gmdate($bData['step']),(float)$bData['data']); 
	} 


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
							spacingRight: 20,
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
							text: 'Location: <?echo $testName; ?>'
						},
						xAxis: {
                                                        type: 'datetime',
                                                        labels: {
            format: '{value:%Y-%m-%d}',
            rotation: 45,
            align: 'left'
        },
							gridLineWidth: 0.3,
							title: {
								text: 'Day'
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
							name: 'With Network Coding',
							marker: {
								symbol: 'square'
							},
							data: <? echo json_encode($aNC );?>

						}, {
							name: 'Without Network Coding',
							marker: {
								symbol: 'diamond'
							},
							data: <? echo json_encode($aWoNC );?>
						}]
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

