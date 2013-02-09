__author__ = 'flatline'

TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title></title>
    <link rel="stylesheet" href="res/css/style.css?ver={version}" type="text/css">
</head>
<body>
    <div class='fluid-container' style="height:100%">
        <div class='row-fluid' style='height:100%'>
            <div class='span1 toolbar-cntr'>
                <div id='toolbar'>
                    <ul>
                        <li><a href=''>Save</a></li>
                        <li><a href=''>Clear</a></li>
                    </ul>
                </div>
            </div>
            <div class='span6' id='editor' style='height:100%'>

            </div>
            <div class="span5" style="margin-left:5px; height:100%;width:44%" >
                <div id='results' style="overflow: auto"></div>
            </div>
        </div>
    </div>
</body>
<script src='res/js/require.js?ver={version}'></script>
<script>
    require(['{module}']);
</script>
</html>
"""


