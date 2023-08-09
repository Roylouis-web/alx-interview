#!/usr/bin/node

const process = require('process');
const request = require('request');
const arg = process.argv[2];

function printCharacters () {
  request(`https://swapi-api.alx-tools.com/api/films/${arg}`, async (error, response, body) => {
    if (error) {
      console.log(error);
    }

    const characterUrls = JSON.parse(body).characters;
    for (const characterUrl of characterUrls) {
      const url = await printACharacter(characterUrl);
      console.log(url);
    }
  });
}

function printACharacter (url) {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        console.log(error);
      }
      resolve(JSON.parse(body).name);
    });
  });
}

printCharacters();
