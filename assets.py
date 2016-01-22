
from Flask.ext.assets import Bundle, Environment
from .server import app

bundles = {
    'js_files': Bundle(
        'materialize.js',
        output='gen/main.js'
    ),

    'css_files': Bundle(
        'materialize.min.css',
        output='gen/main.css'
    )

    'font_files': Bundle(
        
    )
}
