<!DOCTYPE html>
<html>
<head>
	<title>Json</title>
</head>
<body>

<?php
	//file menjadi string
	$result = file_get_contents('biodata.json');
	//string menjadi object
	$json_object = json_decode($result, true);


	//print data object
	echo "Nama : ".$json_object['nama']."<br/>";
	echo "Addres : ".$json_object['addres']."<br/>";
	echo "Hobbies : ".
	$json_object['hobbies']
	// foreach ($json_object['hobbies'] as $value) {
 //    	echo "$value <br>";
	// }
	."<br/>";
	echo "Married : ".$json_object['is_married']."<br/>";
	echo "School : ".$json_object['school']."<br/>";
	echo "Skills : ".$json_object['skills'];
?>
</body>
</html>
