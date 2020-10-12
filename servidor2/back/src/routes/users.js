const { Router } = require('express');
const router =  Router();
const User = require('../models/Users');

router.route('/')
    .get((req,res) => {
        const usu = User.find(function () {
            res.json(usu);    
        });        
    });

module.exports = router;