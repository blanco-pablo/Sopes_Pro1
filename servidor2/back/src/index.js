const app = require('./app');
//require('./database');

function main() {
    app.listen(app.get('port'), 
    ()=> console.log('SERVER OK ',app.get('port')));    
}


main();