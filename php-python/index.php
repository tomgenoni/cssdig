<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS Report</title>
    <link href='../assets/new.css' rel='stylesheet' type='text/css'>
</head>

    <nav>
        <h1>CSS Peek</h1>
        <p class="desc">
            CSS Peek groups CSS properties and values to help you refactor and standardize. That or just stare in horror.
        </p>
        <p>
            <a href="#">About</a> | <a href="#">GitHub</a>
        </p>
        <form action="" method="get">
            <label for="">Enter a URL</label>
            <input type="text" id="url" name="url" value="http://atomeye.com" />
            <div class="props">
                <div class="col-left">
                    <div>
                        <input type="checkbox" name="p[]" value="background" checked="checked">
                        <label for="">background</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="border">
                        <label for="">border</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="color">
                        <label for="">color</label>
                    </div>
                </div>
                <div class="col-right">
                </div>
            </div>
            <button class="button">Peek</button>
        </form>
    </nav>

    <div class="content">
    <?php
        $url = $_GET['url'];
        $properties = $_GET['p'];
        $properties_separated = implode(",", $properties);
        $cmd = 'python build.py '.$url.' '.$comma_separated;
        $results = shell_exec($cmd);
        echo $results;     
    ?>
    </div>
<!-- <form action="./" method="get">
    <input type="checkbox" name="x[]" value="Bike" />
    <input type="checkbox" name="x[]" value="Car" />
    <input type="checkbox" name="x[]" value="Plane" />
    <input type="submit" value="Submit" />
</form>
 -->

</body>
</html>

