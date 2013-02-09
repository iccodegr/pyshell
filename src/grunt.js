module.exports = function (grunt){
    grunt.loadNpmTasks('grunt-contrib-requirejs');
    grunt.loadNpmTasks('grunt-remove-logging');
    grunt.loadNpmTasks('grunt-contrib-less');

    grunt.initConfig({
        less: {
            compile: {
                options: {
                    paths: ['frontend/css']
                },
                files: {
                    'frontend/css/style.css':'frontend/css/style.less'
                }
            }
        },
        requirejs: {
            js: {
                options: {
                    baseUrl:'frontend/js',
                    name:'../vendor/almond',
                    out:'shell.dist.js',
                    include:['shell'],
                    optimize:'none',
                    pragmas: {
                      production:true
                    },
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
                }
            },
            css: {
                options: {
                    baseUrl: 'frontent/css',
                    optimizeCss: "standard.keepLines",
                    cssIn: 'frontend/css/style.css',
                    out: 'pyshell/frontend/css/style.css'
                }
            }
        },
        min:[
            {
                src:'shell.dist.js',
                dest:'pyshell/frontend/js/require.js'
            }
        ]
    });


    grunt.registerTask('default', ['less', 'requirejs', 'min']);
}
