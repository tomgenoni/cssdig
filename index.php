<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CSS Report</title>
    <link href='assets/styles.css' rel='stylesheet' type='text/css'>
</head>

    <nav>
        <h1>CSS Dig</h1>
        <p class="desc">
            CSS Dig groups CSS properties and values to help you refactor and standardize. That or just stare in horror.
        </p>
        <ul class="links">
            <li><a href="#">About</a></li>
            <li><a href="https://github.com/tomgenoni/css-dig">GitHub</a></li>
        </ul>
        <form action="" method="get">
            <label>Enter a URL</label>
            <input type="text" id="url" name="url" placeholder="http://apple.com" />
            <div class="props">
                <div class="col-left">
                    <div>
                        <input type="checkbox" name="p[]" value="background" id="prop-background" checked="checked">
                        <label for="prop-background">background</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="background-size" id="prop-background-size" checked="checked">
                        <label for="prop-background-size">background-size</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="color" id="prop-color" checked="checked">
                        <label for="prop-color">color</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="display" id="prop-display" checked="checked">
                        <label for="prop-display">display</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="float" id="prop-float" checked="checked">
                        <label for="prop-float">float</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="font" id="prop-font" checked="checked">
                        <label for="prop-font">font</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="font-size" id="prop-font-size" checked="checked">
                        <label for="prop-font-size">font-size</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="font-weight" id="prop-font-weight" checked="checked">
                        <label for="prop-font-weight">font-weight</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="font-family" id="prop-font-family" checked="checked">
                        <label for="prop-font-family">font-family</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="font-style" id="prop-font-style" checked="checked">
                        <label for="prop-font-style">font-style</label>
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
                        <input type="checkbox" name="p[]" value="margin" id="prop-margin" checked="checked">
                        <label for="prop-margin">margin</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="margin-top" id="prop-margin-top" checked="checked">
                        <label for="prop-margin-top">margin-top</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="margin-right" id="prop-margin-right" checked="checked">
                        <label for="prop-margin-right">margin-right</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="margin-bottom" id="prop-margin-bottom" checked="checked">
                        <label for="prop-margin-bottom">margin-bottom</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="margin-left" id="prop-margin-left" checked="checked">
                        <label for="prop-margin-left">margin-left</label>
                    </div>
                </div>
                <div class="col-right">
                    <div>
                        <input type="checkbox" name="p[]" value="overflow" id="prop-overflow" checked="checked">
                        <label for="prop-overflow">overflow</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="position" id="prop-position" checked="checked">
                        <label for="prop-position">position</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="top" id="prop-top" checked="checked">
                        <label for="prop-top">top</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="right" id="prop-right" checked="checked">
                        <label for="prop-right">right</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="bottom" id="prop-bottom" checked="checked">
                        <label for="prop-bottom">bottom</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="left" id="prop-left" checked="checked">
                        <label for="prop-left">left</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="padding" id="prop-padding" checked="checked">
                        <label for="prop-padding">padding</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="padding-top" id="prop-padding-top" checked="checked">
                        <label for="prop-padding-top">padding-top</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="padding-right" id="prop-padding-right" checked="checked">
                        <label for="prop-padding-right">padding-right</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="padding-bottom" id="prop-padding-bottom" checked="checked">
                        <label for="prop-padding-bottom">padding-bottom</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="padding-left" id="prop-padding-left" checked="checked">
                        <label for="prop-padding-left">padding-left</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="width" id="prop-width" checked="checked">
                        <label for="prop-width">width</label>
                    </div>
                    <div>
                        <input type="checkbox" name="p[]" value="zoom" id="prop-zoom" checked="checked">
                        <label for="prop-zoom">zoom</label>
                    </div>

                </div>
            </div>
            <button class="button">Peek</button>
        </form>
    </nav>

    <div class="content">
    <?php


        $url = $_GET['url'];
        $properties = $_GET['p'];

        if (isset($url) && isset($properties)) {

            $url_parsed = parse_url($url);

            if ($url_parsed['scheme'] == 'http' || $url_parsed['scheme'] == 'https'){

                $handle = @fopen($url,'r');
                if ($handle !== false){
                    $properties_separated = implode(",", $properties);
                    $cmd = 'python build.py '.$url.' '.$properties_separated;
                    $results = shell_exec($cmd);
                    echo $results;
                }
                else{
                   echo "<div class='error'><b>" . $url . "</b> doesn't appear to be a valid, working website. Please try again.</div>";
                }
            } else {
                echo "<div class='error'>The URL must be in the form of http://domain.com or https://domain.com, with or without 'www'.</div>";
            }
        }

    ?>
    </div>

</body>
</html>

