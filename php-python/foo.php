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
</body>
</html>

