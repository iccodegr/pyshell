define(['jquery','python-mode','./pythonHint'],
function($, CodeMirror, PythonHint){
    var ns = {},
        __cm=null,
        $out=$('#results');

    CodeMirror.commands.autocomplete = function(cm){
        CodeMirror.showHint(cm, PythonHint.pythonHint);
    };

    function __wrapOutput(script, result){
        var html = [
            "<div class='result'>"
            ,"<div class='source'><pre>"
            ,script
            ,"</pre>"
            ,"</div>"
            ,"<div class='output'>"
            ,"<pre>"
            ,result
            ,"</pre>"
            ,"</div>"
            ,"</div>"
            ,"<hr/>"
        ];

        return html.join("")
    }

    function __onKeyDown(ctx, evt){
        if (evt.type!="keydown") return;

        var sel = "";

        if (evt.ctrlKey && evt.keyCode == 13){
            sel = __cm.getSelection() || __cm.getValue();
            $.ajax({
                'url':'execute',
                'type':'post',
                'dataType':'text',
                'data':{
                    'script':sel
                }
            })
                .then(function(res){
                    $out.append(__wrapOutput(sel, res))
                        .animate({scrollTop:$out.prop('scrollHeight')})
                })
                .fail(function(res){
                    $out.append("<div class='error'>Unable to execute</div>")
                        .animate({scrollTop:$out.prop('scrollHeight')})
                })
        }
    }

    ns.init = function(){
        __cm = new CodeMirror($('#editor')[0],{
            lineNumbers: true,
            indentUnit: 4,
            tabMode: "shift",
            matchBrackets: true,
            autofocus: true,
            theme: 'ambiance',
            'mode':'python',
            'extraKeys': {'Ctrl-Space':'autocomplete'},
            'onKeyEvent': __onKeyDown
        });
    };

    return ns;
});
