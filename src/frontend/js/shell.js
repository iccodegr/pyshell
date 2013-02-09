//>>excludeStart("production", pragmas.production);
requirejs.config({
    'baseUrl':'res/js',
    'paths':{
        'codemirror':'../vendor/codemirror-3.02/lib/codemirror',
        'python-mode':'../vendor/codemirror-3.02/mode/python/python'
    },
    'shim':{
        'codemirror': {
            'exports':'CodeMirror'
        },
        'python-mode': {
            'deps':['codemirror','shell/showHint'],
            'exports':'CodeMirror'
        }
    }
});
//>>excludeEnd("production");


define(function(require){
    var shell = require('shell/main');
    shell.init()
});
