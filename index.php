<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS Dig</title>
    <link href='assets/styles.css' rel='stylesheet' type='text/css'>
</head>
<body>
    <nav>

        <h1><a href=".">CSS Dig</a></h1>
        <form action="" method="get">
            <input type="text" id="url" name="url" placeholder="Enter URL" value="<?php echo $_GET['url']; ?>"/>
            <div class="props">
                <div class="col-left">
                    <div>
                        <input type="checkbox" name="p[1]" value="background" id="prop-background" checked="checked">
                        <label for="prop-background">background</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[2]" value="color" id="prop-color" checked="checked">
                        <label for="prop-color">color</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[3]" value="display" id="prop-display" <?php if (isset($_GET['p'][3])){ echo "checked='checked'"; } ?>>
                        <label for="prop-display">display</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="float" id="prop-float">
                        <label for="prop-float">float</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="font" id="prop-font" checked="checked">
                        <label for="prop-font">font</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="font-family" id="prop-font-family" checked="checked">
                        <label for="prop-font-family">font-family</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="font-size" id="prop-font-size" checked="checked">
                        <label for="prop-font-size">font-size</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="font-style" id="prop-font-style" checked="checked">
                        <label for="prop-font-style">font-style</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="font-weight" id="prop-font-weight" checked="checked">
                        <label for="prop-font-weight">font-weight</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="height" id="prop-height" checked="checked">
                        <label for="prop-height">height</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="line-height" id="prop-line-height" checked="checked">
                        <label for="prop-line-height">line-height</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="margin" id="prop-margin">
                        <label for="prop-margin">margin</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="margin-top" id="prop-margin-top">
                        <label for="prop-margin-top">margin-top</label>
                    </div>
                </div>
                <div class="col-right">
                    <div>
                        <input type="checkbox" name="p[]" value="margin-right" id="prop-margin-right">
                        <label for="prop-margin-right">margin-right</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="margin-bottom" id="prop-margin-bottom">
                        <label for="prop-margin-bottom">margin-bottom</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="margin-left" id="prop-margin-left">
                        <label for="prop-margin-left">margin-left</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="padding" id="prop-padding" checked="checked">
                        <label for="prop-padding">padding</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="padding-top" id="prop-padding-top">
                        <label for="prop-padding-top">padding-top</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="padding-right" id="prop-padding-right">
                        <label for="prop-padding-right">padding-right</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="padding-bottom" id="prop-padding-bottom">
                        <label for="prop-padding-bottom">padding-bottom</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="padding-left" id="prop-padding-left">
                        <label for="prop-padding-left">padding-left</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="overflow" id="prop-overflow">
                        <label for="prop-overflow">overflow</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="position" id="prop-position" checked="checked">
                        <label for="prop-position">position</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="width" id="prop-width" checked="checked">
                        <label for="prop-width">width</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="z-index" id="prop-z-index" checked="checked">
                        <label for="prop-z-index">z-index</label>
                    </div>

                </div>
            </div>
            <textarea name="xp" id="xp" placeholder="Enter any additional, comma-separated properties to search: top, left, background-size, etc."><?php echo $_GET['xp']; ?></textarea>
            <button class="button">Dig</button>
        </form>

        <ul class="links">
            <li><a href=".">About</a></li>
            <li><a href="https://github.com/tomgenoni/css-dig">GitHub</a></li>
            <li><a href="https://twitter.com/tomgenoni">@tomgenoni</a></li>
        </ul>

    </nav>

    <div class="content">
    <?php

        $url = $_GET['url'];
        $properties = $_GET['p'];
        $extra_properties = $_GET['xp'];

        $extra_properties = "'".$extra_properties."'";

        if (isset($url) && isset($properties)) {

            $url_parsed = parse_url($url);

            if ($url_parsed['scheme'] == '') {
                $url = "http://" . $url;
            }

            $url_parsed = parse_url($url);

            if ($url_parsed['scheme'] == 'http' || $url_parsed['scheme'] == 'https'){

                $handle = @fopen($url,'r');
                if ($handle !== false){
                    $properties = implode(",", $properties);
                    $cmd = 'python build.py '.$url.' '.$properties.' '.$extra_properties;
                    $results = shell_exec($cmd);
                    echo $results;
                }
                else{
                   echo "<div class='error'><b>" . $url . "</b> doesn't appear to be a valid working website. Please try again.</div>";
                }
            } else {
                echo "<div class='error'>You did not enter a valid URL.</div>";
            }
        } else {
            include 'about.html';
        }

    ?>
    </div>

</body>
</html>

