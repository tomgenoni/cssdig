<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Array Test</title>
</head>
<body>


<?php

    $prop_html = '<div class="col-left">';
    $i = 0;
    $prop_arr = array("background","color","display","float","font","font-family","font-size","font-style","font-weight","height","line-height","margin","margin-top","margin-right","margin-bottom","margin-left","padding","padding-top","padding-right","padding-bottom","padding-left","overflow","position","width","z-index");
    $prop_checked_arr = array("background","color","font","font-family","font-size","font-weight","height","line-height","padding","position","width","z-index");

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

        if ($i == 3) {
            $prop_html .= '</div><div class="col-right">';
        }

        $prop_html .= '<div>';
        $prop_html .= '<input type="checkbox" name="p['.$i.']" value="'.$value.'" id="prop-'.$value.'"'.$checked_value.'>';
        $prop_html .= '<label for="prop-'.$value.'">'.$value.'</label>';
        $prop_html .= '</div>';
    }

    $prop_html .= '</div>';

    echo $prop_html;

?>

</body>
</html>
