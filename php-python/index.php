<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Document</title>
</head>
<body>

<?php
    $checked = $_GET['x'];
    $comma_separated = implode(",", $checked);
    $tmp = exec("python build.py '". $comma_separated ."'");
    echo $tmp;
?>

<form action="./" method="get">
    <input type="checkbox" name="x[]" value="Bike" />
    <input type="checkbox" name="x[]" value="Car" />
    <input type="checkbox" name="x[]" value="Plane" />
    <input type="submit" value="Submit" />
</form>


</body>
</html>

