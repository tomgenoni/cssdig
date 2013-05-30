<?php

    // Create the sidenav properties.
    $prop_html = '<div class="col-left">';
    $i = 0;
    $prop_arr = array("background","color","display","float","font","font-family","font-size","font-style","font-weight","height","line-height","margin","margin-top","margin-right","margin-bottom","margin-left","padding","padding-top","padding-right","padding-bottom","padding-left","overflow","position","width","z-index");
    $prop_checked_arr = array("background","color","font","font-family","font-size","font-weight","height","line-height","margin","padding","position","width","z-index");

    foreach ($prop_arr as $value) {
        $i++;
        $checked_value = "";

        if (in_array($value, $prop_checked_arr)) {
            if ( ! isset($_GET['p'] ) || isset($_GET['p'][$i]) ){
                $checked_value = 'checked="checked"';
            }
        } else {
            if ( isset($_GET['p'][$i]) ) {
                $checked_value = 'checked="checked"';
            }
        }

        if ($i == 14) {
            $prop_html .= '</div><div class="col-right">';
        }

        $prop_html .= '<div>';
        $prop_html .= '<input type="checkbox" name="p['.$i.']" value="'.$value.'" id="prop-'.$value.'"'.$checked_value.'>';
        $prop_html .= '<label for="prop-'.$value.'">'.$value.'</label>';
        $prop_html .= '</div>';
    }

    $prop_html .= '</div>';


    // Load the default HTML, error, or search results.
    function get_include_contents($filename) {
        if (is_file($filename)) {
            ob_start();
            include $filename;
            return ob_get_clean();
        }
        return false;
    }

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
                $output = $results;
            }
            else{
               $output = "<div class='error'><b>" . $url . "</b> doesn't appear to be a valid working website. Please try again.</div>";
            }
        } else {
            $output = "<div class='error'>You did not enter a valid URL.</div>";
        }
    } else {
        $output = get_include_contents('about.html');
    }
?>


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
                <?php echo $prop_html; ?>
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
        <?php echo $output; ?>
    </div>
</body>
</html>

