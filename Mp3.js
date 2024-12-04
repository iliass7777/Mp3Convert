const express = require('express');
const { spawn } = require('child_process');
const mp3 = express.Router();
const path = require('path');
const fs = require('fs');

mp3.post('/', (req, res) => {
    const url =req.body.url;  
    const fileName=Date.now()
    const filePath = path.join('Audio'+fileName);  
    if (!url) {
        return res.status(400).send("URL manquante dans la requête");
    }

    const convert = spawn('python', ['mp3.py', url,filePath]);

    convert.stdout.on('data', (data) => {
        console.log(`Output: ${data}`);
    });
    
    convert.stderr.on('data', (data) => {
        console.error(`Erreur: ${data}`);
    });

    convert.on('close', (code) => {  
        if (code === 0) {
            if (fs.existsSync(filePath)) {
                res.sendFile(filePath, (err) => {
                    if (err) {
                        res.status(500).send("Erreur lors de l'envoi du fichier");
                    }
                });
            } else {
                res.status(500).send("Fichier MP3 non trouvé");
            }
        } else {
            res.status(500).send("Erreur de conversion");
        }
    });
});

module.exports = mp3;
