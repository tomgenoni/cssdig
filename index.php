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
                        <input type="checkbox" name="p[1]" value="background" id="prop-background" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][1])){ echo "checked='checked'"; } ?>>
                        <label for="prop-background">background</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[2]" value="color" id="prop-color" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][2])){ echo "checked='checked'"; } ?>>
                        <label for="prop-color">color</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[3]" value="display" id="prop-display" <?php if (isset($_GET['p'][3])){ echo "checked='checked'"; } ?>>
                        <label for="prop-display">display</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[4]" value="float" id="prop-float" <?php if (isset($_GET['p'][4])){ echo "checked='checked'"; } ?>>
                        <label for="prop-float">float</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[5]" value="font" id="prop-font" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][5])){ echo "checked='checked'"; } ?>>
                        <label for="prop-font">font</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[6]" value="font-family" id="prop-font-family" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][6])){ echo "checked='checked'"; } ?>>
                        <label for="prop-font-family">font-family</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[7]" value="font-size" id="prop-font-size" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][7])){ echo "checked='checked'"; } ?>>
                        <label for="prop-font-size">font-size</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[8]" value="font-style" id="prop-font-style" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][8])){ echo "checked='checked'"; } ?>>
                        <label for="prop-font-style">font-style</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[9]" value="font-weight" id="prop-font-weight" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][9])){ echo "checked='checked'"; } ?>>
                        <label for="prop-font-weight">font-weight</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[10]" value="height" id="prop-height" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][10])){ echo "checked='checked'"; } ?>>
                        <label for="prop-height">height</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[11]" value="line-height" id="prop-line-height" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][11])){ echo "checked='checked'"; } ?>>
                        <label for="prop-line-height">line-height</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[12]" value="margin" id="prop-margin" <?php if (isset($_GET['p'][12])){ echo "checked='checked'"; } ?>>
                        <label for="prop-margin">margin</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[13]" value="margin-top" id="prop-margin-top" <?php if (isset($_GET['p'][13])){ echo "checked='checked'"; } ?>>
                        <label for="prop-margin-top">margin-top</label>
                    </div>
                </div>
                <div class="col-right">
                    <div>
                        <input type="checkbox" name="p[14]" value="margin-right" id="prop-margin-right" <?php if (isset($_GET['p'][14])){ echo "checked='checked'"; } ?>>
                        <label for="prop-margin-right">margin-right</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[15]" value="margin-bottom" id="prop-margin-bottom" <?php if (isset($_GET['p'][15])){ echo "checked='checked'"; } ?>>
                        <label for="prop-margin-bottom">margin-bottom</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[16]" value="margin-left" id="prop-margin-left" <?php if (isset($_GET['p'][16])){ echo "checked='checked'"; } ?>>
                        <label for="prop-margin-left">margin-left</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[17]" value="padding" id="prop-padding" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][17])){ echo "checked='checked'"; } ?>>
                        <label for="prop-padding">padding</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[18]" value="padding-top" id="prop-padding-top" <?php if (isset($_GET['p'][18])){ echo "checked='checked'"; } ?>>
                        <label for="prop-padding-top">padding-top</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[19]" value="padding-right" id="prop-padding-right" <?php if (isset($_GET['p'][19])){ echo "checked='checked'"; } ?>>
                        <label for="prop-padding-right">padding-right</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[20]" value="padding-bottom" id="prop-padding-bottom" <?php if (isset($_GET['p'][20])){ echo "checked='checked'"; } ?>>
                        <label for="prop-padding-bottom">padding-bottom</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[21]" value="padding-left" id="prop-padding-left" <?php if (isset($_GET['p'][21])){ echo "checked='checked'"; } ?>>
                        <label for="prop-padding-left">padding-left</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[22]" value="overflow" id="prop-overflow" <?php if (isset($_GET['p'][22])){ echo "checked='checked'"; } ?>>
                        <label for="prop-overflow">overflow</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[23]" value="position" id="prop-position" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][23])){ echo "checked='checked'"; } ?>>
                        <label for="prop-position">position</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[24]" value="width" id="prop-width" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][24])){ echo "checked='checked'"; } ?>>
                        <label for="prop-width">width</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[25]" value="z-index" id="prop-z-index" <?php if ( ! isset($_GET['p'] )){ echo "checked='checked'"; } else if (isset($_GET['p'][25])){ echo "checked='checked'"; } ?>>
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

